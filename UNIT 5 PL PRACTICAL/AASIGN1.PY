filename = input("Enter the filename: ")

try:
    file = open(filename, "r")
    content = file.read()
    print("\nFile Content:\n", content)
    file.close()

except FileNotFoundError:
    print("Error: File does not exist.")

except PermissionError:
    print("Error: Permission denied to read the file.")

except Exception as e:
    print("An unexpected error occurred:", e)