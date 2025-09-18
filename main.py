import time

timestmps = False

def chat(mes):
    global timestmps
    if mes == "!exit":
        return 1
    elif mes == "!tm-true":
        timestmps = True
        print("> Time stamps activated")
        return 0
    elif mes == "!tm-false":
        timestmps = False
        print("> Time stamps deactivated")
    else:
        print(f"[{time.ctime()}][User] {mes}  \n" if timestmps else print(f"[User] {mes} \n"))
            

while True:
    if chat(mes=input("Chat > ")) == 1:
        print("Program has ended")
        quit()
    