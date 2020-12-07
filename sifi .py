
from tkinter import *
import tkinter.messagebox
import math


root=Tk()
root.title('Scifi calci')
root.configure(background="powder blue")
root.resizable(width=False,height=False)
root.geometry('495x550+0+0')

calc = Frame(root)
calc.grid()

class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value= True #please tell me why this is true
        self.check_sum=False #please tell me why this is false
        self.op = ''
        self.result = False #please tell me why this is false

    def numberEnter(self,num):
        self.result = False
        firstnum = txtdisplay.get()
        secnum = str(num)
        if self.input_value:
            self.current = secnum
            self.input_value = False
        else:
            if secnum == '.':
                if secnum in firstnum:
                    return
            self.current = firstnum + secnum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtdisplay.get())

    def display(self,value):
        txtdisplay.delete(0,END)
        txtdisplay.insert(0,value)

    def log(self):
        self.result = False
        self.current = math.log(float(txtdisplay.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(float(txtdisplay.get()))
        self.display(self.current)
      
    def clear(self):
       self.result = False
       length = len(self.current)-1
       self.current = self.current[0:length]
       self.display(self.current)

    def all_clear(self):
        self.result = False
        self.current = '0'
        self.display(self.current)

    def sqrt(self):
        self.result=False
        self.current = math.sqrt(float(txtdisplay.get()))
        self.display(self.current)

    def valid_function(self):
        if self.op == 'add':
            self.total += self.current
        if self.op == 'sub':
            self.total -= self.current
        if self.op == 'mul':
            self.total *= self.current
        if self.op == 'div':
            self.total /= self.current
        if self.op == 'mod':
            self.total %= self.current
        self.input_value =True
        self.check_sum = False
        self.display(self.total)

    def oper(self,op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        
        self.op = op
        self.result = False
    
    def cos(self):
        self.result = False
        self.current= math.cos(math.radians(float(txtdisplay.get())))
        self.display(self.current)
    
    def tan(self):
        self.result = False
        self.current= math.tan(math.radians(float(txtdisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current= math.sin(math.radians(float(txtdisplay.get())))
        self.display(self.current)

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def acosh(self):
        self.result = False
        self.current = math.acosh(math.radians(float(txtdisplay.get())))
        self.display(self.current)
    
    def asinh(self):
        self.result = False
        self.current = math.asinh(math.radians(float(txtdisplay.get())))
        self.display(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(txtdisplay.get())))
        self.display(self.current)

    def log10(self):
        self.result= False
        self.current = math.log10(float(txtdisplay.get()))
        self.display(self.current)
    
    def log1p(self):
        self.result= False
        self.current = math.log1p(float(txtdisplay.get()))
        self.display(self.current)
    
    def lgama(self):
        self.result= False
        self.current = math.lgamma(float(txtdisplay.get()))
        self.display(self.current)
    
    def expm1(self):
        self.result= False
        self.current = math.expm1(float(txtdisplay.get()))
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtdisplay.get())))
        self.display(self.current)
    
    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(txtdisplay.get())))
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(float(txtdisplay.get()))
        self.display(self.current)

    def deg(self):
        self.result = False
        self.current = math.degrees(float(txtdisplay.get()))
        self.display(self.current)
    
    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def pm(self):
        self.result = False
        self.current = - (float(txtdisplay.get()))
        self.diplay(self.current)



added_value = Calc()

txtdisplay = Entry(calc,font=('arial',20,'bold'),bg='powder blue',bd=30,width=28,justify = RIGHT)
txtdisplay.grid(row = 0,column=0,columnspan=4,pady=1)
txtdisplay.insert(0,0)
numpad = '789456123'
i=0
btn=[]
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc,text = numpad[i],font =('arial',20,'bold'), width=6,height = 2,bd = 4))
        btn[i].grid(row=j,column=k)
        btn[i]['command']=lambda x= numpad [i] : added_value.numberEnter(x)
        i+=1

#=================================Standard Buttons=================================

btnclear = Button(calc,text=chr(67),font =('arial',20,'bold'), width=6,height = 2,bd = 4,command = added_value.clear,bg='pink').grid(row=1,column=0)#ascii charater used here
btnallclear = Button(calc,text=chr(67)+chr(69),font =('arial',20,'bold'), width=6,height = 2,bd = 4,bg='pink',command = added_value.all_clear).grid(row=1,column=1)
btnsqrt = Button(calc,text='SQRT',font =('arial',20,'bold'), width=6,command=added_value.sqrt  ,height = 2,bd = 4,bg='pink').grid(row=1,column=2)
btnadd = Button(calc,text='+',font =('arial',20,'bold'), width=6,height = 2,command=lambda : added_value.oper('add'),bd = 4,bg='pink').grid(row=1,column=3)

btnsub = Button(calc,text='-',font =('arial',20,'bold'), width=6,height = 2,command=lambda : added_value.oper('sub'),bd = 4,bg='pink').grid(row=2,column=3)
btnmul = Button(calc,text='*',font =('arial',20,'bold'), width=6,height = 2,bd = 4,command=lambda : added_value.oper('mul'),bg='pink').grid(row=3,column=3)
btdiv = Button(calc,text=chr(247),font =('arial',20,'bold'), width=6,height = 2,bd = 4,command=lambda : added_value.oper('div'),bg='pink').grid(row=4,column=3)
btnzero = Button(calc,text='0',font =('arial',20,'bold'), width=6,height = 2,bd = 4,bg='pink', command=lambda : added_value.numberEnter(0)).grid(row=5,column=0)

btndec = Button(calc,text='.',font =('arial',20,'bold'), width=6,height = 2,bd = 4,command=lambda : added_value.numberEnter('.'),bg='pink').grid(row=5,column=1)
btnpm = Button(calc,text=chr(177),font =('arial',20,'bold'), width=6,height = 2,command = added_value.pm,bd = 4,bg='pink').grid(row=5,column=2)
btneql = Button(calc,text='=',font =('arial',20,'bold'), width=6,height = 2,command=added_value.sum_of_total,bd = 4,bg='pink').grid(row=5,column=3)

#==============================Scientific Buttons====================================

btnpi = Button(calc,text='PI',font =('arial',20,'bold'),command=added_value.pi,width=6,height = 2,bd = 4,bg='light green').grid(row=1,column=4)
btncos = Button(calc,text='cos',font =('arial',20,'bold'), width=6,command = added_value.cos,height = 2,bd = 4,bg='light green').grid(row=1,column=5)
btnsin = Button(calc,text='sin',font =('arial',20,'bold'), width=6,command = added_value.sin,height = 2,bd = 4,bg='light green').grid(row=1,column=6)
btntan = Button(calc,text='tan',font =('arial',20,'bold'), width=6,height = 2,command = added_value.tan,bd = 4,bg='light green').grid(row=1,column=7)

btn2pi = Button(calc,text='2PI',font =('arial',20,'bold'), width=6,command=added_value.tau,height = 2,bd = 4,bg='light green').grid(row=2,column=4)
btncsoh = Button(calc,text='cosh',font =('arial',20,'bold'), width=6,height = 2,command = added_value.cosh,bd = 4,bg='light green').grid(row=2,column=5)
btnsinh = Button(calc,text='sinh',font =('arial',20,'bold'), width=6,height = 2,command = added_value.sinh,bd = 4,bg='light green').grid(row=2,column=6)
btntanh = Button(calc,text='tanh',font =('arial',20,'bold'), width=6,command = added_value.tanh,height = 2,bd = 4,bg='light green').grid(row=2,column=7)

btnlog = Button(calc,text='log',font =('arial',20,'bold'), width=6,command = added_value.log,height = 2,bd = 4,bg='light green').grid(row=3,column=4)
btnexp = Button(calc,text='Exp',font =('arial',20,'bold'), width=6,height = 2,bd = 4,command = added_value.exp,bg='light green').grid(row=3,column=5)
btnmod = Button(calc,text='Mod',font =('arial',20,'bold'), width=6,height = 2, command =  lambda: added_value.oper('mod'),bd = 4,bg='light green').grid(row=3,column=6)
btnE = Button(calc,text='e',font =('arial',20,'bold'), width=6,command=added_value.e,height = 2,bd = 4,bg='light green').grid(row=3,column=7)

btnlog2 = Button(calc,text='log2',font =('arial',20,'bold'), width=6,height = 2,command = added_value.log2,bd = 4,bg='light green').grid(row=4,column=4)
btnacosh = Button(calc,text='acosh',font =('arial',20,'bold'), command = added_value.acosh,width=6,height = 2,bd = 4,bg='light green').grid(row=4,column=5)
btnasinh = Button(calc,text='asinh',font =('arial',20,'bold'), width=6,height = 2,command = added_value.asinh,bd = 4,bg='light green').grid(row=4,column=6)
btndeg = Button(calc,text='deg',font =('arial',20,'bold'), width=6,height = 2,command = added_value.deg,bd = 4,bg='light green').grid(row=4,column=7)

btnlog10 = Button(calc,text='log10',font =('arial',20,'bold'), width=6,command = added_value.log10,height = 2,bd = 4,bg='light green').grid(row=5,column=4)
btnlog1p = Button(calc,text='log1p',font =('arial',20,'bold'), width=6,command = added_value.log1p,height = 2,bd = 4,bg='light green').grid(row=5,column=5)
btnexpm1 = Button(calc,text='expm1',font =('arial',20,'bold'), width=6,command = added_value.expm1,height = 2,bd = 4,bg='light green').grid(row=5,column=6)
btnlgamma = Button(calc,text='lgamma',font =('arial',20,'bold'), width=6,command = added_value.lgama,height = 2,bd = 4,bg='light green').grid(row=5,column=7)

#========================================================================================================

label = Label(calc,text= 'SCIENTIFIC CALCULATOR',font =('arial',20,'bold'),justify=CENTER).grid(row=0,column=4,columnspan = 4)

#=================================Menu & Functions===========================
def iexit():
    iexit=tkinter.messagebox.askyesno('Scifi Calci','Do you want to quit')
    if iexit==1:
        root.destroy()
def scientific():
    root.resizable(width=False,height=False)
    root.geometry('1000x568+0+0')

def standard():
    root.resizable(width=False,height=False)
    root.geometry('495x568+0+0')

menubar = Menu(calc)
filemenu = Menu(menubar,tearoff= 0)
menubar.add_cascade(label="File",menu = filemenu)
filemenu.add_command(label='Standard',command=standard)
filemenu.add_command(label='Scifi',command = scientific)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=iexit)

editmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu = editmenu)
editmenu.add_command(label='Copy')
editmenu.add_command(label='Cut')
editmenu.add_command(label='Paste')

helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu = helpmenu)
helpmenu.add_command(label='View Help')

root.config(menu=menubar)
root,mainloop()
