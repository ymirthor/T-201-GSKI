import sys

from random import Random

rand = Random()
rand.seed(742983798423)

some_name = [
    "Gardar",
    "Ymir",
    "Kristofer",
    "Jason",
    "Danni",
    "Eggert",
    "Bjartur"
]

some_adjective = [
    "hommi",
    "fagri",
    "skemmtilegi",
    "leidinlegi"
]

def create_directories():
    level = 1
    commands = {1: "mkdir",
                2: "ls",
                3: "cd",
                4: "rm"}

    for _ in range(100):        
        choice = rand.randint(1, 4)
        print(commands[choice], end=" ")

        if choice == 2:
            pass
        else:
            print(rand.choice(some_name), end="")
            print("-" + rand.choice(some_adjective),end="")
            print("-" + str(rand.randint(0,9)), end="")
        print()        

def main():
    orig_stdout = sys.stdout
    fout = open(sys.path[0] + "/ymirs_commands.txt", 'w+')
    sys.stdout = fout

    for _ in range(30):
        create_directories()

    sys.stdout = orig_stdout
    fout.close()


if __name__ == "__main__":
    main()