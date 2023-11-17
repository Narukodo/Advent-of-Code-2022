# each node only has 1 parent, but can have multiple children
# each node: [size, parent, [children]]
# two commands: cd and ls

# if command = cd and directory != .. : create new node
# if command = cd and directory == .. : move to parent
# if command = ls, then for the next lines while '$' does not exist at the beginning of the command: add child node

class FileSystem:
    def __init__(self, root):
        self.root = root
        self.node_stack = [root]

    def calculate_sizes(self, current_node):
        if isinstance(current_node, LeafFile):
            return current_node.size
        else:
            for child in current_node.children:
                current_node.increase_size(self.calculate_sizes(child))
            return current_node.size
    
    def add_directory(self, directory_name):
        current_node = self.where_am_i()
        new_directory = Directory(directory_name, current_node, [])
        current_node.add_child(new_directory)
    
    def add_file(self, file_name, file_size):
        current_node = self.where_am_i()
        new_file = LeafFile(file_name, current_node, file_size)
        current_node.add_child(new_file)
    
    def go_to_child(self, child_name):
        current_node = self.where_am_i()
        for child in current_node.children:
            if child.name == child_name:
                self.node_stack.append(child)
                return
    
    def go_to_parent(self):
        self.node_stack.pop()
    
    # clear stack
    def go_to_root(self):
        self.node_stack = [self.node_stack[0]]
    
    def where_am_i(self):
        return self.node_stack[-1]
    
    def __str__(self):
        return str(self.root)

class Directory:
    def __init__(self, name, parent, children=[]):
        self.name = name
        self.parent = parent
        self.size = 0
        self.children = children
    
    def add_child(self, child):
        self.children.append(child)
    
    def update_size(self, size):
        self.size = size
    
    def increase_size(self, size):
        self.size += size
    
    def decrease_size(self, size):
        self.size -= size

    def __str__(self):
        new_string = f'- {self.name} (dir)\n'
        for child in self.children:
            new_string += f'  {str(child)}\n'
        return new_string
    
class LeafFile:
    def __init__(self, name, parent, size):
        self.name = name
        self.size = size
        self.parent = parent
    
    def __str__(self):
        return f'- {self.name} (file, size={self.size})'

def update_sizes(sizes_dictionary, directories, size):
    path = ''
    for directory in directories:
        path = f'{path}*{directory}'
        if path in sizes_dictionary:
            sizes_dictionary[path] += size
        else:
            sizes_dictionary[path] = size

with open('day7_input.txt') as f:
    directives = f.read().splitlines()
    NUM_DIRECTIVES = len(directives)
    MAX_SIZE = 100000
    TOTAL_DISK_SPACE = 70000000
    REQUIRED_UPDATE_SPACE = 30000000

    directory_stack = []
    current_index = 0
    sizes = dict()

    sum_directories = 0
    while current_index < NUM_DIRECTIVES:
        current_directive = directives[current_index].split(' ')
        if current_directive[0] == '$':
            if current_directive[1] == 'cd':
                if current_directive[2] == '/':
                    directory_stack = ['/']
                elif current_directive[2] == '..':
                    directory_stack.pop()
                else:
                    directory_stack.append(current_directive[2])
            else:
                while current_index + 1 < NUM_DIRECTIVES and directives[current_index + 1][0] != '$':
                    current_index += 1
                    current_directive = directives[current_index].split(' ')
                    if current_directive[0] != 'dir':
                        update_sizes(sizes, directory_stack, int(current_directive[0]))
        current_index += 1

    for directory in sizes:
        if sizes[directory] <= MAX_SIZE:
            sum_directories += sizes[directory]
    print(sum_directories)

    remaining_space = REQUIRED_UPDATE_SPACE - (TOTAL_DISK_SPACE - sizes['*/'])
    smallest_sufficient_delete = TOTAL_DISK_SPACE
    for path in sizes:
        if sizes[path] >= remaining_space and sizes[path] < smallest_sufficient_delete:
            smallest_sufficient_delete = sizes[path]
    print(smallest_sufficient_delete)
        
    # file_system = None
    # current_directive_index = 0
    # num_of_directives = len(directives)
    # while current_directive_index < num_of_directives:
    #     current_directive = directives[current_directive_index]
    #     if 'cd' in current_directive:
    #         directory_name = current_directive[5:]
    #         if '..' not in current_directive:
    #             if file_system == None:
    #                 file_system = FileSystem(current_directive[5:])
    #             else:
    #                 file_system.go_to_child(current_directive[5:])
    #     elif 'ls' in current_directive:
    #         while current_directive_index + 1 < num_of_directives and directives[current_directive_index + 1][0] != '$':
    #             current_directive = directives[current_directive_index + 1]
    #             if current_directive[:3] == 'dir':
    #                 child_directory = Directory(name=current_directive[4:], parent=file_system.where_am_i().name)
    #                 file_system.add_directory(child_directory)
    #             else:
    #                 file_info = current_directive.split(' ')
    #                 child_file = LeafFile(name=file_info[1], size=int(file_info[0]))
    #                 file_system.add_file(child_file)
    #             current_directive_index += 1
    #     current_directive_index += 1

                

