# directory management
from pathlib import Path

#Methods and Classes
# cwd
# home  
# ls

current_path = Path.cwd('E:/PYTHON DS & ML BILDUNG/Python File Management') # working directory
print(current_path) # it show the path

home_path = Path.home()
print(home_path)