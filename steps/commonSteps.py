#Refactor common methods and create commons constans
import os
import sys
import base64


def createDir(directory):
    folder_path = "/" + directory

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Directory '{folder_path}' created successfully.")
    else:
        print(f"Directory '{folder_path}' already exists.")


def delete_files_in_folder(folder_path):
    try:
        content_list = os.listdir(folder_path)

        for content in content_list:
            content_path = os.path.join(folder_path, content)
            
            if os.path.isfile(content_path):
                os.remove(content_path)
                print(f"Deleted file: {content_path}")
            else:
                print(f"Skipping directory: {content_path}")

        print(f"All files in '{folder_path}' deleted.")
    except Exception as e:
        print(f"An error occurred: {e}")


def base64Cipher(file_path,encode):
    try:
        with open(file_path, "rb") as file:
            file_content = file.read()
            if encode == True:
                content = base64.b64encode(file_content)
            else:
                content = base64.b64decode(file_content)  
            return content
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def write_data_to_file(file_path, data):
    try:
        with open(file_path, "wb") as output_file:
            output_file.write(data)
        print(f"Data content successfully written to {file_path}")
    except Exception as e:
        print(f"Error writing to file: {e}")