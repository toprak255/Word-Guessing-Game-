
import ttkbootstrap as tk
import json
from random import randint

body = tk.Window(themename="solar",title="kelime oyunu")

#==============
with open("turkish_words.json","rb") as i: 
    wordlist_json=i.read()
    wordlist=json.loads(wordlist_json)
#==============
mid=0.5
#==============
hexagon="⬢"
hexposition=[]
word=[]
temp_usedletter=[]
usedletters=[]

#==============

#==============
def bum():
    for widget in body.winfo_children():
        widget.destroy()
def letterinput():
    global m_entry
    revealbtn=tk.Button(body,text="Reveal Word",command=revealword).place(relx=.9,rely=.95,anchor="center")
    m_entry=tk.Entry(body,justify="center")
    m_entry.place(relx=.5,rely=.5,anchor="center",relwidth=.1)
    btn=tk.Button(body,text="Send",command=l_check)
    btn.place(relx=.5,rely=.58,anchor="center")
def nextword():
    tk.Button(body,text="Skip",style="darkly",command=newword).place(relx=.95,rely=.95,anchor="center")
def newword():
    global hexagon
    global hexposition
    global word
    global mid
    global wordlist
    global coock
    bum()
    letterinput()
    nextword()
    mid=0.5
    kelime=wordlist[randint(0,len(wordlist))]
    # coock=tk.Labelframe(body,text="Used Letters",style="success")   
    # coock.place(relx=.2,rely=.1,anchor="center",relheight=.13,relwidth=.35)
    word=[]
    hexposition=[]
    klengt=len(kelime)
    for i in kelime:
        word.append(i)
    if(klengt %2)==0:
        mid+=0.02
        mid-=(klengt/2*0.04)
    elif (klengt%2)==1:
        mid-=((klengt-1)/2)*0.04
    for i in kelime:
        x=tk.Label(text=hexagon,font=("Ariel", 50),foreground="#ffffff")
        if i == " ":
            hexposition.append(mid)
            mid+=0.04
        else:
            x.place(relx=mid,rely=.7,anchor="center")
        
            hexposition.append(mid)
            mid+=0.04
def revealword():
        global word
        for i in range(len(word)):
            if word[i]!=" ":
                abc = tk.Label(text=word[i].upper(),font=("Ariel", 19),foreground=body['bg'],background="#ffffff")
                abc.place(relx=hexposition[i],rely=.7,anchor="center")   
def l_check():
    global temp_usedletter
    global word
    global m_entry
    global usedletters
    global coock
    x=0
    if len(m_entry.get()) > 1:
        m_entry.delete(0, tk.END)
    else:
        bigL=m_entry.get()
        for i in range(len(word)):
            if word[i].lower()==bigL.lower() and bigL.lower()!=" ":
                abc = tk.Label(text=word[i].upper(),font=("Ariel", 19),foreground=body['bg'],background="#ffffff")
                abc.place(relx=hexposition[i],rely=.7,anchor="center")
                m_entry.delete(0, tk.END)
            elif bigL.lower()!=" " and bigL.lower()!="":
                # for i in range(len(word)):
                #     if word[i] in temp_usedletter:
                #         x+=1
                #         pass
                #     elif
                #         x+=1
                #             temp_usedletter.append(bigL)
                #             usedletters.insert(0,bigL.upper())
                #             print(usedletters)           
                #             usedL_label=tk.Label(coock,text=usedletters)        
                m_entry.delete(0, tk.END)
                

     
newword()



body.minsize(1600,500)

body.mainloop()