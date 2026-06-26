from pathlib import Path
import os

def showexistingthings():
    path = Path('')
    items = list(path.rglob('*'))
    for i , items in enumerate(items):
        print(f"{i+1} : {items}")

def create_file():
    try:
        showexistingthings()
        name = input("Give Name To Your File :- ")
        p = Path(name)
        if not p.exists() and p.is_file:
            with open(p,"a") as f:
                data = input("Write whatever you want to Insert In The File :- ")
                f.write(data)
            print("FILE CRAETED SUCCESSFULLY")
        else:
            print(f"There Is Already A File Exists Named {name}")
    except Exception as err:
        print(f"Sorry ! An Error Occured As {err}")
    
def read_file() :
    try :
        showexistingthings()
        file_name = input("Enter The File Name :- ")
        p = Path(file_name)
        if p.exists and p.is_file :
            with open(file_name,"r") as f:
                data = f.read()
                print(data)
                print(f"{file_name} : File Readed Successfully")
        else :
            print("File Does not Exists")
    except Exception as err:
        print(f"An Error Occured As {err}")

def update_file() :
    try:
        showexistingthings()
        file_name = input("Enter The Name Of The File You Wanna Update :- ")
        p = Path(file_name)
        if p.exists and p.is_file :
            print("Place 1 for Rename a file")
            print("Place 2 for overwrite a file")
            print("Place 3 for Appending some data a file")
            res = int(input("Give your Resonse :- "))
            if res == 1:
                name2 = input("Enter the Alternative Name For the File :- ")
                p2 = Path(name2)
                p.rename(p2)
            if res == 2:
                with open(p,"w") as f:
                    data = input("Enter the new data :- ")
                    f.write(data)
            if res == 3:
                with open(p,"a") as f:
                    data = input("Enter the new data :- ")
                    f.write(" " + data)
            print(f"{file_name} : The File Is Successfully Updated")
        else :
            print("The File Does not Exists At All")
    except Exception as err:
        print(f"An Exception Occured As {err}")

def delete_file() :
    try:
        showexistingthings()
        name = input("Enter the File Name You Wanna Delete :- ")
        p = Path(name)
        if p.exists and p.is_file:
            os.remove(name)
            print(f"{name} : File Removed Succesfully")
        else :
            print("The File Does Not Exists")
    except Exception as err:
        print(f"A Error Occured As {err}")

print("Place 1 for creating a file")
print("Place 2 for reading a file")
print("Place 3 for updating a file")
print("Place 4 for delition a file")
response = int(input("Enter You Response : "))

if response == 1 :
    create_file()

if response == 2 :
    read_file()

if response == 3 :
    update_file()

if response == 4 :
    delete_file()