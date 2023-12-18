import os
import sys

script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))

# Define the path for the new directory
folder_path = script_directory + "/output"

# Create an empty directory if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"Directory '{folder_path}' created successfully.")
else:
    print(f"Directory '{folder_path}' already exists.")

