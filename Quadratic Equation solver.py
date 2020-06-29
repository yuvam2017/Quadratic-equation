from tkinter import *
root = Tk()
root.title("Quadratic Equation Solver")
root.configure(bg="white")



##########################################  Physical Appearance  #############################################
Label(root,text="Enter the Equation : ",fg="red",bg="white",font="comicsansms 19 bold").grid(row=0,column=0,padx=10)
entry_xsquare = Entry(root,bd=2,justify=RIGHT)
Label(root,text=" x\u00b2  +  ",fg="black",bg="white",font="comicsansms 10 bold").grid(row=0,column=2)
entry_x = Entry(root,bd=2,justify=RIGHT)
Label(root,text=" x + ",fg="black",bg="white",font="comicsansms 10 bold").grid(row=0,column=4)
entry_constant = Entry(root,bd=2,justify=RIGHT)

Label(root,text="Roots are : ",fg="#ff0066",bg="white",font="comicsansms 15 bold",justify=CENTER).grid(row=1,column=0)

Button(root,text="Submit",bd=2,fg="red",font="comicsansms 10",justify=CENTER,command=lambda: solver(int(entry_xsquare.get()),int(entry_x.get()),int(entry_constant.get()))).grid(row=2,column=1,columnspan=2,sticky='ew')
Button(root,text="Reset",bd=2,fg="red",font="comicsansms 10",justify=CENTER,command=lambda: reset()).grid(row=2,column=3,columnspan=2,sticky='ew')
Button(root,text="Quit",bd=2,fg="red",font="comicsansms 10",justify=CENTER,command=root.destroy).grid(row=2,column=5,sticky='ew')

##############################################################################################################


#####################################  Placing on the screen #################################################
entry_xsquare.grid(row=0,column=1)
entry_x.grid(row=0,column=3)
entry_constant.grid(row=0,column=5,padx=10)


##############################################################################################################

#Functions
def solver(a,b,c):
     D = b**2-4*a*c
     print(D)
     if a != 0:
          if D>0:
               #((-b + D**0.5)/(2*a)),((-b - D**0.5)/(2*a))
               num1 = (-b + D**0.5)
               den = (2*a)
               if (num1//den)*den == num1:
                    firstroot = num1//den
                    num2 = (-b - D**0.5)
                    if (num2//den)*den == num2:
                         secondroot = num2//den
                    else:
                         secondroot = '{}/{}'.format(num2,den)
               else:
                    firstroot = '{}/{}'.format(num1,den)
                    if (num2//den)*den == num2:
                         secondroot = num2//den
                    else:
                         secondroot = '{}/{}'.format(num2,den)              
               answer = ' {} and {}  {}{}'.format(firstroot,secondroot,'Both roots are different and D=',D)
          elif D == 0:
               num = -b
               den = 2*a
               if (num//den)*den == num:
                    firstroot  = num//den
                    secondroot = num //den
               else:
                    firstroot = '{}/{}'.format(-b,2*a)
                    secondroot = '{}/{}'.format(-b,2*a)
               answer = ' {} and {}  {}'.format(firstroot,secondroot,'Both Roots are same')
          elif D <0:
               answer = 'No possible real roots as D is {} which is less than zero '.format(D)
     elif a == 0:
          num,den = -c,b
          if (num//den)*den == num:
               answer = ' {} '.format((-c//b))
          else:
               answer = ' {}/{} '.format(-c,b)
     Label(root,text=answer,fg="black",bg="white",font="comicsansms 10 ",justify=CENTER).grid(row=1,column=1,columnspan=3)
     
          
     
     
def reset():
     entry_xsquare.delete(0,END)
     entry_x.delete(0,END)
     entry_constant.delete(0,END)
     Label(root,text='                                                                                               ',fg="black",bg="white",font="comicsansms 10 ",justify=CENTER).grid(row=1,column=1,columnspan=3)
     
root.mainloop()
