names = ["Gabriel","Larissa","Vaneli","Ele","admin"]

if len(names) > 0:
    for name in names:
        if name.lower() == "admin":
            print(f"Olá {name.title()}")
        else:
            print(f"Outra vez por aqui, {name}")
else:
    print("Lista precisa de coisa")

