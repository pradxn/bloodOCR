import json
import boto3
from pprint import pprint
from parser_1 import (
    extract_text,
    map_word_id,
    extract_table_info,
    get_key_map,
    get_value_map,
    get_kv_map,
)


def lambda_handler(event, context):
    textract = boto3.client("textract")
    if event:
        file_obj = event["Records"][0]
        bucketname = str(file_obj["s3"]["bucket"]["name"])
        filename = str(file_obj["s3"]["object"]["key"])

        print(f"Bucket: {bucketname} ::: Key: {filename}")

        response = textract.analyze_document(
            Document={
                "S3Object": {
                    "Bucket": bucketname,
                    "Name": filename,
                }
            },
            FeatureTypes=["FORMS", "TABLES"],
        )

        print(json.dumps(response))

        raw_text = extract_text(response, extract_by="LINE")
        word_map = map_word_id(response)
        table = extract_table_info(response, word_map)
        key_map = get_key_map(response, word_map)
        value_map = get_value_map(response, word_map)
        final_map = get_kv_map(key_map, value_map)

        print(json.dumps(table))
        print(json.dumps(final_map))
        print(raw_text)
        
        def print_table(data):
            for key, values in data.items():
                print("\n")
                for value in values:
                    row = "|".join([str(x).ljust(20) for x in value])
                    print(row)
                    
        print_table(table)

    return {"statusCode": 200, "body": json.dumps("Hello from Lambda")}