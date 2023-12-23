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
    "createDir": "poetry run python " + script_dir + "/createOutputDir.py",
    "delete": "poetry run python " + script_dir + "/deleteOutputFiles.py",
    "encode": "poetry run python " + script_dir + "/EncodeCaesarCipher.py " + script_dir + "/input/file.txt " + script_dir + "/output/encoded.txt",
    "decode": "poetry run python " + script_dir + "/decodeCaesarCipher.py " + script_dir + "/input/encoded.txt " + script_dir + "/output/file.txt"
}

# Execute a specific command based on a key
#key = "encode" 
for key in commands_dict:
    if key in commands_dict:
        os.system(commands_dict[key])
    else:
        print(f"Invalid key '{key}'. Command not found.")


