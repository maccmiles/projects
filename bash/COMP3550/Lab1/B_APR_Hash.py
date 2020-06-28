# COMP3550-1 Lab1
# MacchiaroliM 5-17-2020
# Question B1
#############
#Create a Python script to create the APR1
#hash for the following: "changeme","123456","password"
#Prove them against on-line APR1 generator
#(or from the page given above).
#############
from passlib.hash import apr_md5_crypt
words=["changeme","123456","password"]
salt="PkWj6gM4"
for x in words:
    print("Hashes for \""+x+"\":")
    print ("MD5 Hash: "+apr_md5_crypt.using(salt=salt).hash(x)) # .encrypt deprecated, using hash instead