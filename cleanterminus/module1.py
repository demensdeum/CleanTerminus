import os

def clear():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
    else:
        print("Clean Terminus does not support your OS!")

if __name__ == "__main__":
    clear()