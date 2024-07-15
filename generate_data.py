import json
import random
import string
import xml.etree.ElementTree as ET

def get_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def get_random_number():
    return random.randint(0, 100)

def get_random_date():
    start = '2020-01-01T00:00:00Z'
    end = '2023-12-31T23:59:59Z'
    return start  # You can enhance this to generate a random date within the range

def generate_data(number_of_records):
    data = []
    for _ in range(number_of_records):
        record = {
            "field1": get_random_string(),
            "field2": get_random_number(),
            "field3": get_random_date()
        }
        data.append(record)
    return data

def save_as_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def save_as_xml(data, filename):
    root = ET.Element("records")
    for record in data:
        rec_elem = ET.SubElement(root, "record")
        for key, value in record.items():
            field_elem = ET.SubElement(rec_elem, key)
            field_elem.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)

# Generate 100 records
data = generate_data(100)

# Save data as JSON
save_as_json(data, 'data.json')

# Save data as XML
save_as_xml(data, 'data.xml')

