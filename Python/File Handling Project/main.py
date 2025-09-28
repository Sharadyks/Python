from pathlib import Path

def readFileAndFolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i,item in enumerate(items):
        print(f"{i+1} : {item} ")

def createfile():
    try:
        readFileAndFolder()
        name = input("Enter your name of file:- ")
        p = Path(name)
        with open(p,"w") as fs:
            data = input("What do you want to write:- ")
            fs.write(data)
            print("File created succesfully")
    except Exception as e:
        print(f"Excetion occured as {e}")
    

print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deletion a file")

check = int(input("Please tell me your response: "))
if check ==1:
    createfile()