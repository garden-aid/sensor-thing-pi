'use strict'

const RaspiCam = require('raspicam');
const five = require('johnny-five');
const AWS = require('aws-sdk');
const fs = require('fs');

const s3 = new AWS.S3();

const bucketName = process.env.AWS_BUCKET_NAME;

const imagePath = '../data/image.jpg';

const camera = new RaspiCam({
	mode: 'photo',
	output: imagePath,
	encoding: 'jpg',
	timeout: 100 // take the picture immediately
});

const board = new five.Board();

board.on('ready', () => {
	const button = new five.Button('A0');

	button.on('release', () => {
    console.log('Taking photo');
		camera.start();
	});
});


camera.on('read', (err, timestamp, filename) => {
  if(err) {
    console.error(err);
    return;
  }

	const fileStream = fs.createReadStream(imagePath);

	const params = {
		Bucket: bucketName,
		Key: `garden-aid-pi-${timestamp}.jpg`,
		Body: fileStream,
	};

	s3.upload(params, {}, function (err, data) {
    if(err) {
      console.error(err);
      return;
    }
    
		console.log('Saved file to S3', data);
	});
});