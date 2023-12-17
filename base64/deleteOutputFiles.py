import os
import sys


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


current_directory = os.getcwd()
folder_path = current_directory + "/base64/output"

delete_files_in_folder(folder_path)
