# COMP3550-1 Lab1
# MacchiaroliM 5-17-2020
# Question D1
#############
#Create a Python script to create the PHPass
#hash for the following: "changeme","123456","password"
#Prove them against on-line PHPass generator
#(or from the page given above).
#Just note the first five characters of the
#hashed value.
#############
from passlib.hash import phpass
words=["changeme","123456","password"]
salt="ZDzPE45C"

for x in words:
    print("Hashes for \""+x+"\":")
    print("Salt Used: \""+salt+"\"")
    print ("PHPass Hash: "+phpass.hash(x,salt=salt,rounds=7)) # .encrypt deprecatyed, using hash instead