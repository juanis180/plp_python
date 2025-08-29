# Ask the user for a filename
filename = input("Enter the filename you want to read: ")

try:
    # Try to open and read the file
    with open(filename, "r") as infile:
        content = infile.read()

    # Modify the content (example: convert to uppercase)
    modified_content = content.upper()

    # Create a new output file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as outfile:
        outfile.write(modified_content)

    print(f"Success! The modified content has been saved in '{new_filename}'")

except FileNotFoundError:
    print("Error: The file does not exist. Please check the filename and try again.")
except PermissionError:
    print("Error: You don’t have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
