import csv
import json

def csv_to_json(file):
    # Read the CSV file
    with open(f'{file}.csv', mode='r', encoding='utf-8') as f:
        csv_reader = csv.DictReader(f)
        data = {}
        
        # Convert the CSV rows to dictionaries, using the 'id' as the key and removing 'id' from the dictionary
        for row in csv_reader:
            id_value = row.pop('id')  # Remove 'id' and use it as the key
            data[id_value] = row
    
    # Write the JSON data to a file
    with open(f'{file}.json', mode='w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    print(f'{file}.csv succesfully converted to {file}.json')

# Example usage
file = 'data'
csv_to_json(file)