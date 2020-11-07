# Project Description 
The purpose of this project is to instruct the Adafruit Matrix Portal to pull a json response from a simple flask application. The Flask app parses the quote_color file where the first line should be the text you want displayed on the matrix and the second line should be the desired color. You can change this file by SSH'ing it from any device that has SSH access to the Flask server. 

# Project Layout
## MatrixFiles Directory
This contains the code, lib folder, and CircuitPython files needed to run this project. These files are included because version changes happen frequently. As long as you use these files with this project everything should work. 

## Root Directory
Contains files needed to run the Python Flask server. 

# Instructions
## Matrix Portal
1. Install the adafruit-circuitpython .u2f using Adafruit's Matrix Portal instructions 
2. Update the secrets.py with your SSID and SSID Password
3. Update the code.py's JSON_URL variable with your Flask Sever's URL 
4. Copy unzip the lib folder
5. Copy the code.py, secrets.py, and lib folder into the root directory of the Matrix Portal

## Flask 
1. Perform a git clone on the server needing to run the flask app
2. Install the depedencies using the requirements text and pip 
3. Update the quote_color file with initial text you want displayed
4. Install openssh server on the intended flask server
5. Create username/password or ssh keys to the server so you can remotely update the quote color file when needed
6. Run the flask application 
7. Turn on the Portal