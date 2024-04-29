import tkinter as tk
import subprocess
import os
import webbrowser
import platform


class GUI:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title('bDownloader GUI')
        self.root.resizable(width=False, height=False)
        self.root.geometry('')

        self.label_1 = tk.Label(self.root, text='Urls: Only 1 entry per line.', font=15)
        self.label_1.pack(anchor=tk.W, padx=10)

        self.v = tk.Scrollbar(self.root, orient='vertical')
        self.v.pack(side='right', fill='y')

        self.url_text = tk.Text(self.root, height=8, yscrollcommand=self.v.set)
        self.v.config(command=self.url_text.yview)
        self.url_text.pack(padx=10, fill='both')

        # self.label_2 = tk.Label(self.root, text='Filenames: Only 1 entry per line.', font=15)
        # self.label_2.pack(anchor=tk.W, padx=10)

        #self.filename_text = tk.Text(self.root, height=5)
        #self.filename_text.pack(padx=10)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)

        self.btn1 = tk.Button(self.button_frame, text='Download')
        self.btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
        self.btn2 = tk.Button(self.button_frame, text='View in explorer', command=show_explorer)
        self.btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

        self.button_frame.pack(padx=5, pady=5, fill='x')

        self.btn3 = tk.Button(self.root, text='Github', command=github)
        self.btn3.pack(padx=5, pady=5, fill='x')

        self.root.mainloop()


def github():
    webbrowser.open('https://github.com/Burritoless-Codec/bDownloader', new=2)


def show_explorer():
    downloads_path = os.path.join(os.getcwd(), 'downloads')

    if platform.system() == 'Windows':
        subprocess.Popen(f'explorer /enter,"{downloads_path}"')
    elif platform.system() == 'Linux':
        try:
            subprocess.Popen(['xdg-open', downloads_path])
        except FileNotFoundError:
            print(
                'Failed to open file manager.')
    elif platform.system() == 'Darwin':  # macOS
        subprocess.Popen(['open', downloads_path])
    else:
        print('Unsupported operating system.')


def create_downloads_directory():
    if not os.path.exists('downloads'):
        os.mkdir('downloads')


if __name__ == '__main__':
    GUI()
