import base64
import sys

def decode_base64_to_file(file_path):
    try:
        with open(file_path, "rb") as file:
            file_content = file.read()
            decoded_content = base64.b64decode(file_content)
            return decoded_content
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def write_decoded_data_to_file(file_path, decoded_data):
    try:
        with open(file_path, "wb") as output_file:
            output_file.write(decoded_data)
        print(f"Encoded content successfully written to {file_path}")
    except Exception as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input_file output_file")
    else:
        input_file_path = sys.argv[1]
        output_file_path = sys.argv[2]
        
        decoded_data = decode_base64_to_file(input_file_path)
        
        if decoded_data:
            write_decoded_data_to_file(output_file_path, decoded_data)
