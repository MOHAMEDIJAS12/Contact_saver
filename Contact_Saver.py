# To Add Data of a Person---!
def add():
    print("--" * 26, "To Add Data", "--" * 26)
    with open("project.txt", "a") as o:
        x, y = input("\nEnter your Name: "), 1
        while len(str(y)) != 10:
            y = int(input("\nEnter your Number [10 digits--!]: "))
            if x.isalpha and str(y).isdigit():
                o.write(f"\n{x.title()}:{y}")
            else:
                error()
        print("!--Data Added Sucessfully--!")

        o.flush()
    o.close()
# To Search a Data--!
def search():
    print("\n[1]-Search Single Data")
    print("\n[2]-Search Multiple Data")
    l = int(input("\n>>>>>"))
    if l == 1:
        print("--" * 22, "To Search Single Data", "--" * 22)
        with open("project.txt", "r") as o:
            f = o.read().strip()
            s = dict()
            for i in f.split("\n"):
                u = i.split(":")
                s.update({u[0]: int(u[1])})

            r = input("\nEnter the Name to Search:  ")
            r = r.title()
            if r in s:
                print(f"\nNumber of {r}", s[r])
            else:
                error()
            o.flush
        o.close()
    elif l == 2:
        print("--" * 23, "To Search Multiple Data", "--" * 23)
        b = int(input("\nEnter No.of Data's should be Searched: "))
        h = ""
        for i in range(0, b):
            h += input("\nEnter the Name: ")
            h += " "
        h = h.title()
        h = h.split()
        with open("project.txt", "r") as o:
            f = o.read().strip()
            s = dict()
            for i in f.split("\n"):
                u = i.split(":")
                s.update({u[0]: int(u[1])})
            for i in range(0, b):
                if h[i] in s:
                    print(f"\n\nNumber of {h[i]}", s[(h[i])])
# To Get all the Data
def get_all():
    print(("--" * 21) + "!!--ALL DATA IN THE DATABASE--!!" + ("--" * 21))
    with open("project.txt", "r") as o:
        f = o.read().strip()
        s = dict()
        for i in f.split("\n"):
            u = i.split(":")
            s.update({u[0]: int(u[1])})
        for i in s:
            print(f" {i} --  {s[i]}")
        o.flush()
    o.close()
def error():
    print("--_ERROR_-- Enter the Correct Data--!")
def pro():
    while True:
        print("--" * 25, "Contact Saver", "--" * 26)
        print("\n[1]-Add Data")
        print("[2]-Search Data")
        print("[3]-Show all Data")
        print("[0]-Quit")
        t = int(input("\n\n>>>>>"))
        if t == 1:
            add()
        elif t == 2:
            search()
        elif t == 3:
            get_all()
        elif t == 0:
            print("Thank you Have a good day :)")
            break
pro()