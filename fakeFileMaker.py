from os.path import getsize
from os import listdir
from time import sleep

print('''
 _____     _        _____ _ _      __  __       _             
|  ___|_ _| | _____|  ___(_) | ___|  \/  | __ _| | _____ _ __ 
| |_ / _` | |/ / _ \ |_  | | |/ _ \ |\/| |/ _` | |/ / _ \ '__|
|  _| (_| |   <  __/  _| | | |  __/ |  | | (_| |   <  __/ |   
|_|  \__,_|_|\_\___|_|   |_|_|\___|_|  |_|\__,_|_|\_\___|_|   
                                                            
''')

file_name = input("Enter Fullname of file: ")
mod = input("Enter mode (MG, KB): ")
hajm = float(input("Enter size as mg: "))

if not file_name in listdir('./'):
    with open(file_name, 'wb') as file:
        file.close()
else:
    print("file exists.")
    exit(0)

size = getsize(file_name)
with open(file_name, 'r+b') as file:
    # file.write(b'A'*int(hajm*1000*1000))
    if mod.upper() == 'MG':
    	file.write(b'A'*int(hajm*1000*1000))
    	file.close()
    elif mod.upper() == 'KB':
    	file.write(b'A'*int(hajm*1000))
    	file.close()
    
size = getsize(file_name)

print(f"-------------\nSuccesfully Created :)\nname: {file_name}\nsize: {hajm}")
