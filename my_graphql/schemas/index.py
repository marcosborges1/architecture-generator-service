type_defs = """
        type Query {
                generate_architeture(sos:String!, mission_file_json:String!, css_behavior_file_json:String!, valid_css_combinations_file_json:String!): architeture_file_output!
        }

        type architeture_file_output @key(fields: "architeture_file") {
                architeture_file: String!
                information: String!
        }
"""
