import os
import sys

# Hardcoded values
# Must change using some sort of data representation (protobuf? json?)

# Main procedure
is_valid = False

while not is_valid:
    chromedriver_path = raw_input("Enter path to chromedriver: ")
    url_input = raw_input("Enter URL to observe: ")

    if chromedriver_path and url_input:
        is_valid = True

f = open("EnvFile", "wb")
f.write(chromedriver_path + "\n")
f.write(url_input)
f.close()
