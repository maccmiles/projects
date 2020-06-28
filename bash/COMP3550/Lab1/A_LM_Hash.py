# COMP3550-1 Lab1
# MacchiaroliM 5-17-2020
# Question A1
#############
#Create a Python script to determine the LM
#hash and NTLM hash of the following
#words:"Napier","Foxtrot"
#############
from passlib.hash import lmhash,nthash
words=["Napier","Foxtrot"]
for x in words:
    print("Hashes for \""+x+"\":")
    print ("LM Hash: "+lmhash.hash(x)) # .encrypt deprecated, using hash instead
    print ("NT Hash: "+nthash.hash(x)) # .encrypt deprecated, using hash instead
