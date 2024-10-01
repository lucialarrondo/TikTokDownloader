#Modules
from tkinter import*
import pyktok as pyk
from tkinter import messagebox

#We create the main window
mw=Tk()
mw.geometry('700x600')
mw.title('TikTok Downloader')
mw.config(bg='salmon4')

#Heading of the window
headingFrame=Frame(mw,bg='salmon4',bd=5)
headingFrame.place(relx=0.15,rely=0.05,relwidth=0.7,relheight=0.1)
headingLabel=Label(headingFrame,text='TikTok Downloader',bg='white',font=('Times',20,'bold'))
headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

#Taking the input of the url
Frame1=Frame(mw,bg='salmon4')
Frame1.place(relx=0.1,rely=0.15,relwidth=0.7,relheight=0.3)
label1=Label(Frame1,text='Enter the URL (must be from firefox): ',bg='salmon4',fg='white',font=('Times',12))
label1.place(relx=0.05,rely=0.2,relheight=0.08)
link=Entry(Frame1,font=('Times 12'))
link.place(relx=0.05,rely=0.3,relwidth=1,relheight=0.2)

#Function that download the video and saves it
def Downloader():
    pyk.specify_browser('firefox')
    pyk.save_tiktok(link.get(),True,'data.csv')
    messagebox.showinfo('TikTok Downloader', 'The TikTok is saved successfully')

#We create the button that calls the Downloader function
button=Button(mw,text='Download',font='Times 12',bg='salmon4',fg='white',padx=2,command=Downloader)
button.place(relx=0.35,rely=0.9,relwidth=0.25,relheight=0.05)

mw.mainloop()