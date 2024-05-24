This Python script allows you to send the contents of multiple code files to AI models like ChatGPT or Claude for analysis more quickly than manual copy/pasting each one. 

It combines the relevant files into a single text file on your machine that can then be uploaded manually to ChatGPT or a different AI, or even used for a different purpose entirely.

(Or it can instead read the directory structure of the specified project and put that structure into a text file)



Here are some examples of running the script:


python scanner.py ‘../Documents/my_project’ fc None None

^Scans each of the files in “my_project”, including ones in subdirectories, and writes everything into a text file (called “code.txt”)
which can then be sent to ChatGPT


 
python scanner.py ‘../Documents/my_project’ ds None None

^Scans the directory structure of “my_project” and writes that directory structure into a text file (called “directory_structure.txt”)


 
python scanner.py '../Git Repositories/excalidraw' fc None LanguageList.tsx,index.html

^Scans the files in “excalidraw” but excludes files named "LanguageList.tsx" and “index.html”


 
python scanner.py '../Git Repositories/excalidraw' fc +excalidraw-app,packages None

^Scans “excalidraw” but only reads files within the subdirectories named “excalidraw-app” and “packages”

 


This is what each argument means:

Argument 0: File name of this script

Argument 1: Path of the project directory to focus on

Argument 2: ‘fc’ if you want the file contents to be written to “code.txt”, or ‘ds’ if you want the directory structure to be written to “directory_structure.txt”

Argument 3: Comma-separated list of subdirectories within the main directory that you want to exclude from the output.  
            Or, if you instead want to focus solely on these directories and exclude everything else, put ‘+’ at the beginning of the list.  
            Or, just put “None” to skip over this argument.

Argument 4: Same as argument 3, but for files instead of subdirectories

Argument 5: Optional argument specifying the maximum recursion depth
