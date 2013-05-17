import os
import sys
import environmentvariables_pb2

# Hardcoded values
# Must change using some sort of data representation (protobuf? json?)

# Main procedure
def main():
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

if __name__ == '__main__':
    main()
