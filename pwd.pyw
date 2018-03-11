## This module manages Passwords to enter the Discord+ Client.
from cryptography.fernet import Fernet
import base64
import os
import sys
import csv


def enAES256(input_plaintext):
    cphKey = Fernet.generate_key()
    cipher = Fernet(cphKey)
    plntxt = bytes(input_plaintext, "utf-8")
    en = cipher.encrypt(plntxt)
    return en, cphKey

def deAES256(input_bytes, cphKey):
    cipher = Fernet(cphKey)
    return cipher.decrypt(input_bytes)


def pwdNew():
    pwd = str(input("Enter a password, this password is stored on Client and is not transfered. It is also hashed to be safe.\n"))
    pwdCn = str(input("Please Confirm Your Password.\n"))
    while pwd != pwdCn:
        pwd = str(input("Passwords do not match! Re-enter password.\n"))
        pwdCn = str(input("Please Confirm Your Password.\n"))
    if pwd == pwdCn:
        pwd = enAES256(str(pwd))
        csv.writer(open("pwdInternal.csv", "w"), lineterminator='\n').writerows([[pwd[0], pwd[1]]])
    print("Password Has Been Sucessfuly set and hashed.")


def pwd_unhash():
    pwd = []
    for line in csv.reader(open("pwdInternal.csv", "r"), delimiter=','):
        pwd.append(line)
    pwd = pwd[0]
    pwdls0 = list(pwd[0])
    pwdls1 = list(pwd[1])
    del pwdls0[0:1]
    del pwdls0[-1]
    del pwdls1[0:1]
    del pwdls1[-1]
    pwd[0] = "".join(pwdls0)
    pwd[1] = "".join(pwdls1)
    pwd = deAES256(bytes(pwd[0], "utf-8"), bytes(pwd[1], "utf-8"))
    pwd = list(pwd)
    for x in range(len(pwd)):
        pwd[x] = chr(pwd[x])
    pwd = "".join(pwd)
    return pwd
