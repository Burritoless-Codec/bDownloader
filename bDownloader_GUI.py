import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import webbrowser
import platform
from urllib.request import urlretrieve, urlopen
from urllib.parse import urlparse


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

        self.button_frame = tk.Frame(self.root)
        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)

        self.btn1 = tk.Button(self.button_frame, text='Download', command=self.process_lines)
        self.btn1.grid(row=0, column=0, sticky=tk.W + tk.E)
        self.btn2 = tk.Button(self.button_frame, text='View in explorer', command=show_explorer)
        self.btn2.grid(row=0, column=1, sticky=tk.W + tk.E)

        self.button_frame.pack(padx=5, pady=5, fill='x')

        self.btn3 = tk.Button(self.root, text='Github', command=github)
        self.btn3.pack(padx=5, pady=5, fill='x')

        self.root.mainloop()

    def process_lines(self):
        lines = self.url_text.get("1.0", "end").splitlines()
        urls = [url.strip() for url in lines]
        for url in urls:
            default_filename = get_default_filename(url)
            if default_filename:
                download_file(url, default_filename)
            else:
                print(f"Could not determine default filename for {url}.")


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
    elif platform.system() == 'Darwin':
        subprocess.Popen(['open', downloads_path])
    else:
        print('Unsupported operating system.')


def create_downloads_directory():
    if not os.path.exists('downloads'):
        os.mkdir('downloads')


def download_file(url, filename):
    save_path = f'downloads/{filename}'
    if os.path.exists(save_path):
        user_choice = ask_overwrite_dialog(filename)
        if user_choice == 'yes':
            try:
                urlretrieve(url, save_path)
                print(f"File downloaded successfully to '{save_path}'")
            except Exception as e:
                messagebox.showerror('Error', f'Error downloading file: {e}')
                print(f"Error downloading file: {e}")
        elif user_choice == 'no':
            new_filename = get_new_filename()
            if new_filename:
                download_file(url, new_filename)
        else:
            messagebox.showerror('Error', f'Invalid input')
            print('Invalid input.')
    else:
        try:
            urlretrieve(url, save_path)
            print(f"File downloaded successfully to '{save_path}'")
        except Exception as e:
            messagebox.showerror('Error', f'Error downloading file: {e}')
            print(f"Error downloading file: {e}")


def ask_overwrite_dialog(filename):
    user_choice = messagebox.askyesno("Overwrite Confirmation",
                                      f'The file "{filename}" already exists. Do you want to overwrite it?')
    return 'yes' if user_choice else 'no'


def get_default_filename(url):
    try:
        response = urlopen(url)
        disposition = response.headers.get('Content-Disposition')
        if disposition:
            parts = disposition.split(';')
            for part in parts:
                if part.strip().startswith('filename='):
                    return part.split('=')[1].strip().strip('"')
        parsed_url = urlparse(url)
        return os.path.basename(parsed_url.path)
    except Exception as e:
        messagebox.showerror('Error', f'Error getting default filename: {e}')
        print(f"Error getting default filename: {e}")
        return None


def get_new_filename():
    new_filename = None

    def set_new_filename():
        nonlocal new_filename
        new_filename = entry.get()
        root.destroy()

    root = tk.Tk()
    root.title("Enter New Filename")
    root.resizable(width=False, height=False)
    root.geometry('')

    label = tk.Label(root, text="Please enter a new filename:")
    label.pack(padx=10, pady=5)

    entry = tk.Entry(root, width=40)
    entry.pack(padx=10, pady=5)

    button = tk.Button(root, text="OK", command=set_new_filename)
    button.pack(padx=10, pady=5)

    root.mainloop()

    return new_filename.strip() if new_filename is not None else None


if __name__ == '__main__':
    GUI()
