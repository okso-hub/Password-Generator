import string, random, os

clear = lambda: os.system('clear') if os.name == "posix" else os.system("cls")

string.ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!"§$%&/()=?' 

    
    
def main():

    length = int(input("Enter the length of the password ")) 

    password = "" 

    while length > 0: 
        password += random.choice(string.ascii_letters) 
        length -= 1 
    print(f"Your password is {password}")


if __name__ == "__main__":
    clear()
    main()
