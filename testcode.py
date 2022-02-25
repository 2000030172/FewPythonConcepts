# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 15:47:06 2022

@author: Dell
"""

print("Welcome to KL University, Vijayawada.......!")
first=input()
last=input()
regid=int(input())
status=eval(input())
qualification=eval(input())

print("Your details are saved :")
print("First Name : ",first)
print("Last Name : ",last)
print("Name : ",first,last)
print("Registered ID : ",regid)
print("Result Status : ",status)
print("Qualified : ",qualification)


a=list(map(int,input("Enter 5 values").split()))