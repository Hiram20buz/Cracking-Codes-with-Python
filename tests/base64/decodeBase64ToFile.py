import base64
import sys
import os

current_directory = os.getcwd()
steps_path = os.path.join(current_directory, 'steps')
print(steps_path)
sys.path.append(steps_path)

import commonSteps


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input_file output_file")
    else:
        input_file_path = sys.argv[1]
        output_file_path = sys.argv[2]
        
        decoded_data = commonSteps.decode_base64_to_file(input_file_path)
        
        if decoded_data:
            commonSteps.write_data_to_file(output_file_path, decoded_data)
