import sys
import os

current_directory = os.getcwd()
steps_path = os.path.join(current_directory, 'steps')
print(steps_path)
sys.path.append(steps_path)

import commonSteps


folder_path = commonSteps.script_directory() + "/output"

commonSteps.delete_files_in_folder(folder_path)
