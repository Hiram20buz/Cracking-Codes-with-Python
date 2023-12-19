import sys
import os

current_directory = os.getcwd()
steps_path = os.path.join(current_directory, 'steps')
print(steps_path)
sys.path.append(steps_path)

import commonSteps

script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))

# Define the path for the new directory
folder_path = script_directory + "/output"

commonSteps.createDir(folder_path)
