# COMP3550-1 Lab1
# MacchiaroliM 5-17-2020
# Deliverable 2
#############
# Using the above code write an interactive python program, 
# requesting a user’s password and the hashing algorithm 
# they wish to use. The output should be the actual password, 
# the hash name, and the hashed password.  
# Please include at least one extra hashing algorithm discussed 
# in lecture or from your research of the topic
#############
import passlib.hash # Pass Library
from getpass import getpass # ()___)____________)

def listavail(): # List possible algorithms
    print()
    print("The following is a list of acceptable inputs: ")
    for item in dir(passlib.hash):
        if dir(passlib.hash).index(item) > 28:# List all items in the library ((minus the fancy stuff we dont care about))
            print(item)                       # Making it this way is more tedious, but helps me be lazier down the line
    print("To exit type \"exit\" or \"quit\"")

while True:# (¬_¬)

    #salt=input("hahaha you're funny...") # I totally would but I work full time and I dont sleep as it is

    passwd=getpass("\nPlease enter a (*fake*) password: ") # please dont use your real password, it's just good practice

    while True: # Look, I know, but i'm not paid enough for this
        alg=input("Please enter a hashing algorithm: ").lower() # lower(case)

        if alg=="help":
            listavail() # 01189998819991197253

        elif alg=="exit" or alg=="quit" or alg=="e" or alg=="q" or alg=="sudo shutdown -p now": # (for power users)
            print("Goodbye!")
            exit(0) # quit, quit now, leave immediately, do not pass go, do not collect $200

        elif alg in dir(passlib.hash):
            hashFunc=getattr(passlib.hash,alg) # (actual comment) you can't casually stick strings in commands so this does some fancy stuff to let me reference it with function modules
            
            #this is where i'd put the checking to make sure you didn't use a hash that i've overlooked and uses a different format from the others... but I have better things to worry about than a couple of edge-cases.   (also why i didnt add salt, some of em' are flipped and i really dont wanna deal with that right now)

            print("\nHash of \""+passwd+"\" using "+alg+": "+hashFunc.hash(passwd)) # print the thing... (compressed to one line)
            retry=input("\n(N)ew password  (R)euse password  (Q)uit: ").upper() # upper(case)

            if retry=="N":
                break # there is no escape

            elif retry=="Q":
                 print("Maybe Next Time then...")
                 exit(0) # yeah yeah, just get out

            elif retry=="R":
                print() # s p a c e s  a r e  a e s t h e t i c

            else:
                 print("... well that's not very helpful. I'll presume you're so excited you've mistyped and want to have another go.\n")
        else:
            print("\nPlease enter a valid operation.")
            print("For a list of valid operations, please enter \"help\".\n")