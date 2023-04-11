const AWS = require("aws-sdk");
const textract = new AWS.Textract();

exports.handler = async (event) => {
  if (event) {
    const fileObj = event.Records[0];
    const bucketName = fileObj.s3.bucket.name;
    const fileName = fileObj.s3.object.key;
    
    console.log(`Bucket: ${bucketName} ::: Key: ${fileName}`);
    
    const response = await textract.analyzeDocument({
      Document: {
        S3Object: {
          Bucket: bucketName,
          Name: fileName,
          
        },
        
      },
      FeatureTypes: ["FORMS", "TABLES"],
      
    }).promise();
    
    console.log(JSON.stringify(response));
    
    return {
      statusCode: 200,
      body: JSON.stringify("Hello from Lambda"),
      
    };