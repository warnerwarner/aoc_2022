#%% 
import numpy as np

#%%

# %%
class Directory():
    
    def __init__(self, name, parent):
        self.name = name
        self.init_size = 0
        self.full_size = 0
        self.parent = parent
        self.children = []
    
    def explore_children(self, contents):
        for line in contents:
            if 'dir' in line:
                new_dir = Directory(line.split(' ')[1], self)
                self.children.append(new_dir)
            else:
                self.children.append(line.split(' ')[1])
                self.init_size += int(line.split(' ')[0])
                self.full_size += int(line.split(' ')[0])

    def find_child_directory(self, dir_name):
        for dir in self.children:
            if isinstance(dir, Directory):
                if dir.name == dir_name:
                    return dir
        return 'Ooops'

    def find_full_size(self):
        self.full_size = self.find_full_size_(self.children)
    
    def find_full_size_(self, children):
        size = 0
        for child in children:
            if isinstance(child, Directory):
                size += self.find_full_size_(child.children)
                size += child.init_size
        return size


def read_contents(data):
    current_line = ' '
    contents = []

    while '$' not in current_line and len(current_line) > 0:
        prev_pos = data.tell()
        current_line = data.readline()
        contents.append(current_line[:-1])
    data.seek(prev_pos)
    return contents[:-1]

def get_all_children(directory):
    dirs = []
    
    for child in directory.children:
        if isinstance(child, Directory):
            child_dirs = get_all_children(child)
            print(child)
            dirs.append(child)
            [dirs.append(i) for i in child_dirs]
    return dirs


# %%
print(data[:10])
# %%

# %%
data = open('Day7_input.txt', 'r')
line = data.readline()
home_dir = Directory('/', None)

current_dir = home_dir
dirs = []
while line:
    line = data.readline()[:-1]
    if line == '$ ls':
        contents = read_contents(data)
        current_dir.explore_children(contents)
    elif '$ cd' in line:
        # print(line)
        # print(current_dir.name)
        dir_name = line.split(' ')[-1]
        if dir_name == '..':
            new_dir = current_dir.parent
        else:
            new_dir = current_dir.find_child_directory(dir_name)
        current_dir = new_dir
    print(line)
    






# %%
current_dir.find_full_size()
print(current_dir.name)
print(current_dir.full_size)
print(current_dir.init_size)
parent = current_dir.parent
parent.find_full_size()
print(parent.init_size)
print(parent.full_size)
# %%
print(isinstance(home_dir, Directory))

# %%
all_dirs = get_all_children(home_dir)
# %%
tot_size = 0
for dir in all_dirs:
    if dir.full_size <= 100000:
        tot_size += dir.full_size
print(tot_size)
# %%
dir_names = [i.name for i in all_dirs]
sizes = [i.full_size for i in all_dirs]
print(len(np.unique(dir_names)))
print(len(np.unique(sizes)))
# %%
