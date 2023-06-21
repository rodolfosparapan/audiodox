
def get_string_array_from_file(file_path):

    with open(file_path, "r") as file:
        content = file.readlines()

    string_array = [line.strip() for line in content]
    return string_array
    
