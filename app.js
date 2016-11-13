'use strict'

var fs = require('fs');

var AWS = require('aws-sdk');

// var RaspiCam = require('raspicam');
var Cylon = require('cylon');

// var s3 = new AWS.S3();

// var bucketName = process.env.AWS_BUCKET_NAME;

// var imagePath = '../data/image.jpg';

// var camera = new RaspiCam({
// 	mode: 'photo',
// 	output: imagePath,
// 	encoding: 'jpg',
// 	timeout: 100 // take the picture immediately
// });

Cylon.robot({
  connections: {
    raspi: { adaptor: 'raspi' },
  },

  devices: {
    button: { driver: 'button', pin: 4 },
    lcd: { driver: 'lcd' },
  },

  work: function(my) {
		// camera.start();
    my.button.on('push', function() {
      console.log("Button pushed!");
    });

    my.lcd.on('start', function(){
      my.lcd.print("Hello!");
    });
  }
}).start();

// camera.on('read', (err, timestamp, filename) => {
//   if(err) {
//     console.error(err);
//     return;
//   }

// 	var fileStream = fs.createReadStream(imagePath);

// 	var params = {
// 		Bucket: bucketName,
// 		Key: `garden-aid-pi-${timestamp}.jpg`,
// 		Body: fileStream,
// 	};

// 	s3.upload(params, {}, function (err, data) {
//     if(err) {
//       console.error(err);
//       return;
//     }

// 		console.log('Saved file to S3', data);
// 	});
// });