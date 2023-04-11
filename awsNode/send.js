const fs = require('fs');
const { PutObjectCommand, S3Client } = require('@aws-sdk/client-s3');
import { TextractClient, StartDocumentAnalysisCommand } from '@aws-sdk/client-textract';

async function uploadToS3(file) {
  const s3 = new S3Client({ region: process.env.AWS_REGION });

  const fileContent = fs.readFileSync(file.path);

  const params = {
    Bucket: process.env.AWS_BUCKET_NAME, // Create bucket in S3 with AWS console and save name in .env
    Key: file.originalname,
    Body: fileContent,
  };

  try {
    return await s3.send(new PutObjectCommand(params));
  } catch (err) {
    console.log('ERROR', err);
    return err;
  }  
};



async function readFileWithTextract(fileName) {
  const textract = new TextractClient({ region: process.env.AWS_REGION });

  const params = {
    DocumentLocation: {
      S3Object: {
        Bucket: process.env.AWS_BUCKET_NAME, // This will be the same bucket that you use to save the file
        Name: fileName,
      },
    },
    FeatureTypes: ['TABLES']
  };

  const command = new StartDocumentAnalysisCommand(params);
  
  try {
    return await textract.send(command);
  } catch (err) {
    // Handle error
    console.log('ERROR', err);
    return err;
  }
};