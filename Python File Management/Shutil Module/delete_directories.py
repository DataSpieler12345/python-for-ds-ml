import shutil 
from pathlib import Path

current_path = Path.cwd()
files_path = current_path / "files"
json_path = current_path / "json"

# shutil.rmtree(json_path) # delete directory

users_copy_path = files_path / "testuser.json" #delete a file

if users_copy_path.is_file():
   users_copy_path.unlink() # file or link
