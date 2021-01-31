import os
import datalayer as IO

members = {
    0: {"name": "Gardar", "phone": "5812345", "email": "gardar19@ru.is", "yob": 1995},
    1: {"name": "Ymir", "phone": "8574696", "email": "ymir19@ru.is", "yob": 2000}
}
sports = {
    0: {"name":"Sund", "members": [0,1]}, 
    1: {"name": "Box", "members": []}
}
# JSON file
{
    "members": [
        {
            "name": "Garðar",
            "phone": "6182827",
            "email": "gardar19@ru.is",
            "year_of_birth": 1995
        },
        {
            "name": "Ymir",
            "phone": "8574696",
            "email": "ymir19@ru.is",
            "year_of_birth": 2000
        },
        {
            "name": "Jason",
            "phone": "8445921",
            "email": "jason19@ru.is",
            "year_of_birth": 1998
        }
    ]
}

class Sport:
    def __init__(self):
        self.main()
    
    def main(self):
        while True:
            os.system("cls")
            print("--------------------- \n")
            print("[1] Sports\n[2] Members\n[Q] Exit")
            choice = input()
            if choice.upper() == "Q":
                return
            elif choice == "1":
                self.list_of(sports)
            elif choice == "2":
                self.list_of(members)
                
    def list_of(self, adict):
        while True:
            os.system("cls")
            for k,d in adict.items():
                print("[{}] {}".format(k+1,d["name"]))
            print("[N] New\n[B] Back")
            choice = input() 
            if choice.upper() == "B":
                return
            if choice.upper() == "N":
                self.new(adict)
                return
            if choice.isdigit():
                choice = int(choice) - 1
                if choice in adict:
                    self.edit(adict, choice)
                    return
            print("Invalid command!")

    def edit(self, adict, idx):
        while True:
            os.system("cls")
            
            for key, data in adict[idx].items():
                if type(data) is list:
                    new_data = ""
                    for i in data:
                        new_data += members[i]["name"]
                        if i != data[-1]:
                            new_data += ", "
                    data = new_data
                print("{:<5}: {}".format(key ,data))
            
            print("[R] Remove\n[B] Back")
            choice = input()
            if choice.upper() == "B":
                return
            if choice.upper() == "R":
                del adict[idx]
                return
            print("Invalid command!")

    def input_name(self):
        while True:
            lol = input("Enter name: ").split()
            if all([i.isalpha() for i in lol]):
                return " ".join(lol)
            
            else:
                print("Name has to be letters")


    def input_phone(self):
         while True:
            lol = input("Phone number: ").strip()
            if lol.isdigit() and len(lol) == 7:
                return lol
            
            else:
                print("Not a valid phone number")

    def input_email(self):
        while True:
            lol = input("Email: ").strip()
            for idx, i in enumerate(lol):
                if i == "@":
                    for i in lol[idx:]:
                        if i == ".":
                            return lol
                    continue
            else:
                print("Not a valid Email")

    def input_yob(self):
        while True:
            lol = input("Year of birth: ").strip()
            if lol.isdigit() and len(lol) == 4:
                return lol
            
            else:
                print("Not a valid Year of birth")

    def new(self, adict):
        counter = 0
        while counter in adict:
            counter += 1
        if adict == members:
            adict[counter] = {
                "name": self.input_name(), 
                "phone": self.input_phone(),
                "email": self.input_email(), 
                "yob": int(input("Year of birth: "))
            }
            return
        else:
            adict[counter] = {
                0: {"name": input("Sport name: "), 
                "members": []}, 
            }
            return

Sport()