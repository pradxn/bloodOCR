import json
import uuid

#code for parsing JSON based on type of word data
def extract_text(response, extract_by="WORD"):
    line_text = []
    for block in response["Blocks"]:
        if block["BlockType"] == extract_by:
            line_text.append(block["Text"])
    return line_text


def map_word_id(response):
    word_map = {}
    for block in response["Blocks"]:
        if block["BlockType"] == "WORD":
            word_map[block["Id"]] = block["Text"]
        if block["BlockType"] == "SELECTION_ELEMENT":
            word_map[block["Id"]] = block["SelectionStatus"]
    return word_map


def extract_table_info(response, word_map):
    row = []
    table = {}
    ri = 0
    flag = False

    for block in response["Blocks"]:
        if block["BlockType"] == "TABLE":
            key = f"table_{uuid.uuid4().hex}"
            table_n = +1
            temp_table = []

        if block["BlockType"] == "CELL":
            if block["RowIndex"] != ri:
                flag = True
                row = []
                ri = block["RowIndex"]

            if "Relationships" in block:
                for relation in block["Relationships"]:
                    if relation["Type"] == "CHILD":
                        row.append(" ".join([word_map[i] for i in relation["Ids"]]))
            else:
                row.append(" ")

            if flag:
                temp_table.append(row)
                table[key] = temp_table
                flag = False
    return table


def get_key_map(response, word_map):
    key_map = {}
    for block in response["Blocks"]:
        if block["BlockType"] == "KEY_VALUE_SET" and "KEY" in block["EntityTypes"]:
            for relation in block["Relationships"]:
                if relation["Type"] == "VALUE":
                    value_id = relation["Ids"]
                if relation["Type"] == "CHILD":
                    v = " ".join([word_map[i] for i in relation["Ids"]])
                    key_map[v] = value_id
    return key_map


def get_value_map(response, word_map):
    value_map = {}
    for block in response["Blocks"]:
        if block["BlockType"] == "KEY_VALUE_SET" and "VALUE" in block["EntityTypes"]:
            if "Relationships" in block:
                for relation in block["Relationships"]:
                    if relation["Type"] == "CHILD":
                        v = " ".join([word_map[i] for i in relation["Ids"]])
                        value_map[block["Id"]] = v
            else:
                value_map[block["Id"]] = "VALUE_NOT_FOUND"

    return value_map


def get_kv_map(key_map, value_map):
    final_map = {}
    for i, j in key_map.items():
        final_map[i] = "".join(["".join(value_map[k]) for k in j])
    return final_map

print("...................................................................")


f = open('analyzeDocResponse.json')
response = json.load(f)


word_map = map_word_id(response)
table = extract_table_info(response, word_map)

def print_table(data):
    for key, values in data.items():
        print("\n")
        for value in values:
            row = "|".join([str(x).ljust(20) for x in value])
            print(row)
                    
print_table(table)

row_name = input("Enter test name: ")

def extract_serum_data(table):
    req_tables = []
    for table_name, table in table.items():
        for row in table:
            if row_name in row[0]:
                req_tables.append(table)
    return req_tables
row = extract_serum_data(table)

for data in row[0]:
    if row_name.lower() in ' '.join(data).lower():
        print(data)
        test_name = data[0]
        result = data[1]
        units = data[2]
        bioRange = data[3]
        #method = data[4]
        print("\n")
        print(f"Test Description: {test_name}")
        print(f"Result: {result}")
        print(f"Units: {units}")
        print(f"Reference Ranges: {bioRange}")

print('\n')
print("...................................................................")
######################
print("...................................................................")
'''
def extract_serum_data(table, row_names):
    req_tables = []
    for table_name, table in table.items():
        for row in table:
            if any(row_name.lower() in ' '.join(row).lower() for row_name in row_names):
                req_tables.append(table)
    return req_tables

row_names = input("Enter test names separated by commas: ")
print('\n')
row_names = row_names.split(",")

rows = extract_serum_data(table, row_names)

for row in rows:
    for data in row:
        if any(row_name.lower() in ' '.join(data).lower() for row_name in row_names):
            print(data)
            test_name = data[0]
            result = data[1]
            units = data[2]
            bioRange = data[3]
            #method = data[4]
            print("\n")
            print(f"Test Description: {test_name}")
            print(f"Result: {result}")
            print(f"Units: {units}")
            print(f"Reference Ranges: {bioRange}")
            print('\n')
print('\n')
'''

def extract_serum_data(table, row_names):
    req_tables = []
    for table_name, table in table.items():
        for row in table:
            if any(row_name.lower() in ' '.join(row).lower() for row_name in row_names):
                req_tables.append(table)
                break
    return req_tables


word_map = map_word_id(response)
table = extract_table_info(response, word_map)

def print_table(data):
    for key, values in data.items():
        print("\n")
        for value in values:
            row = "|".join([str(x).ljust(20) for x in value])
            print(row)
                    
print_table(table)

row_names = input("Enter test names separated by commas: ")
row_names = row_names.split(',')

rows = extract_serum_data(table, row_names)

for row in rows:
    for data in row:
        if any(row_name.lower() in ' '.join(data).lower() for row_name in row_names):
            print(data)
            test_name = data[0]
            result = data[1]
            units = data[2]
            bioRange = data[3]
            #method = data[4]
            print("\n")
            print(f"Test Description: {test_name}")
            print(f"Result: {result}")
            print(f"Units: {units}")
            print(f"Reference Ranges: {bioRange}")
