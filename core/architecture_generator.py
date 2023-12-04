import re
import json
import os
import aiohttp
from core.utils import Utils


class ArchitectureGenerator:
    def __init__(self):
        self.architectural_file = []

    async def open_file(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    raise ValueError(f"Error {response.status}: {response.reason}")
                return await response.json()  # Parse JSON and return the content

    def read_json(self, file_path):
        try:
            with open(file_path, "r") as file:
                # Load JSON content from the file
                data = json.load(file)
                return data
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except json.JSONDecodeError:
            print(f"Error reading the JSON file: {file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def update_css_messages_according_to_their_files(self, css, messages):
        updated_messages = []

        for message in messages:
            from_prefix = message[
                "from"
            ].lower()  # Lowercase for case-insensitive comparison
            to_prefix = message["to"].lower()

            from_matches = [
                css_item for css_item in css if css_item.lower().startswith(from_prefix)
            ]
            to_matches = [
                css_item for css_item in css if css_item.lower().startswith(to_prefix)
            ]

            for from_match in from_matches:
                for to_match in to_matches:
                    new_message = (
                        message.copy()
                    )  # Create a copy of the original message
                    new_message["from"] = from_match
                    new_message["to"] = to_match
                    updated_messages.append(new_message)

        return updated_messages

    def find_equal_items(self, list1, list2):
        def preprocess_list(lst):
            new_list = []
            for item in lst:
                new_item = (
                    item.copy()
                )  # Create a copy to avoid modifying the original item
                message = new_item.get("message", "")
                # Remove 'in' and 'out' from message
                new_item["message"] = message.replace("in", "").replace("out", "")
                # Normalize the case for comparison
                new_item = {k: v for k, v in new_item.items()}
                new_list.append(new_item)
            return new_list

        normalized_list1 = preprocess_list(list1)
        normalized_list2 = preprocess_list(list2)

        equal_items = [item for item in normalized_list1 if item in normalized_list2]
        return equal_items

    async def get_css_names(self, css_behavior_file_json):
        css_list = await self.open_file(css_behavior_file_json)
        css_names = []
        for cs in css_list:
            for key in cs:
                css_names.append(key)
        return css_names

    async def generate_architectural_file(
        self,
        sos_name,
        mission_file_json,
        css_behavior_file_json,
        valid_css_combinations_file_json,
    ):
        css_names = await self.get_css_names(css_behavior_file_json)
        first_sentece = f'From the top perspective, {sos_name} are made of {", ".join(css_names[:-1]) + ", and " + css_names[-1]}!'
        self.architectural_file.append(first_sentece)
        self.architectural_file.append("\n")

        pairs = await self.open_file(mission_file_json)
        valid_css_combination_list = await self.open_file(
            valid_css_combinations_file_json
        )
        for pair in pairs:
            pair_updated = self.update_css_messages_according_to_their_files(
                css_names, pair
            )
            valid_communications = self.find_equal_items(
                pair_updated, valid_css_combination_list
            )

            if valid_communications:
                for v in valid_communications:
                    # Create Scenario
                    sentence = f"From the top perspective, {v['from']} sends {v['message']} to {v['to']}"
                    self.architectural_file.append(f"{sentence}!")
                if pair != pairs[-1]:
                    self.architectural_file.append("\n")

    def save_file(self, file_name="architecture"):
        return Utils.save_file(file_name, "\n".join(self.architectural_file))
