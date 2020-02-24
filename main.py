import random
import tkinter as tk


def generate_password(num):
    chars = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%*'
    password = ''
    try:
        num_int = int(num)
    except ValueError:
        password_text['text'] = 'Please enter a valid number'
        clear_text()
    for x in range(num_int):
        password = password + random.choice(chars)
    password_text['text'] = password
    clear_text()


def clear_text():
    entry.delete(0, 'end')


root = tk.Tk()

root.geometry('300x250')
root.title('Password Generator')
root.config(bg='#000000')
root.bind('<Return>', lambda event: generate_password(entry.get()))

left_label = tk.Label(root, text='Enter # of characters:',
                      font=(None, 15), fg='white', bg='#000000')
left_label.grid(row=1, column=1)

entry = tk.Entry(root, font=(None, 15), width=4, fg='black', bd=0)
entry.grid(row=1, column=2)

button = tk.Button(root, text='Go', height=1, bd=3,
                   command=lambda: generate_password(entry.get()))
button.grid(row=1, column=3)

frame = tk.Frame(root, bd=10, bg='#5387B6')
frame.place(relx=0.5, rely=0.15, relwidth=0.75, relheight=0.4, anchor='n')

password_text = tk.Label(
    frame, text='Your Password will be here', bg='#5387B6', font=(None, 12))
password_text.place(relx=0.5, rely=0.3, anchor='n')

quit_button = tk.Button(root, text='Quit', command=quit)

entry.focus()
root.mainloop()
