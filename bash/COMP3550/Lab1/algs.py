# COMP3550-1 Lab1
# MacchiaroliM 5-17-2020
# Deliverable 2
#############
#Using the above code write an interactive python program, 
# requesting a user’s password and the hashing algorithm 
# they wish to use. The output should be the actual password, 
# the hash name, and the hashed password.  
# Please include at least one extra hashing algorithm discussed 
# in lecture or from your research of the topic
#############
import passlib.hash # Pass Library

def listavail(): # List possible algorithms
    print()
    print("The following is a list of acceptable inputs: ")
    for item in dir(passlib.hash):
        if dir(passlib.hash).index(item) > 28:
            print(item)
    print("To exit type \"exit\" or \"quit\"")


passwd=input("Please enter a (fake) password: ")
while True:
    alg=input("Please enter a hashing algorithm: ").lower()

    if alg=="help":
        listavail()
    elif alg=="exit" or "quit" or "q":
        exit(0)
    elif alg in dir(passlib.hash): #if valid operation
        hashFunc=getattr(passlib.hash, alg) #build command with chosen operation
        print ("Hash of \""+passwd+"\" using "+alg+": "+hashFunc.hash(passwd)) #return hash
        print("\n\n")
        print("Would you like to ")

    else:
        print("Please enter a valid operation.")
        print("For a list of operations, please enter \"help\".")
