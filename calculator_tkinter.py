from tkinter import *
import math

root = Tk()
root.title("Calculator GUI By Aatif")

e1 = Entry(root,bg = "#9de5f2",width = 33,font = ("calibri",11))
e2 = Entry(root,bg = "#9df2c8",width = 11,font = ("calibri",11))

e1.grid(row = 0,column = 0,columnspan = 3)
e2.grid(row = 0,column = 3,columnspan = 1)

def button_click(number):
    if(number == 10):
        e1.insert(END,'.')
    else:
        e1.insert(END,number)

def button_clear():
    e1.delete(0,END)

def button_add():
    e2.delete(0,END)
    e2.insert(0,'+')
    first_number = e1.get()
    global f_num
    f_num = float(first_number)
    global oper
    oper = "addition"
    e1.delete(0,END)

def button_sub():
    e2.delete(0,END)
    e2.insert(0,'-')
    first_number = e1.get()
    global f_num
    f_num = float(first_number)
    global oper
    oper = "subtraction"
    e1.delete(0,END)

def button_mul():
    e2.delete(0,END)
    e2.insert(0,'*')
    first_number = e1.get()
    global f_num
    f_num = float(first_number)
    global oper
    oper = "multiplication"
    e1.delete(0,END)

def button_div():
    e2.delete(0,END)
    e2.insert(0,'/')
    first_number = e1.get()
    global f_num
    f_num = float(first_number)
    global oper
    oper = "division"
    e1.delete(0,END)

def button_perc():
    e2.delete(0,END)
    e2.insert(0,'%')
    first_number = e1.get()
    global f_num
    f_num = float(first_number)
    global oper
    oper = "percentage"
    e1.delete(0,END)

def button_power():
    e2.delete(0,END)
    e2.insert(0,'^')
    first_number = e1.get()
    global f_num
    f_num = float(first_number)
    global oper
    oper = "power"
    e1.delete(0,END)

def button_gcd():
    e2.delete(0,END)
    e2.insert(0,"gcd")
    first_number = e1.get()
    global f_num
    f_num = int(first_number)
    global oper
    oper = "gcd"
    e1.delete(0,END)

def button_log_e():
    e2.delete(0,END)
    e2.insert(0,'ln')
    first_number = e1.get()
    global f_num
    f_num = float(first_number)
    global oper
    oper = "natural_logarithm"
    e1.delete(0,END)

def button_log_10():
    e2.delete(0,END)
    e2.insert(0,'log_10')
    first_number = e1.get()
    global f_num
    f_num = float(first_number)
    global oper
    oper = "common_logarithm"
    e1.delete(0,END)

def button_sin():
    e2.delete(0,END)
    e2.insert(0,"sin")
    first_number = e1.get()
    global f_num
    f_num = float(first_number)
    global oper
    oper = "sine"
    e1.delete(0,END)

def button_cos():
    e2.delete(0,END)
    e2.insert(0,"cos")
    first_number = e1.get()
    global f_num
    f_num = float(first_number)
    global oper
    oper = "cosine"
    e1.delete(0,END)

def button_tan():
    e2.delete(0,END)
    e2.insert(0,"tan")
    first_number = e1.get()
    global f_num
    f_num = float(first_number)
    global oper
    oper = "tangent"
    e1.delete(0,END)

def button_fact():
    e2.delete(0,END)
    e2.insert(0,"fact")
    first_number = e1.get()
    global f_num
    f_num = int(first_number)
    global oper
    oper = "factorial"
    e1.delete(0,END)

def button_abs():
    e2.delete(0,END)
    e2.insert(0,"abs")
    first_number = e1.get()
    global f_num
    f_num = float(first_number)
    global oper
    oper = "absolute_val"
    e1.delete(0,END)

def button_sqrt():
    e2.delete(0,END)
    e2.insert(0,"sqrt")
    first_number = e1.get()
    global f_num
    f_num = float(first_number)
    global oper
    oper = "square_root"
    e1.delete(0,END)

def button_inv():
    e2.delete(0,END)
    e2.insert(0,"1/x")
    first_number = e1.get()
    global f_num
    f_num = float(first_number)
    global oper
    oper = "inverse"
    e1.delete(0,END)

def button_equal():
    if(oper == "natural_logarithm"):
        e1.delete(0,END)
        e1.insert(0,math.log(f_num))
    elif(oper == "sine"):
        e1.delete(0,END)
        e1.insert(0,math.sin(f_num))
    elif(oper == "cosine"):
        e1.delete(0,END)
        e1.insert(0,math.cos(f_num))
    elif(oper == "tangent"):
        e1.delete(0,END)
        e1.insert(0,math.tan(f_num))
    elif(oper == "tangent"):
        e1.delete(0,END)
        e1.insert(0,math.log10(f_num))
    elif(oper == "factorial"):
        e1.delete(0,END)
        e1.insert(0,math.factorial(f_num))
    elif(oper == "absolute_val"):
        e1.delete(0,END)
        e1.insert(0,abs(f_num))
    elif(oper == "square_root"):
        e1.delete(0,END)
        e1.insert(0,math.sqrt(f_num))
    elif(oper == "inverse"):
        e1.delete(0,END)
        e1.insert(0,(1 / f_num))
    
    else:
        second_number = float(e1.get())
        e1.delete(0,END)
        if oper == "addition" :
            e1.insert(0, f_num + second_number)
        elif oper == "subtraction" :
            e1.insert(0,f_num - second_number)
        elif oper == "multiplication" :
            e1.insert(0,f_num * second_number)
        elif oper == "division" :
            e1.insert(0,f_num / second_number)
        elif oper == "percentage" :
            e1.insert(0, (f_num / second_number) * 100)
        elif oper == "power" :
            e1.insert(0,pow(f_num,second_number))
        # elif oper == "gcd" :
        #     second_number = int(second_number)
        #     res = math.gcd(f_num,second_number)
        #     e1.insert(0,res)

button_1 = Button(root,text = "7",width = 10,height = 5,bg = "#e89b72",command = lambda : button_click(7))#7
button_2 = Button(root,text = "8",width = 10,height = 5,bg = "#e89b72",command = lambda : button_click(8))#8
button_3 = Button(root,text = "9",width = 10,height = 5,bg = "#e89b72",command = lambda : button_click(9))#9
button_4 = Button(root,text = "sin",width = 10,height = 5,bg = "#e8c37d",command = button_sin)#sin
button_5 = Button(root,text = "4",width = 10,height = 5,bg = "#e89b72",command = lambda : button_click(4))#4
button_6 = Button(root,text = "5",width = 10,height = 5,bg = "#e89b72",command = lambda : button_click(5))#5
button_7 = Button(root,text = "6",width = 10,height = 5,bg = "#e89b72",command = lambda : button_click(6))#6
button_8 = Button(root,text = "cos",width = 10,height = 5,bg = "#e8c37d",command = button_cos)#cos
button_9 = Button(root,text = "1",width = 10,height = 5,bg = "#e89b72",command = lambda: button_click(1))#1
button_10 = Button(root,text = "2",width = 10,height = 5,bg = "#e89b72",command = lambda : button_click(2))#2
button_11 = Button(root,text = "3",width = 10,height = 5,bg = "#e89b72",command = lambda: button_click(3))#3
button_12= Button(root,text = "tan",width = 10,height = 5,bg = "#e8c37d",command = button_tan)#tan
button_13= Button(root,text = "0",width = 10,height = 5,bg = "#e89b72",command = lambda : button_click(0))#0
button_14= Button(root,text = "+",width = 10,height = 5,bg = "#e8c37d",command = button_add)#+
button_15= Button(root,text = "-",width = 10,height = 5,bg = "#e8c37d",command = button_sub)#-
button_16= Button(root,text = "fact",width = 10,height = 5,bg = "#e8c37d",command = button_fact)#fact
button_17= Button(root,text = "*",width = 10,height = 5,bg = "#e8c37d",command = button_mul)#*
button_18= Button(root,text = "/",width = 10,height = 5,bg = "#e8c37d",command = button_div)#/
button_19= Button(root,text = "abs",width = 10,height = 5,bg = "#e8c37d",command = button_abs)#abs
button_20= Button(root,text = "log10",width = 10,height = 5,bg = "#e8c37d",command = button_log_10)#log10
button_21= Button(root,text = "sqrt",width = 10,height = 5,bg = "#e8c37d",command = button_sqrt)#sqrt
button_22= Button(root,text = "%",width = 10,height = 5,bg = "#e8c37d",command = button_perc)#%
button_23= Button(root,text = "pow",width = 10,height = 5,bg = "#e8c37d",command = button_power)#pow
button_24= Button(root,text = "ln",width = 10,height = 5,bg = "#e8c37d",command = button_log_e)#ln
button_25= Button(root,text = "=",width = 10,height = 5,bg = "#9de5f2",command = button_equal)#=
button_26= Button(root,text = "1/x",width = 10,height = 5,bg = "#e8c37d",command = button_inv)#1/x
button_27 = Button(root,text = ".",width = 10,height = 5,bg = "#e8c37d",command =lambda :  button_click(10))#gcd
button_28 = Button(root,text = "Clear",width = 10,height = 5,bg = "#9df2c8",command = button_clear)#clear

button_1.grid(row = 1,column = 0)
button_2.grid(row = 1,column = 1)
button_3.grid(row = 1,column = 2)
button_4.grid(row = 1,column = 3)
button_5.grid(row = 2,column = 0)
button_6.grid(row = 2,column = 1)
button_7.grid(row = 2,column = 2)
button_8.grid(row = 2,column = 3)
button_9.grid(row = 3,column = 0)
button_10.grid(row = 3,column = 1)
button_11.grid(row = 3,column = 2)
button_12.grid(row = 3,column = 3)
button_13.grid(row = 4,column = 0)
button_14.grid(row = 4,column = 1)
button_15.grid(row = 4,column = 2)
button_16.grid(row = 4,column = 3)
button_17.grid(row = 5,column = 0)
button_18.grid(row = 5,column = 1)
button_19.grid(row = 5,column = 2)
button_20.grid(row = 5,column = 3)
button_21.grid(row = 6,column = 0)
button_22.grid(row = 6,column = 1)
button_23.grid(row = 6,column = 2)
button_24.grid(row = 6,column = 3)
button_25.grid(row = 7,column = 0)
button_26.grid(row = 7,column = 1)
button_27.grid(row = 7,column = 2)
button_28.grid(row = 7,column = 3)

root.mainloop()