import json

# A Python Dictionary
my_data = {"name": "Gemini", "is_awesome": True, "rank": None}

# 1. Convert to JSON String (Serialization)
json_string = json.dumps(my_data)
print(f"JSON String: {json_string}")

# 2. Convert back to Python Dictionary (Deserialization)
back_to_python = json.loads(json_string)
print(f"Python Dict: {back_to_python}")