# COMP3550-1 Lab1
# MacchiaroliM 5-17-2020
# Question F1
#############
#Create the hash for the word “hello” for the
#different methods (you only have to give the
#first six hex characters for the hash):MD5, SHA-1, SHA-256, SHA-512, DES
#MD5 SHA1 SHA256 SHA512 DES
#Also note the number hex characters that the hashed value uses:MD5, Sun MD5, SHA-1, SHA-256, SHA-512
#############
from passlib.hash import md5_crypt,sun_md5_crypt,sha1_crypt,sha256_crypt,sha512_crypt,des_crypt
words=["hello"]
salt="ZDzPE45C"

for x in words:
    print("Hashes for \""+x+"\":")
    md5=md5_crypt.using(salt=salt).hash(x)
    print ("MD5: "+md5)
    sha1=sha1_crypt.using(salt=salt).hash(x)# .encrypt deprecatyed, using hash instead
    print("SHA1: "+sha1) 
    sha256=sha256_crypt.using(salt=salt).hash(x)
    print("SHA256: "+sha256)
    sha512=sha512_crypt.using(salt=salt).hash(x)
    print("SHA512: "+sha512_crypt.using(salt=salt).hash(x))

    des=des_crypt.using(salt=salt[:2]).hash(x) # first 2 chars of salt
    print("DES: "+des)
    print("")
    print("Hex length for \""+x+"\":")
    print("MD5: "+str(len(md5)))
    print("Sun MD5: "+str(len(sun_md5_crypt.using(salt=salt).hash(x))))
    print("SHA-1: "+str(len(sha1)))
    print("SHA-256: "+str(len(sha256)))
    print("SHA=512: "+str(len(sha512)))


