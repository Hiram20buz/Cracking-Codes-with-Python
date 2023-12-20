#Refactor common methods and create commons constans
import os
import sys
import base64
import reverse


def createDir(directory: str):
    folder_path = "/" + directory

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Directory '{folder_path}' created successfully.")
    else:
        print(f"Directory '{folder_path}' already exists.")


def delete_files_in_folder(folder_path: str):
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


def base64Cipher(file_path: str,encode: bool) -> str:
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


def write_data_to_file(file_path: str, data: str):
    try:
        with open(file_path, "wb") as output_file:
            output_file.write(data)
        print(f"Data content successfully written to {file_path}")
    except Exception as e:
        print(f"Error writing to file: {e}")


def script_directory() -> str:
    return os.path.dirname(os.path.abspath(sys.argv[0]))


def reverseCipher(input_file_name: str, output_file_name: str):
    try:
        with open(input_file_name, 'r') as input_file, open(output_file_name, 'w') as output_file:
            for line in input_file:
                encrypted_line = reverse.cipher(line.strip())  # Assuming you want to strip newline characters
                output_file.write(encrypted_line + '\n')  # Write encrypted line to output file

        print("Encryption successful. Check", output_file_name)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)