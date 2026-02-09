filename = input("Enter the filename: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("File content:\n", content)

except FileNotFoundError:
    print("Oops! That file doesn't exist yet.")
