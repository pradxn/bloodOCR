const express = require("express");
const multer = require("multer");
const aws = require("aws-sdk");
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Hello World!')
})

aws.config.update({
    accessKeyId: 'AKIAU2V2Z7VMCKWDM3PO',
    secretAccessKey: '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',
    region: 'ap-south-1'
  });
  
  // create an S3 instance
  const s3 = new aws.S3();
  
  // set up multer for file handling
  const upload = multer();  

app.post('/upload', upload.single("file"), (req, res) => {
    // get file from the request
  const file = req.file;

  // create a unique filename for the file in S3
  const s3FileName = `${Date.now()}-dummyFile`;
  //add file name logic
  
  // set up S3 upload parameters
  const params = {
    Bucket: "aws-api-report",
    Key: s3FileName,
    Body: file.buffer,
    ContentType: file.mimetype,
    ACL: "public-read"
  };
  console.log(params)
  // upload the file to S3
  s3.upload(params, (error, data) => {
    if (error) {
      return res.status(500).send(error);
    }
    
    // return the URL of the file in S3
    return res.status(200).send({ location: data.Location });
  });
  })

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
/////////////////////////////////


const AWS = require('aws-sdk');
const cloudwatchlogs = new AWS.CloudWatchLogs({
  accessKeyId: 'AKIAU2V2Z7VMCKWDM3PO',
  secretAccessKey: 'W/yR8K9CSDal0LOFfn/bO1b+VH10cSbHqnxHZ8vr',
  region: 'ap-south-1'
});

// Define your AWS region and log group name
const region = 'ap-south-1';
const logGroupName = '/aws/lambda/awsAPIfunction';

app.get('/logs', async (req, res) => {
  try {
    let nextToken = null;
    let logs = [];

    do {
      // Retrieve the logs from CloudWatch using the FilterLogEvents API action
      const logsResponse = await cloudwatchlogs.filterLogEvents({
        logGroupName: logGroupName,
        startTime: req.query.startTime,
        endTime: req.query.endTime,
        filterPattern: req.query.filterPattern,
        nextToken: nextToken
      }).promise();

      // Add the logs to the array
      logs = logs.concat(logsResponse.events.map(event => ({
        message: event.message
      })));

      // Set the nextToken to fetch the next set of events
      nextToken = logsResponse.nextToken;
    } while (nextToken);

    // Return the logs as an API response
    res.json(logs);
  } catch (error) {
    console.error(error);
    res.status(500).send('Internal Server Error');
  }
});

/*
// Define your API endpoint that will return the logs
app.get('/logs', async (req, res) => {
  try {
    // Retrieve the logs from CloudWatch using the FilterLogEvents API action
    const logsResponse = await cloudwatchlogs.filterLogEvents({
      logGroupName: logGroupName,
      startTime: req.query.startTime,
      endTime: req.query.endTime,
      filterPattern: req.query.filterPattern
    }).promise();

    // Format the logs as a JSON response
    const logs = logsResponse.events.map(event => ({
      message: event.message
    }));

    // Return the logs as an API response
    res.json(logs);
  } catch (error) {
    console.error(error);
    res.status(500).send('Internal Server Error');
  }
});
*/


/*
API application, a single API, reportSerice
1. upload file to s3, call textract and table should be responded back in JSON format
2. wait until textraction
3. respond back with data in required form
*/