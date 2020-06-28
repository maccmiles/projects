# COMP3550-1 Lab1
# MacchiaroliM 5-17-2020
# Question C1
#############
#Create a Python script to create the SHA
#hash for the following: "changeme","123456","password"
#Prove them against on-line SHA generator
#(or from the page given above).
#############
from passlib.hash import sha1_crypt,sha256_crypt,sha512_crypt
words=["changeme","123456","password"]
salt="8sFt66rZ"
for x in words:
    print("Hashes for \""+x+"\":")
    print ("SHA1 Hash: "+sha1_crypt.using(salt=salt).hash(x)) # .encrypt deprecatyed, using hash instead
    print ("SHA256 Hash: "+sha256_crypt.using(salt=salt).hash(x)) # .encrypt deprecatyed, using hash instead
    print ("SHA512 Hash: "+sha512_crypt.using(salt=salt).hash(x)) # .encrypt deprecatyed, using hash instead