import tkinter as tk
import math

"""
Compound interest formula = A = P(1 + r/n)^(nt)

A = the final amount (including both the principal and the interest)

P = the principal amount (the initial amount of money)
r = the annual interest rate (expressed as a decimal)
n = the number of times that interest is compounded per year
t = the number of years
"""

def Calculate_Compound(P,r,n,t):
    
    r = float(r / 100.0)
    power = float(n*t)
    inside = float(1 + r / n)
    start = float(P)
    
    full = math.pow(inside,power)
    pFull = full * start
    return  round(pFull,2)

def Calculate_Compound_Yearly(P,r,t):#Once a year
    
    r = float(r / 100.0)
    power = float(t)
    inside = float(1 + r / 1)
    start = float(P)
    
    full = math.pow(inside,power)
    pFull = full * start
    return  round(pFull,2)

def Calculate_Compound_Semi(P,r,t):#Twice a year
    r = float(r / 100.0)
    power = float(2*t)
    inside = float(1 + r / 2)
    start = float(P)
    
    full = math.pow(inside,power)
    pFull = full * start
    return  round(pFull,2)

def Calculate_Compound_Quarterly(P,r,t):#Four times a year
    r = float(r / 100.0)
    power = float(4*t)
    inside = float(1 + r / 4)
    start = float(P)
    
    full = math.pow(inside,power)
    pFull = full * start
    return  round(pFull,2)

def Calculate_Compound_Monthly(P,r,t):#Twelve times a year
    
    r = float(r / 100.0)
    power = float(12*t)
    inside = float(1 + r / 12)
    start = float(P)
    
    full = math.pow(inside,power)
    pFull = full * start
    return  round(pFull,2)

def main():
    P = float(input("Enter initial amount:"))
    r = float(input("Enter interest rate:"))
    t = float(input("Enter amount of years:"))
    ans =  Calculate_Compound_Yearly(P,r,t)
    ans1 =  Calculate_Compound_Semi(P,r,t)
    ans2 =  Calculate_Compound_Quarterly(P,r,t)
    ans3 = Calculate_Compound_Monthly(P,r,t)
    print(f"Yearly: {ans}\nSemi: {ans1} \nQuar: {ans2} \nMonthly: {ans3}")
main()
    
    
    