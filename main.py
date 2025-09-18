def chat(mes):
    if mes == "!exit":
        return 1
    else:
        print(f"[User] {mes} \n")
    return 0
    

while True:
    if chat(mes=input("Chat > ")) == 1:
        print("Program has ended")
        break
    