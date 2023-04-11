import json
import boto3
import base64

def lambda_handler(event, context):
    
    eventBody = json.loads(json.dumps(event))['body']
    
    imageBase64 = json.loads(eventBody)['Image']
    
    # Amazon Textract client
    textract = boto3.client('textract')
    
    # Call Amazon Textract
    response = textract.detect_document_text(
        Document={
            'Bytes': base64.b64decode(imageBase64)
        })
        
    detectedText = ''

    # Print detected text
    for item in response['Blocks']:
        if item['BlockType'] == 'LINE':
            detectedText += item['Text'] + '\n'     

    return {
        'statusCode': 200,
        'body': json.dumps(detectedText)
    }