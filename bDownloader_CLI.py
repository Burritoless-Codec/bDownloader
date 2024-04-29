from urllib.request import urlretrieve
import os


def main():
    create_downloads_directory()
    urls_input = input('Enter URLs (comma-separated): ')
    filenames_input = input('Enter filenames (comma-separated): ')

    urls = [url.strip() for url in urls_input.split(',')]
    filenames = [filename.strip() for filename in filenames_input.split(',')]

    if len(urls) != len(filenames):
        print("Number of URLs and filenames must be the same.")
        return

    for url, filename in zip(urls, filenames):
        if filename == '':
            filename = input(f"Please enter a filename for URL '{url}': ")

        download_file(url, filename)


def create_downloads_directory():
    if not os.path.exists('downloads'):
        os.mkdir('downloads')


def download_file(url, filename):
    save_path = f'downloads/{filename}'
    if os.path.exists(save_path):
        while True:
            user_choice = input('The file already exists. Do you want to overwrite it? (Y/n): ').lower()
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
