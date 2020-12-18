from PyDictionary import  PyDictionary
from PyDictionary import  *
from tkinter import *

root = Tk()
root.title('My Dictionary')
root.geometry('500x200')
root.resizable(width=False,height=False)


global word_in,tr_code,mean_wrd,syn_wrd,anto_wrd,trans_wrd



def word_inp():
    root.geometry('1000x200')
    root.resizable(width=False,height=False)
    dicto = PyDictionary()
    word_in = var1.get()
    tr_code = var2.get()
    mean_wrd =  dicto.meaning(word_in)
    syn_wrd = dicto.synonym(word_in)
    anto_wrd = dicto.antonym(word_in)
    trans_wrd = dicto.translate(word_in,tr_code)
    lab3 = Label(root,text='RESULTS',font=('liberation serif',20,'bold','italic'))
    lab3.place(x=660,y=0)
    lab4 = Text(root,bg ="powder blue",width = 30,height = 6,font=('arial',10))
    lab4.place(x=500,y=35)  
    lab4.insert(INSERT,mean_wrd)
    lab5 = Label(root,text=trans_wrd,bg ="light green", width = 30,font=('arial',10))
    lab5.place(x=750,y=35)
    lab6 = Label(root,text=f'\',\'.join({syn_wrd})',bg ="green yellow", width = 30,font=('arial',10))
    lab6.place(x=750,y=65)
    lab7 = Label(root,text=f'\',\'.join({anto_wrd})',bg ="lightblue4",width = 30, font=('arial',10))
    lab7.place(x=750,y=95)
    

    
##    insert(0,(f'The meaning of the {word_in} is {mean_wrd}'))
##    insert(0,(f'The translation of the \'{word_in}\' in \'{tr_code}\' is:-\t {trans_wrd}'))
##    insert(0,(f'\nThe synonym(s) of the \'{word_in}\' are:-\t ',','.join(syn_wrd)))
##    insert(0,(f'\nThe antonym(s) of the \'{word_in}\' are:-\t',','.join(anto_wrd)))



lab1 = Label(root,text='Enter the word',font=('arial',10))
lab1.place(x=0,y=45)
lab2 = Label(root,text='Enter the langage code',font=('arial',10))
lab2.place(x=0,y=90)
var1 = StringVar()
var2 = StringVar()
ent1 = Entry(root,textvariable=var1,font=('arial',10),bg='powder blue',bd=2,width=38)
ent1.place(x=160,y=45)
ent2 = Entry(root,textvariable=var2,font=('arial',10),bg='powder blue',bd=2,width=38)
ent2.place(x=160,y=90)





butt1= Button(root,text='Submit',command  = word_inp,width=15,font=('urw bookman',17))
butt1.place(x=160,y=140)






##mean_wrd =  dicto.meaning(word_in)
##syn_wrd = dicto.synonym(word_in)
##anto_wrd = dicto.antonym(word_in)
##trans_wrd = dicto.translate(word_in,tr_code)
##print(f'The meaning of the {word_in} is {mean_wrd} \n')
##print(f'The translation of the \'{word_in}\' in \'{tr_code}\' is:-\t {trans_wrd}\n')
##print(f'\nThe synonym(s) of the \'{word_in}\' are:-\t ',','.join(syn_wrd))
##print(f'\nThe antonym(s) of the \'{word_in}\' are:-\t',','.join(anto_wrd))


