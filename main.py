import tkinter as tk

from frontend.login_screen import LoginScreen


def main(): 
    root = tk.Tk()
    app = LoginScreen(root)
    root.mainloop()


if __name__ == '__main__':
    main()