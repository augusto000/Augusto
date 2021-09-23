#Este programa separa la primera inicial de un nombre
def splitInitials(name):
    firstInit= name[0:1]
    return firstInit

def main():
    name=input("Input the First letter :")
    second_name=input("Input your second name :")

    print(f"Your initials af"+splitInitials(name)+\
        splitInitials(second_name))

if __name__=="__main__":
    main()    