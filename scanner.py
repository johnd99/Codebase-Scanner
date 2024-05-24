import os
import sys


def scan_directory(input_directory, mode, skip_dir, selected_directories, skip_files, selected_files, total_depth):
    
    # This list can be extended
    file_extensions = ('.txt', '.md', '.py', '.js', '.html', '.css', '.scss', '.java', '.cpp', '.c', '.h', 
                       '.php', '.rb', '.cs', '.swift', '.go', '.rs', '.ts', '.tsx', '.scala', '.lua', '.pl', 
                       '.sh', '.bat', '.ps1', '.json')

    file_count = 0

    def has_match(path, my_set):
        names = path.split('\\')
        for name in names:
            if name in my_set:
                return True
        return False

    
    def read_files_recursive(directory, cur_depth):      # Note: This can take a while to run for very large amounts of text
        nonlocal file_count
        if cur_depth <= total_depth:
            for entry in os.scandir(directory):
                if entry.is_dir() and not entry.name.startswith('.'):
                   if not (skip_dir and entry.name in selected_directories):
                        read_files_recursive(entry.path, cur_depth + 1)
                elif entry.is_file() and entry.name.endswith(file_extensions):
                    if skip_dir or has_match(entry.path, selected_directories):
                        if skip_files != (entry.name in selected_files):          # Can't have both be true or both be false
                            try:
                                with open(entry.path, 'r', encoding='utf-8') as f:
                                    content = f.read()
                                    absolute_path = os.path.abspath(entry.path)
                                    outf.write(f'--- CONTENT OF {absolute_path} ---\n\n{content}\n\n\n\n')
                                    file_count += 1
                            except UnicodeDecodeError as e:
                                print(f"Skipping file due to encoding issue: {entry.path}. Error: {e}")
                            except IOError as e:
                                print(f"Skipping inaccessible file: {entry.path}. Error: {e}")
    

    def read_directory_structure_recursive(directory, cur_depth, indentation):
        nonlocal file_count
        if cur_depth <= total_depth:
            for entry in os.scandir(directory):
                if entry.is_dir() and not entry.name.startswith('.'):
                   if not (skip_dir and entry.name in selected_directories):
                        line = indentation + entry.name + '\n'
                        outf.write(line)
                        read_directory_structure_recursive(entry.path, cur_depth + 1, indentation + "    ")   
                elif entry.is_file() and entry.name.endswith(file_extensions):
                    if skip_dir or has_match(entry.path, selected_directories):
                        if skip_files != (entry.name in selected_files):            # Can't have both be true or both be false
                            line = indentation + entry.name + '\n'
                            outf.write(line)
                            file_count += 1

    if mode == 'fc':
        with open('code.txt', 'w', encoding='utf-8') as outf:
            read_files_recursive(input_directory, 1)
    else:
        with open('directory_structure.txt', 'w', encoding='utf-8') as outf:
            read_directory_structure_recursive(input_directory, 1, "")
    
    result = str(file_count) + " files"
    print(result)



def main():
    num_args = len(sys.argv)
    if not (num_args == 5 or num_args == 6):
        print("Script needs 5-6 arguments")
        sys.exit(1)
    
    input_directory = sys.argv[1]  # Codebase to scan
    
    mode = sys.argv[2]
    if not (mode == 'fc' or mode == 'ds'):  # 'File contents' or 'directory structure'
        print("Invaid mode")
        sys.exit(1)
    
    skip_dir = True
    selected_directories = set()
    if sys.argv[3] == "None":     # Don't skip over any directories
        pass
    elif sys.argv[3][0] == '+':
        skip_dir = False
        selected_directories.update(sys.argv[3][1:].split(','))  # Include files within these directories, skip everything else
    else:
        selected_directories.update(sys.argv[3].split(','))   # Skip files within these directories

    skip_files = True
    selected_files = set()
    if sys.argv[4] == "None":      # Don't skip over any files
        pass
    elif sys.argv[4][0] == '+':
        skip_files = False
        selected_files.update(sys.argv[4][1:].split(','))   # Include these files, skip everything else
    else:
        selected_files.update(sys.argv[4].split(','))    # Skip these files

    depth = float('inf')      # Indicates the max recursion depth, optional argument
    if num_args == 6:
        if sys.argv[5].isdigit():
            depth = int(sys.argv[5])
        else:
            print("Invalid depth")
            sys.exit(1)

    scan_directory(input_directory, mode, skip_dir, selected_directories, skip_files, selected_files, depth)


if __name__ == '__main__':
    main()


