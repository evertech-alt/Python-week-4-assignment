filename = input("Enter the file name: ")

try:
    with open(filename, "r") as file:
        data = file.read()

    new_filename = "modified_" + filename
    
    with open(new_filename,"w") as new_file:
        new_file.write(data)
        new_file.write("===Modified version of your file===")
        
    print(f"The modified file has been created and saved as {new_filename}")

except FileNotFoundError:
    print("Error:File not found")

except PermissionError:
    print("Error:You do not have permission to read this file")