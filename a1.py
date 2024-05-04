from pathlib import Path

def create_file(command):
    dir_path = command[1]
    command_extention = command[2]
    file_name = command[3]
    file_path = f"{dir_path}\\{file_name}.dsu"
    print("this is file path",file_path)
    if Path(file_path).exists():
        print("file already exists")
        start()
    else:
        Path(file_path).touch()
        print(f'file created at {file_path}')
        start()

def start():
    command = input("Please Enter Command: ")
    command_list = command.split(' ')
    type = command_list[0]
    if type == 'C':
        create_file(command_list)
    elif type == 'R':
        pass
    elif type == 'D':
        pass
    else:
        print("Please Enter Correct Command")
        start()

if __name__ == "__main__":
    start()