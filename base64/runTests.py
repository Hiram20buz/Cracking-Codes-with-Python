import os

# Dictionary of commands with keys
commands_dict = {
    "delete": "poetry run python base64/deleteOutputFiles.py",
    "encode": "poetry run python base64/EncodeFileToBase64.py base64/input/file.pdf base64/output/file.txt",
    "decode": "poetry run python base64/decodeBase64ToFile.py base64/input/file.txt base64/output/file.pdf"
}

# Execute a specific command based on a key
#key = "encode" 
for key in commands_dict:
    if key in commands_dict:
        os.system(commands_dict[key])
    else:
        print(f"Invalid key '{key}'. Command not found.")


