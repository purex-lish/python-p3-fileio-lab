def write_file(file_name, file_content):
    file_txt=f"{file_name}.txt"
    with open(file_txt,mode='w',encoding="utf-8") as new_file:
       new_file.write(file_content)


def append_file(file_name, append_content):
    file_txt=f"{file_name}.txt"
    with open(file_txt,mode='a',encoding="utf-8") as new_file:
       new_file.write(append_content)

def read_file(file_name):
    file_txt=f"{file_name}.txt"
    with open(file_txt,encoding="utf-8") as file_name:
       text=file_name.read()
       return text
