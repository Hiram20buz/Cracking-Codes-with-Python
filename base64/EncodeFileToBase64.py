import base64
import sys

def encode_file_to_base64(file_path):
    try:
        with open(file_path, "rb") as file:
            file_content = file.read()
            encoded_content = base64.b64encode(file_content)
            return encoded_content
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def write_encoded_data_to_file(file_path, encoded_data):
    try:
        with open(file_path, "wb") as output_file:
            output_file.write(encoded_data)
        print(f"Encoded content successfully written to {file_path}")
    except Exception as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input_file output_file")
    else:
        input_file_path = sys.argv[1]
        output_file_path = sys.argv[2]
        
        encoded_data = encode_file_to_base64(input_file_path)
        
        if encoded_data:
            write_encoded_data_to_file(output_file_path, encoded_data)

