#create a function that will search the whole folder
def file_check(curf, cnt, fname):
    if (curf.container[cnt].name != fname and cnt < curf.size):
        return True
    return False
def check_arguments(required, given):
    return required == given
class File:
    def __init__(self, name, ftype):
        self.name = name
        self.ftype = ftype
        self.file_info = ""
    def rename(self, new_name):
        self.name = new_name
    def view_file(self):
        return self.file_info
    def add_info(self, other):
        self.file_info += other
    def overwrite_info(self, other):
        self.file_info = other
class Folder:
    def __init__(self, name, parent_folder="home"):
        self.parent_folder = parent_folder
        self.name = name
        self.size = 0
        self.ftype = "folder"
        self.container = []
    def rename(self, new_name):
        self.name = new_name
    def add_file(self, file):
        self.container.append(file);
        self.size+=1;
    def add_folder(self, folder):
        self.container.append(folder)
        self.size+=1;
    def remove_f(self, pos):
        self.container.pop(pos)
print ("HASY MANDELA TERMINAL REMAKE")
print ("© CREATIVE COMMON LICENSE")
print ()
root_folder = Folder("home")
desktop_folder = Folder("Desktop", root_folder)
c_folder = Folder("C", root_folder)
d_folder = Folder("D", root_folder)
root_folder.add_folder(desktop_folder);
root_folder.add_folder(c_folder);
root_folder.add_folder(d_folder);
current_folder = root_folder
path = ["home"]
def rename(current_name, new_name):
    global current_folder
    count = 0
    while (file_check(current_folder, count, current_name)): count+=1
    if (count == current_folder.size): print(f"The folder/file with the name {new_name} is not found")
    else: current_folder.container[count].rename(new_name)
def change_directory(dir):
    global current_folder
    if (dir == ".."): 
        if (current_folder != root_folder):
            current_folder = current_folder.parent_folder
            path.pop()
    else:
        count = 0
        while (file_check(current_folder, count, dir) or current_folder.container[count].ftype != "folder"): count+=1;
        if (count == current_folder.size): print(f"The folder with the name {dir} is not found")
        else: 
            current_folder = current_folder.container[count]
            path.append(current_folder.name)
def addf(finfo):
    f_spl = finfo.split(".")
    if (len(f_spl) == 1):
        F = Folder(f_spl[0], current_folder)
        current_folder.add_folder(F);
    else:
        F = File(f_spl[0], f_spl[1])
        current_folder.add_folder(F);
def removef(name):
    count = 0
    while (file_check(current_folder, count, name)): count+=1
    if (count == current_folder.size): print(f"The folder/file with the name {name} is not found")
    else: current_folder.remove_f(count)
def flist():
    whitespace = 25
    for f in current_folder.container:
        string = "  "
        string += f.name
        avail_whitespace = whitespace-len(f.name)
        while (avail_whitespace > 0):
            string += " "
            avail_whitespace -= 1
        string += f.ftype
        print(string)
def path_view():
    string = ""
    for i in path:
        string += i
        string +="/"
    print("PATH")
    print("____")
    print(string[0:-1])
def cat_file(name):
    count = 0
    while (file_check(current_folder, count, name) or current_folder.container[count].ftype == "folder"): count+=1
    if (count == current_folder.size): print(f"The folder/file with the name {name} is not found")
    else: print(current_folder.container[count].view_file())
def overwriteinfo(name, info):
    count = 0
    while (file_check(current_folder, count, name) or current_folder.container[count].ftype == "folder"): count+=1
    if (count == current_folder.size): print(f"The folder/file with the name {name} is not found")
    else: current_folder.container[count].overwrite_info(info)
def addinfo(name, info):
    count = 0
    while (file_check(current_folder, count, name) or current_folder.container[count].ftype == "folder"): count+=1
    if (count == current_folder.size): print(f"The folder/file with the name {name} is not found")
    else: current_folder.container[count].add_info(info)
while (True):
    string = ""
    for i in path:
        string += i
        string += "/"
    inp = input(f"{string[0:-1]}> ")
    input_split = inp.split()
    command = input_split[0]
    if (command == "rename" and check_arguments(2, len(input_split)-1)): rename(input_split[1], input_split[2])
    elif (command == "cd" and check_arguments(1, len(input_split)-1)): change_directory(input_split[1])
    elif (command == "add" and check_arguments(1, len(input_split)-1)): addf(input_split[1])
    elif (command == "ls" and check_arguments(0, len(input_split)-1)): flist()
    elif (command == "pwd" and check_arguments(0, len(input_split)-1)): path_view()
    elif (command == "rm" and check_arguments(1, len(input_split)-1)): removef(input_split[1])
    elif (command == "cat" and check_arguments(1, len(input_split)-1)): cat_file(input_split[1])
    elif (command == "addinfo" and check_arguments(2, len(input_split)-1)): addinfo(input_split[1], input_split[2])
    elif (command == "overwriteinfo" and check_arguments(2, len(input_split)-1)): overwriteinfo(input_split[1], input_split[2])
    elif (command == "quit" or command == "exit" and check_arguments(0, len(input_split)-1)): break
    else: print(f"The command {command} is either invalid or has the incorrect amount of parameters given")
