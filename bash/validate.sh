#!/bin/bash
echo -n "Enter First Name: "
read fName #only Letters and hyphens

if [[ $fName =~ [^a-zA-Z-] ]]; then #Any characters or hyphens
     echo Invalid Name
     exit 1
else
    echo -n " "
fi
echo -n "Enter Last Name: "
read lName #only letters and hyphens

if [[ $lName =~ [^a-zA-Z-] ]]; then #Any characters or hyphens
     echo Invalid Name
     exit 1
else
    echo -n " "
fi
echo -n "Enter Zip Code: "
read uZip #only 5 digits

if [[ $uZip =~ [0-9]{5} ]]; then #any num 5 times
     echo -n "Enter Email Address: "
     read uMail #onl letters num dots underscores hyphens @
     if [[ $uMail =~ [^a-zA-Z\._\-@] ]]; then #any num 5 times
	     echo Invalid Email
             exit 1
	else
	    echo -n " "
	fi
else
    echo Invalid Zip
    exit 1
fi


	
