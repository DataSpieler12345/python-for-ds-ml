from pathlib import Path


current_path = Path.cwd()
files_path = current_path / "files"

def show_txt_files(path):
   
   for dir in path.iterdir():
      if dir.is_dir():
         show_txt_files(dir)
      else:
         
         if dir.suffix == '.txt':
            print(dir.name)
         

if(files_path.exists()):
   
   show_txt_files(files_path)