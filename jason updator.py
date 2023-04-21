import json
import openpyxl

def update_json(excel_file_path, json_file_path):
    # Load the Excel workbook and get the active sheet
    workbook = openpyxl.load_workbook(excel_file_path)
    sheet = workbook.active

    # Convert the data to a list of dictionaries
    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        old_name, new_name = row
        data.append({
            "old_name": old_name,
            "new_name": new_name
        })

    # Write the data to the JSON file
    with open(json_file_path, "w") as f:
        json.dump(data, f)

    print("JSON file updated successfully!")

# Example usage
excel_file_path = "data.xlsx"
json_file_path = "data.json"
update_json(excel_file_path, json_file_path)
