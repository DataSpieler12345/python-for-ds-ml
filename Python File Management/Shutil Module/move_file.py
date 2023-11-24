import shutil 
from pathlib import Path

current_path = Path.cwd()
files_path = current_path / "files"
json_path = current_path / "json"

for dir in files_path.iterdir():
   
   if dir.is_file() and dir.suffix == '.json':
      
      shutil.move(
         dir, #original directory
         json_path / dir.name #destiny directory
              
      )
      