# -*- coding: utf-8 -*-
import random

def generate_password(lowercase,numbers,v,b,a,s,d,f):
    password=[]
    if lowercase==True:
        for i in range(a):
            password.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
    if numbers==True:
        for i in range(s):
            password.append(random.choice('0123456789'))
    if v==True:
        for i in range(d):
            password.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if b==True:
        for i in range(f):
            password.append(random.choice('!@#$%^&*()'))
    random.shuffle(password)
    new_password=''.join(password)
    return new_password