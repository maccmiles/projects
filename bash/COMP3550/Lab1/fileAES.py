# COMP3550-1 Lab1
# MacchiaroliM 5-17-2020
# Deliverable 3
#############
# Using the above code as a guide and pycrypto module write
# a python program using AES to encrypt and/or decrypt a file.
#############

from Crypto.Cipher import AES #pycrypto deprecated, using pycryptodome 3.9.7 (same syntax)
from Crypto.Random import get_random_bytes as randB  # to generate random keys (32b) for your file
import hashlib # importing for aid in verifying the hash of origin file and destination file

# for the sake of my sanity we're using functions this time around (3x as fun as the last one!)

def verify(file,fileBuffer): # verify the origin and decrypt via hex
    fileHash = hashlib.sha256() # create object to feed bytes into
    with open(file, 'rb') as d:
        dataBytes = d.read(fileBuffer) # Read in data as chunk
        while len(dataBytes) > 0: # while we have data
            fileHash.update(dataBytes) # inserts data to the dictionary
            dataBytes = d.read(fileBuffer) # bring in next chunks
    return fileHash.hexdigest() # return answer



def encrypt(key,docin,fileBuffer): # encrypt function ... it encrypts things

    fileOrigin = open(docin, 'rb') # open file as read bytes
    fileDestination = open(docin + '.enc', 'wb') # make new file with write bytes (add .enc to make sure it's encrypted!)

    encryptCypher = AES.new(key, AES.MODE_CFB) # define cypher, using AES

    fileDestination.write(encryptCypher.iv) # store the Initialization vector to destination file

    dataBuffer = fileOrigin.read(fileBuffer) # put your left foot in
    while len(dataBuffer) > 0: # while we have data
        encryptedData = encryptCypher.encrypt(dataBuffer) # shake it all about
        fileDestination.write(encryptedData) # do the hokey-pokey
        dataBuffer = fileOrigin.read(fileBuffer) # increment segment

    fileOrigin.close() # close origin
    fileDestination.close() # that's what it's all about!




def decrypt(key,docin,fileBuffer): # decrypt function ... it (hopefully) (de)crypts things

# This function does much the same as the previous, it just flips from encrypt to decrypt, all processing is identical

# in retrospect, i'd do that fancy thing from my last program (hashFunc=getattr(passlib.hash,alg))
# but the formatting is really finikey and I'm doing this last minute like I shouldn't be

    fileOrigin = open(docin + '.enc', 'rb') # open the file we just closed (inefficient, i know!)
    fileDestination = open(docin + '.dec', 'wb') # make a new, more different file for our destination
    
    encryptCypher = AES.new(key, AES.MODE_CFB, iv=fileOrigin.read(16)) # make a new cypher, with the first 16b of file as the Initialization vector 
    
    dataBuffer = fileOrigin.read(fileBuffer) # load up that buffer!
    while len(dataBuffer) > 0:
        decrypted_bytes = encryptCypher.decrypt(dataBuffer) # CTL+Z
        fileDestination.write(decrypted_bytes) # CTL+V
        dataBuffer = fileOrigin.read(fileBuffer) # TAB(x32)
    
    fileOrigin.close() # CTL+S
    fileDestination.close() # New (de)crypted file, should match original document







#==================================
#         Too Many Colors!
#==================================







key = randB(32) # Random key in bytes (must be 16,32,etc)
#docin ='C:/Users/macchiarolim/Documents/WIT/2020-21/Summer 2020/Computer Security/git/projects/bash/COMP3550/Lab1/testdoc.txt'#file path in
fileBuffer = 65536 # 64k in binary (very picky)
loop="y" # looooooooooops
while loop=="y": # (¬_¬)
    docin=input("Please specify the absolute path of the file you'd like to process: ") # file path in
    
    print("Processing File: \""+docin+" \"")
    print("\nEncrypting Document...")
    
    encrypt(key,docin,fileBuffer) # (En)crypt the thing!
    
    print("\nDecrypting Document...")
    decrypt(key,docin,fileBuffer) # (De)Crypt the thing!
    
    print("\nComparing Decrypted Document with Original...")
    
    if verify(docin,fileBuffer) == verify(docin + '.dec',fileBuffer): # Validate origin and decrypt match
        print("Decrypt: OK") #we did it reddit!
    else:
        print("Hash Error! Files are mismatched.") # the odds are not in your favor
    
    retry=input("\nGo Again? (Y/N)").lower() # Same spiel, make anything you type lowercase
    if retry=="n":
        loop="" # See you next time
