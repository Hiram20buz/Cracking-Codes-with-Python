import os

current_directory = os.getcwd()

# Define the path for the new directory
folder_path = os.path.join(current_directory, "base64", "output")

# Create an empty directory if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"Directory '{folder_path}' created successfully.")
else:
    print(f"Directory '{folder_path}' already exists.")

