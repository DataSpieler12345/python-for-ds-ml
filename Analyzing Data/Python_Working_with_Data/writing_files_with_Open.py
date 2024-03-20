
from asyncore import write
from distutils.file_util import write_file


# Write line to file

ejemplo2 = "Example3.txt"
with open(ejemplo2, "w") as escritura: # comprobamos si se han agregado las 3 lineas al Example3.txt
    escritura.write("This is line A\n ")
    escritura.write("This is line B\n ")
    escritura.write("This is line C\n ")
    print(escritura)


  
  
    
    
    