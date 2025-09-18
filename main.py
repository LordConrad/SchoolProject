import time

def chat(mes):
    global timestmps
    if mes == "!exit":
        return 1
    elif mes == "tm-true":
        timestmps = True
    else:
        if timestmps:
            print(f"[{time.localtime()}][User] {mes} \n")
        else:
            timestmps = False
            
while True:
    if chat(mes=input("Chat > ")) == 1:
        print("Program has ended")
        break
while True:
    if chat(mes=input("Chat > ")) == 1:
        print("Program has ended")
        break
    