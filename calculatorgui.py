
from tkinter import *
 
expression=""
 
def press(num):

    global expression

    expression=expression+str(num)

    equation.set(expression)
 
def equalpress():

    global expression

    total=str(eval(expression))

    equation.set(total)

    expression=""
 
def clear():

    global expression

    expression=""

    equation.set("")
 
 
root=Tk()
 
root.configure(background='grey')

root.title('Simple Calculator')
 
root.geometry("400x300")
root.resizable(False,False)
 
equation=StringVar()
 
expression_field = Entry(root, textvariable=equation)

expression_field.grid(column=1,row=0, pady=5)
 
button1= Button(root, text='1', fg='black', bg='light grey', command=lambda:press(1), height=1,width=10)

button1.grid(column=0,row=1, pady=5)
 
button2= Button(root, text='2', fg='black', bg='light grey', command=lambda:press(2), height=1,width=10)

button2.grid(column=1,row=1, pady=5)
 
button3= Button(root, text='3', fg='black', bg='light grey', command=lambda:press(3), height=1,width=10)

button3.grid(column=2,row=1, pady=5)
 
button4= Button(root, text='4', fg='black', bg='light grey', command=lambda:press(4), height=1,width=10)

button4.grid(column=0,row=2, pady=5)
 
button5= Button(root, text='5', fg='black', bg='light grey', command=lambda:press(5), height=1,width=10)

button5.grid(column=1,row=2, pady=5)
 
button6= Button(root, text='6', fg='black', bg='light grey', command=lambda:press(6), height=1,width=10)

button6.grid(column=2,row=2, pady=5)
 
button7= Button(root, text='7', fg='black', bg='light grey', command=lambda:press(7), height=1,width=10)

button7.grid(column=0,row=3, pady=5)
 
button8= Button(root, text='8', fg='black', bg='light grey', command=lambda:press(8), height=1,width=10)

button8.grid(column=1,row=3, pady=5)
 
button9= Button(root, text='9', fg='black', bg='light grey', command=lambda:press(9), height=1,width=10)

button9.grid(column=2,row=3, pady=5)
 
button10= Button(root, text='0', fg='black', bg='light grey', command=lambda:press(0), height=1,width=10)

button10.grid(column=1,row=4 ,pady=5)
 
decimalpoint=Button(root, text='.',fg='black', bg='light grey', command=lambda:press('.'), height=1,width=10)

decimalpoint.grid(column=2,row=4, padx=5, pady=5)
 
add= Button(root, text='+', fg='black', bg='light grey', command=lambda:press('+'), height=1,width=10)

add.grid(column=4,row=1,  padx=5, pady=5)
 
subtract= Button(root, text='-', fg='black', bg='light grey', command=lambda:press('-'), height=1,width=10)

subtract.grid(column=4,row=2,  padx=5, pady=5)
 
multiply= Button(root, text='*', fg='black', bg='light grey', command=lambda:press('*'), height=1,width=10)

multiply.grid(column=4,row=3,  padx=5, pady=5)
 
divide= Button(root, text='/', fg='black', bg='light grey', command=lambda:press('/'), height=1, width=10)

divide.grid(column=4,row=4,  padx=5, pady=5)
 
clear=Button(root,text='Clear',fg='black',bg='light grey',command=clear,height=1, width=10)

clear.grid(column=1, row=5,  pady=5)
 
equal=Button(root, text='=',fg='black', bg='light grey', command=lambda:equalpress(), height=1,width=10)

equal.grid(column=0, row=4,  padx=5, pady=5)

root.mainloop()
