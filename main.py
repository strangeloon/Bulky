import json
import os
import shutil

def rename_files(json_file_path, directory_path):
    # Load the JSON data from the file
    with open(json_file_path, "r") as f:
        data = json.load(f)

    # Rename the files using the data from the JSON object
    for item in data:
        old_file_name = os.path.join(directory_path, item["old_name"])
        new_file_name = os.path.join(directory_path, item["new_name"])
        shutil.move(old_file_name, new_file_name)

    print("Files have been renamed successfully!")

# Example usage
json_file_path = "data.json"
directory_path = "files"
rename_files(json_file_path, directory_path)
