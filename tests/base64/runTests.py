import os
import sys

current_directory = os.getcwd()
steps_path = os.path.join(current_directory, 'steps')
#print(steps_path)
sys.path.append(steps_path)

import commonSteps


script_dir = commonSteps.script_directory()
#print(script_directory)
# Dictionary of commands with keys
commands_dict = {
    "createDir": "poetry run python tests/createOutputDir.py base64",
    "delete": "poetry run python tests/deleteOutputFiles.py base64",
    "encode": "poetry run python " + script_dir + "/EncodeFileToBase64.py " + script_dir + "/input/file.pdf " + script_dir + "/output/file.txt",
    "decode": "poetry run python " + script_dir + "/decodeBase64ToFile.py " + script_dir + "/input/file.txt " + script_dir + "/output/file.pdf"
}

# Execute a specific command based on a key
#key = "encode" 
for key in commands_dict:
    if key in commands_dict:
        os.system(commands_dict[key])
    else:
        print(f"Invalid key '{key}'. Command not found.")


