from core import ArchitectureGenerator
import os

BASE_URL = f"http://localhost:{os.getenv('PORT')}"


async def resolve_generate_architecture(
    _,
    info,
    sos,
    mission_file_json,
    css_behavior_file_json,
    valid_css_combinations_file_json,
):
    architecture_generator = ArchitectureGenerator()
    await architecture_generator.generate_architectural_file(
        sos, mission_file_json, css_behavior_file_json, valid_css_combinations_file_json
    )
    file_saved = architecture_generator.save_file()
    information = f"Architecture file saved in '{BASE_URL}/{file_saved}'"

    return {
        "architeture_file": f"{BASE_URL}/{file_saved}",
        "information": f"{information}",
    }
