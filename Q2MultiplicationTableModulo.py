# multiplication function 
#https://www.youtube.com/watch?v=CqaB4B7xzNA
def multiplication():
    print("Please enter a number: /n")
    a = int(input())

    print("\t\t\t Multiplation Mod " + str(a) + "\n")

    for i in range(1,a):
        print(i, end="\t")
    print()
    print("--------------------------------------------------------------------------------------")

    for j in range(1,a):
        for k in range (1,a):
            print((j * k) % a, end="\t")
        print("\n")

multiplication()