import shutil 
from pathlib import Path

current_path = Path.cwd()
files_path = current_path / "files"
json_path = current_path / "json"

shutil.copy(
   json_path / "users.json",
   files_path / "users-copy.json"
)