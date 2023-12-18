import os
import sys

script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
#print(script_directory)

# Dictionary of commands with keys
commands_dict = {
    "createDir": "poetry run python " + script_directory + "/createOutputDir.py",
    "delete": "poetry run python " + script_directory + "/deleteOutputFiles.py",
    "encode": "poetry run python " + script_directory + "/EncodeFileToBase64.py " + script_directory + "/input/file.pdf " + script_directory + "/output/file.txt",
    "decode": "poetry run python " + script_directory + "/decodeBase64ToFile.py " + script_directory + "/input/file.txt " + script_directory + "/output/file.pdf"
}

# Execute a specific command based on a key
#key = "encode" 
for key in commands_dict:
    if key in commands_dict:
        os.system(commands_dict[key])
    else:
        print(f"Invalid key '{key}'. Command not found.")


