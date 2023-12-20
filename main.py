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
    "base64": "poetry run python tests/base64/runTests.py",
    "cipher": "poetry run python tests/cipher/runTests.py"
}

# Execute a specific command based on a key
#key = "encode" 
for key in commands_dict:
    if key in commands_dict:
        os.system(commands_dict[key])
    else:
        print(f"Invalid key '{key}'. Command not found.")