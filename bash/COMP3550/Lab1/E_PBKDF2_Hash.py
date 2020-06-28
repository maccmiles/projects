# COMP3550-1 Lab1
# MacchiaroliM 5-17-2020
# Question E1
#############
#Create a Python script to create the PBKDF2
#hash for the following (uses a salt value of
#“ZDzPE45C”). You just need to list the first six
#hex characters of the hashed value.
#############
from passlib.hash import pbkdf2_sha1,pbkdf2_sha256
words=["changeme","123456","password"]
salt="ZDzPE45C"
b = bytes(salt, 'utf-8') # Salts for pbkdf2 must me in byte format, not string format
for x in words:
    print("Hashes for \""+x+"\":")
    print ("PBKDF2 (SHA1): "+pbkdf2_sha1.using(salt=b).hash(x))
    print("PBKDF2 (SHA256): "+pbkdf2_sha256.using(salt=b).hash(x)) # .encrypt deprecatyed, using hash instead
