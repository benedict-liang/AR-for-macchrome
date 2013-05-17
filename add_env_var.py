import os
import sys
import environmentvariables_pb2

# Hardcoded values
# Must change using some sort of data representation (protobuf? json?)
def PromptForVariables(variable_set):
    # TODO: Need to check for uniqueness
    variable_set.setid = raw_input("Enter unique project name: ")
    variable_set.chromedriver_path = raw_input("Enter path to chromedriver: ")
    variable_set.url_to_watch = raw_input("Enter URL to observe: ")


# Main procedure
def main():

    env_variables = environmentvariables_pb2.EnvironmentVariables()

    # Read the existing address book.
    try:
        f = open("EnvFile", "rb")
        env_variables.ParseFromString(f.read())
        f.close()
    except IOError:
         print "Creating new EnvFile."

    # Add a variable set
    PromptForVariables(env_variables.variableset.add())

    f = open("EnvFile", "wb")
    f.write(env_variables.SerializeToString())
    f.close()

if __name__ == '__main__':
    main()
