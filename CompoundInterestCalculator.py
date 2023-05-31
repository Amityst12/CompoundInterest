import tkinter as tk
from tkinter import ttk

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

def mainTest():
    P = float(input("Enter initial amount:"))
    r = float(input("Enter interest rate:"))
    t = float(input("Enter amount of years:"))
    ans =  Calculate_Compound_Yearly(P,r,t)
    ans1 =  Calculate_Compound_Semi(P,r,t)
    ans2 =  Calculate_Compound_Quarterly(P,r,t)
    ans3 = Calculate_Compound_Monthly(P,r,t)
    print(f"Yearly: {ans}\nSemi: {ans1} \nQuar: {ans2} \nMonthly: {ans3}")
    
def mainTK():
    pass

root = tk.Tk()
root.geometry("500x450")
root.title("Compound Interest Calculator")

# Title label
label_Title = tk.Label(root, text="Compound Interest Calculator!", font=("Arial", 20))
label_Title.grid(column=0, columnspan=4, padx=45, pady=15)

# Initial amount label and entry
text_Initial = tk.Label(root, text="Initial amount:", font=("Arial", 18))
text_Initial.grid(row=1, column=0, sticky="E", padx=5, pady=5)
resault_Initial = tk.Text(root, height=1, width=11, font=("Arial", 18))
resault_Initial.grid(row=1, column=1, sticky="W", padx=5, pady=5, columnspan=4)

# Interest rate label and entry
text_Interest = tk.Label(root, text="Interest rate:", font=("Arial", 18))
text_Interest.grid(row=2, column=0, sticky="E", padx=5, pady=5)
resault_Interest = tk.Text(root, height=1, width=11, font=("Arial", 18))
resault_Interest.grid(row=2, column=1, sticky="W", padx=5, pady=5, columnspan=4)

# Years label and entry
text_Years = tk.Label(root, text="Years:", font=("Arial", 18))
text_Years.grid(row=3, column=0, sticky="E", padx=5, pady=5)
resault_Years = tk.Text(root, height=1, width=11, font=("Arial", 18))
resault_Years.grid(row=3, column=1, sticky="W", padx=5, pady=5, columnspan=4)

# Options
options = ["Yearly", "Semi-Yearly", "Quarterly", "Monthly"]
selected_option = tk.StringVar(root)
selected_option.set(options[0])

text_Freq = tk.Label(root, text="Frequency:", font=("Arial", 18))
text_Freq.grid(row=4, column=0, sticky="E", padx=5, pady=5)

menu_Options = tk.OptionMenu(root, selected_option, *options)
menu_Options.config(font=("Arial", 14))
menu_Options.grid(row=4, column=1, sticky="W", padx=5, pady=5, columnspan=4)

root.mainloop()

    
    