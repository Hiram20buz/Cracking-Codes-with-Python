import sys
import os
import time

current_directory = os.getcwd()
steps_path = os.path.join(current_directory, 'steps')
#print(steps_path)
sys.path.append(steps_path)

import detectEnglish


print(detectEnglish.isEnglish('Is this sentence English text?'))