BLUE = "\033[94m"
RED = "\033[91m"
ORANGE = "\033[93m"
PINK = "\033[35m"
GREEN = "\033[92m"
BOLD = "\033[;1m"
RESET = "\033[0m"
WHITE = "\033[97m"


def primaire(chaine):
    pprint("=======================================",BLUE,True)
    pprint(chaine,bold=True)
    pprint("=======================================",BLUE,True)
    print("\n")

def warning(chaine,hard = 0):
    if hard == 2:
        pprint(f"===> {chaine}",RED)
    elif hard == 1:
        pprint(f"===> {chaine}",ORANGE)
    else:
        pprint(f"===> {chaine}",PINK)
    print("\n")

def securite():
    pprint(f"Confirmer le lancement ? [{GREEN}o{WHITE}/{RED}n{RESET}] ", BOLD)
    res = input()
    print("\n")
    return res

def information(chaine):
    if type(chaine) == str:        
        print(f"---   {chaine}   ---")
    elif type(chaine) == list:
        for c in chaine:
            print(f"---   {c}   ---")
    print("\n")

def final(chaine):
    pprint(chaine,GREEN,bold=True)
    print("\n")


def pprint(chaine, couleur = WHITE, bold = False):
    if bold:
        print(f"{BOLD}{couleur}{chaine}{RESET}")
    else:
        print(f"{couleur}{chaine}{RESET}")

def to_bold(chaine):
    return f"{BOLD}{chaine}{RESET}"