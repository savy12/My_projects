import pyshorteners
from tkinter import *

root  = Tk()
root.title('URL Shortener')
root.geometry('500x200')
root.resizable(width=False,height=False)
lab1 = Label(root,text='Enter URL',font=('arial',10))
lab1.place(x=0,y=45)
var1 = StringVar()
var2 = StringVar()
ent1 = Entry(root,textvariable=var1,font=('arial',10),bg='powder blue',bd=2,width=38)
ent1.place(x=115,y=45)


def short_link():
    global shorten_URL
    var = var1.get()
    s= pyshorteners.Shortener(api_key = '15110e36b0614512ef665bd10444077cb9f54b33')
    shorten_URL = s.bitly.short(var)
    ent2.insert(0,shorten_URL)

def no_click():
    global no_of_click
    s= pyshorteners.Shortener(api_key = '15110e36b0614512ef665bd10444077cb9f54b33')
    no_of_click  = s.bitly.total_clicks(shorten_URL)
    lab3 = Label(root,text = no_of_click,font=('arial',10))
    lab3.place(x=350,y=115)
    


lab2 = Label(root,text='Short URL',font=('arial',10))
lab2.place(x=0,y=75)
ent2 = Entry(root,font=('arial',10),textvariable=var2,bg='powder blue',bd=2,width=38)
ent2.place(x=115,y=75)
butt1= Button(root,text='create short link',width=15,command = short_link,font=('arial',10))
butt1.place(x=50,y=115)
butt2= Button(root,text='No of clicks',command = no_click,width=15,font=('arial',10))
butt2.place(x=200,y=115)
