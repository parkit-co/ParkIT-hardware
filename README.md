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

### OpenALPR & Raspberry Pi
  - Raspberry Pi does not have a X86, AMD64 or X86_64 processor so OpenALPR had to be built from it's source code to fit the Raspberry Pi architechture, compiling all indiviual dependencies 
  
 ### Future Steps
  - Optimize the application: with the usage of two bash scripts being called, there is some lag in analyzing pictures. This can be done through: -using Cloud Api for OpenALPR - fixing Python bindings for OpenALPR library 
