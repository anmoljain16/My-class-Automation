
from tkinter import *
from datetime import datetime

from pyttsx3 import speak

from pyautogui import sleep
from pyautogui import write
from pyautogui import press
import webbrowser
from tkinter import messagebox
import time


window = Tk()
window.geometry('600x400')
entry_reg = Entry(window)
entry_pass = Entry(window, show='*')
entry_reg.place(x=300, y=100)
entry_pass.place(x=300, y=150)
label_reg = Label(window, text='Username').place(x=220, y=100)
label_pass = Label(window, text='Password').place(x=220, y=150)

hour = datetime.now().strftime("%I:%M %p")


def login():
    reg_no = entry_reg.get()
    passw = entry_pass.get()
    if reg_no == '' or passw == '':
        messagebox.showwarning("showwarning", "Please fill the credentials")
    else:
        frame = Frame(window, width=600, height=400)
        frame.place(x=0, y=0)
        print(reg_no)
        print(passw)
        var1 = IntVar()

    def myf():
        class_press = var1.get()
        print(class_press)

        def nextb():
            frame_2 = Frame(frame, width=600, height=400)
            frame_2.place(x=0, y=0)

            # frame_2.place(x=0, y=0)
            def takenow():
                sleep(1)
                webbrowser.open('https://myclass.lpu.in/')
                sleep(3)
                press('tab')
                write(reg_no)
                press('tab')
                sleep(1)
                write(passw)
                press('tab')
                press('enter')
                sleep(2)
                speak('I am in My class Platform Sir')
                sleep(0.5)

                speak('Going to Open meetings ')
                press('tab', presses=5)
                press('enter')

                sleep(2)
                press('tab', presses=5)
                sleep(0.5)

                press('tab', presses=5)
                sleep(0.5)

                press('tab', presses=4)
                sleep(1)

                press('tab', presses=class_press)
                sleep(1)
                press('Enter')
                sleep(1)
                press('enter')
                speak('Joining class in 3 seconds')

                press('tab')
                press('tab')
                sleep(1)
                press('enter')

                sleep(15)
                speak('I will join my class with listen only mode in 3 seconds')
                sleep(2)
                press('tab', presses=3)

                sleep(0.5)
                press('enter')
                sleep(5)

            def shedule():
                frame_shedule = Frame(frame_2, width=600, height=400)
                frame_shedule.pack()

                clicked = StringVar()
                clicked.set("09:00 AM")

                def time_set():
                    t_class = clicked.get()
                    print(t_class)
                    hour = datetime.now().strftime("%I:%M %p")

                    while t_class != hour:
                        hour = datetime.now().strftime("%I:%M %p")
                        time.sleep(1)
                    if t_class == hour:
                        webbrowser.open('https://myclass.lpu.in/')
                        sleep(3)
                        press('tab')
                        write(reg_no)
                        press('tab')
                        sleep(1)
                        write(passw)
                        press('tab')
                        press('enter')
                        sleep(2)
                        speak('I am in My class Platform Sir')
                        sleep(0.5)

                        speak('Going to Open meetings ')
                        press('tab', presses=5)
                        press('enter')

                        sleep(2)
                        press('tab', presses=5)
                        sleep(0.5)

                        press('tab', presses=5)
                        sleep(0.5)

                        press('tab', presses=4)
                        sleep(1)

                        press('tab', presses=class_press)
                        sleep(1)
                        press('Enter')
                        sleep(1)
                        press('enter')
                        speak('Joining class in 3 seconds')

                        press('tab')
                        press('tab')
                        sleep(1)
                        press('enter')

                        sleep(15)
                        speak('I will join my class with listen only mode in 3 seconds')
                        sleep(2)
                        press('tab', presses=3)

                        sleep(0.5)
                        press('enter')
                        sleep(5)

                drop = OptionMenu(window, clicked, "9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM",
                                  "3:00 PM", "4:00 PM", "5:00 PM")
                drop.place(x=200, y=60)

                button = Button(window, text='Enter', command=time_set, width=20)
                button.place(x=400, y=60)

            button_shedule = Button(frame_2, text='Shedule The Time', width=30, command=shedule)
            button_now = Button(frame_2, text='Take it now', width=30, command=takenow)
            button_now.place(x=210, y=250)
            button_shedule.place(x=210, y=130)

        button = Button(frame, text=">>Next>>", command=nextb)
        button.place(x=500, y=330)

    rb1 = Radiobutton(frame, text='1st', variable=var1, value=1, anchor='w', command=myf)
    rb1.place(x=200, y=60)
    rb2 = Radiobutton(frame, text='2nd', variable=var1, value=2, anchor='w', command=myf)
    rb2.place(x=200, y=120)
    rb3 = Radiobutton(frame, text='3rd', variable=var1, value=3, anchor='w', command=myf)
    rb3.place(x=200, y=180)
    rb4 = Radiobutton(frame, text='4th', variable=var1, value=4, anchor='w', command=myf)
    rb4.place(x=200, y=240)
    rb5 = Radiobutton(frame, text='5th', variable=var1, value=5, anchor='w', command=myf)
    rb5.place(x=200, y=300)




button_login = Button(window, text='Login', command=login)
button_login.place(x=300, y=250)

mainloop()
