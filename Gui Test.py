from tkinter import *
root = Tk()
root.title('Hello Python')
root.geometry("700x500+10+20")

import random
def Task1():
    count =  random.randint(10,20)
    for x in range(count):

        number =  random.randint(1,60)
        #print(x+1 ,":-" ,number)
        #print("_________")
        label = Label(root, text= (str(x+1),str(":-"),str(number)))
        label.pack() 
btn = Button(root, text = 'Click me !',command =Task1)
Quit = Button(root, text="Exit", fg="red", command=root.quit)

#output = Text(root, width=200, height=300)
btn.pack(padx=20, pady=8)
Quit.pack(padx=20, pady=18)
#output.pack()
root.mainloop()

"""#Task 1:---
import random 
count =  random.randint(10,20)
for x in range(count):

    number =  random.randint(1,60)
    print(x+1 ,":-" ,number)
    print("_________")
#Task2:---
import random 
count =  random.randint(10,20)
for x in range(count):
    
    
    number =  random.randint(1,60)
    star = "*"*number
    print(x+1,":-" ,number,   star) 

#Task3:--
import random
from statistics import mean 
count =  random.randint(10,20)
NumberList = []
for x in range(count):
    
    number =  random.randint(1,60)
    NumberList.append(number)
print(NumberList)
print("Min Value :-", min(NumberList))    
print("Min Value :-", max(NumberList))
print("Min Value :-", mean(NumberList))
"""
