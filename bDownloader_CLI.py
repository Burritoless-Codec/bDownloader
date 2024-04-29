from urllib.request import urlretrieve, urlopen
import os
from urllib.parse import urlparse


def main():
    create_downloads_directory()
    urls_input = input('Enter URLs (comma-separated): ')
    urls = [url.strip() for url in urls_input.split(',')]

    for url in urls:
        default_filename = get_default_filename(url)
        if default_filename:
            download_file(url, default_filename)
        else:
            print(f"Could not determine default filename for {url}.")


def create_downloads_directory():
    if not os.path.exists('downloads'):
        os.mkdir('downloads')


def download_file(url, filename):
    save_path = f'downloads/{filename}'
    if os.path.exists(save_path):
        while True:
            user_choice = input(f'The file "{filename}" already exists. Do you want to overwrite it? (Y/n): ').lower()
            if user_choice == 'y':
                break
            elif user_choice == 'n':
                new_filename = get_new_filename()
                download_file(url, new_filename)
                return
            else:
                print('Invalid input. Please enter Y or n.')

    try:
        urlretrieve(url, save_path)
        print(f"File downloaded successfully to '{save_path}'")
    except Exception as e:
        print(f"Error downloading file: {e}")


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
        print(f"Error getting default filename: {e}")
        return None


def get_new_filename():
    while True:
        new_filename = input("Please enter a new filename: ")
        save_path = f'downloads/{new_filename}'
        if os.path.exists(save_path):
            print("File already exists. Please choose a different filename.")
        else:
            return new_filename


if __name__ == '__main__':
    main()
