import json

row_name = input("Enter test name: ")

def map_word_id(response):
    word_map = {}
    for page in response:
        for word in page['words']:
            word_map[word['id']] = word['text']
    return word_map

def extract_table_info(response, word_map):
    table_map = {}
    for page in response:
        for table in page['tables']:
            table_rows = []
            for row in table['rows']:
                table_rows.append([word_map[word_id] for word_id in row['wordIds']])
            table_map[table['title']] = table_rows
    return table_map

def print_table(data):
    for key, values in data.items():
        print("\n")
        for value in values:
            row = "|".join([str(x).ljust(20) for x in value])
            print(row)

def extract_serum_data(table, row_names):
    req_tables = []
    for table_name, table in table.items():
        for row in table:
            if any(row_name.lower() in name.lower() for name in row_names):
                req_tables.append(row)
    return req_tables

with open('analyzeDocResponse.json') as f:
    response = json.load(f)

word_map = map_word_id(response)
table = extract_table_info(response, word_map)

print_table(table)

row_names = input("Enter test names separated by commas: ").split(",")
rows = extract_serum_data(table, row_names)

for data in rows:
    print(data)
    test_name = data[0]
    result = data[1]
    units = data[2]
    bioRange = data[3]
    # method = data[4]
    print("\n")
    print(f"Test Description: {test_name}")
    print(f"Result: {result}")
    print(f"Units: {units}")
    print(f"Reference Ranges: {bioRange}")
