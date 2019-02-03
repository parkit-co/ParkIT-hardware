# IoT Component
## Raspberry Pi, USB Webcam, PIR Sensor, OpenALPR, OpenCV, Tesseract, Leptonica
### Bash scripts
  - for interpreting USB webcam
  - for calling OpenAPLR library and returning license plate possibilites + confidence (percentage value)
### Python Script
  - Upon movement detected by PIR Motion sensor, script takes a picture by calling Bash script
  - Picture is passed OpenALPR Bash script, with entire terminal result kept
  - first license plate (most confident guess) is truncated -- try/catch exception block used to analyze case where no license plate was detected
  - A HTTP POST request is sent to ParkIT server with following features: license (plate number), time (date of photo), and action (for our demo purposes since only one camera was in use, this was hard set to leaving -- usually will be based on which camera recorded plate)
