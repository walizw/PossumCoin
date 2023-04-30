from .blockchain.chain import Chain

import readline

readline.parse_and_bind("tab: complete")
readline.parse_and_bind("set editing-mode emacs")

while True:
    line = input(">>> ")
    if line == "exit":
        break
    elif line == "help":
        print("\t\t> PossumCoin <\n")
        print("Commands:")
        print("- help: show this screen")
        print("- exit: exits the program")
