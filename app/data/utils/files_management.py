# Functions
def generate_file(p_name:str, p_extension:str, p_info:str):
    file = open(p_name + p_extension, 'w', encoding="utf-8")
    file.write(p_info)

def read_file(p_name:str, p_extension:str):
    file = open(p_name + p_extension, 'r', encoding="utf-8")
    return file.read()