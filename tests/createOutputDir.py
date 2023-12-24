import sys
import os

current_directory = os.getcwd()
steps_path = os.path.join(current_directory, 'steps')
#print(steps_path)
sys.path.append(steps_path)

import commonSteps

# Define the path for the new directory
folder_path = commonSteps.script_directory() + "/" + sys.argv[1] + "/output"
#print(folder_path)
#print(folder_path)
commonSteps.createDir(folder_path)
