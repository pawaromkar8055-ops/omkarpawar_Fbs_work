import tkinter as tk
r=tk.Tk()
r.title("Mumbai In")
r.geometry("500x400")

# l1=tk.Label(r,text='Rohit Sharma On Top ladali metraa',bg="Blue",fg="white",font=("Comic Sans MS",18))
# l2=tk.Label(r,text='Rohit ',bg="Blue",fg="white",font=("Comic Sans MS",18))
# l3=tk.Label(r,text=' On Top ',bg="Blue",fg="white",font=("Comic Sans MS",18))
# l4=tk.Label(r,text='ladali metraa',bg="Blue",fg="white",font=("Comic Sans MS",18))

# l1.pack(side="top")
# l2.pack(side="bottom")
# l3.pack(side="right")
# l4.pack(side="left")

# tk.Label(r,text="Enter your name").pack()
# e=tk.Entry(r)
# e.pack()
# l2=tk.Label(r,text="",bg="Blue",fg="White",font=("Comic Sans MS",18))
# l2.pack()
# def show():
#     r=e.get()
#     print(r)
#     l2.config(text=r)
# btn=tk.Button(r,text="Submit",command=show)
# btn.pack()

# tk.Label(r,text="Rohit",bg="Blue",font=("Comic Sans Ms",18)).grid(row=1,column=1)
# tk.Label(r,text="Rohit",bg="Blue",font=("Comic Sans Ms",18)).grid(row=2,column=1)
# tk.Label(r,text="Rohit",bg="Blue",font=("Comic Sans Ms",18)).grid(row=2,column=2)

tk.Label(r,text="Rohit",bg="Blue",font=("Comic Sans Ms",18)).place(x=40,y=30)
tk.Label(r,text="Rohit",bg="Blue",font=("Comic Sans Ms",18)).place(x=140,y=150)
tk.Label(r,text="Rohit",bg="Blue",font=("Comic Sans Ms",18)).place(x=96,y=58)
r.mainloop()