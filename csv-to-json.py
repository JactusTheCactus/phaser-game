import csv
import json

def csv_to_json(csv_file, json_file):
    # Read the CSV file
    with open(csv_file, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        data = {}
        
        # Convert the CSV rows to dictionaries, using the 'id' as the key and removing 'id' from the dictionary
        for row in csv_reader:
            id_value = row.pop('id')  # Remove 'id' and use it as the key
            data[id_value] = row
    
    # Sort the dictionary by the keys (the 'id' values) alphabetically
    sorted_data = {key: data[key] for key in sorted(data)}

    # Write the sorted JSON data to a file
    with open(json_file, mode='w', encoding='utf-8') as file:
        json.dump(sorted_data, file, indent=2)

# Example usage
csv_file = 'data.csv'  # Replace with your CSV file path
json_file = 'data.json'  # Replace with the desired output JSON file path
csv_to_json(csv_file, json_file)