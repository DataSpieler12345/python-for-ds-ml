from pathlib import Path


current_path = Path.cwd()
users_path = current_path / "files" / "users.txt"

if users_path.exists() and users_path.is_file():
   print("The File exists")
   
   content = users_path.read_text()
   
   new_user = input("Enter a new user info: ")
   content += f"\n{new_user}"
   
   users_path.write_text(content)
   
   print(content)