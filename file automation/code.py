def print_file_content(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                print(line.strip())  # Strip newline characters for clean printing
    except FileNotFoundError:
        print("File not found!")

file_name = 'file.txt'
print_file_content(file_name)
