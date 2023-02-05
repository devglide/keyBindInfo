import tkinter as tk



'''
def key_press(evt):
    if evt.keycode==3145753:
        print('Shift+Tab is pressed')

root = tk.Tk()
root.bind("<Key>", key_press)
root.mainloop()
'''

def key_press(evt):
    print(evt)

root = tk.Tk()
root.bind("<Key>", key_press)
root.mainloop()