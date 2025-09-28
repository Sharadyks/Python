import os

def createfile(filename):
    try:
        with open(filename,"x") as f:
            print(f"File Name {filename} created successfully")
    except FileExistsError:
        print(f"File name {filename} already exist")
    except Exception as E:
        print("An error occured")

def view_all_files():
    files = os.listdir()
    if not files:
        print("No file found")
    else:
        print("Files in directory!")
        for file in files:
            print(file)

def deleteFile(filename):
    try:
        os.remove(filename)
        print(f"File name {filename} has been deleted successfully!")
    except FileNotFoundError:
        print("File not found")
    except Exception as E:
        print("An error occured")

def readFile(filename):
    try:
        with open("sample.txt","r") as f:
            content = f.read()
            print(f"Content of {filename} : \n{content}")
    except FileNotFoundError:
        print("File doesn't exist")
    except Exception as E:
        print("An error occured")

def editFile(filename):
    try:
        with open("sample.txt","a") as f:
            content = input("Enter data to add: ")
            f.write(content + "\n")
            print(f"Content added to {filename} Successfully"))
    except FileNotFoundError:
        print("File doesn't exist")
    except Exception as e:
         print("An error occured")