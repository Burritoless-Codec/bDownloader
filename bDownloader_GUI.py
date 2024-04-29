import tkinter as tk
import subprocess
import os

class GUI:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title('bDownloader GUI')
        self.root.resizable(width=False, height=False)
        self.root.geometry('600x290')

        self.label_1 = tk.Label(self.root, text='Urls: Only 1 entry per line.', font=15)
        self.label_1.pack(anchor=tk.W, padx=10)

        self.url_text = tk.Text(self.root, height=5)
        self.url_text.pack(padx=10)

        self.label_2 = tk.Label(self.root, text='Filenames: Only 1 entry per line.', font=15)
        self.label_2.pack(anchor=tk.W, padx=10)

        self.filename_text = tk.Text(self.root, height=5)
        self.filename_text.pack(padx=10)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)

        self.btn1 = tk.Button(self.button_frame, text='Download')
        self.btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
        self.btn2 = tk.Button(self.button_frame, text='View in explorer', command=show_explorer)
        self.btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

        self.button_frame.pack(padx=5, pady=5, fill='x')

        self.btn3 = tk.Button(self.root, text='Github', command=self.github)
        self.btn3.pack(padx=5, pady=5, fill='x')

        self.root.mainloop()

    def github(self):
        os.system("start \"\" https://github.com/Burritoless-Codec/bDownloader")


def show_explorer():
    create_downloads_directory()
    cwd = os.getcwd()
    subprocess.Popen(f'explorer /enter,"{cwd}\\downloads"')


def create_downloads_directory():
    if not os.path.exists('downloads'):
        os.mkdir('downloads')


if __name__ == '__main__':
    GUI()
