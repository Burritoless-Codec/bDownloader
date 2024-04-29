from urllib.request import urlretrieve
import os



def main():
    url = str(input('Enter URL: '))
    filename = str(input('Save file as: '))
    dir_exists('downloads')
    savepath = (f'downloads/{filename}')
    urlretrieve(url, savepath)


def dir_exists(path):
    if not os.path.exists(path):
        os.mkdir(path)
    return path

if __name__ == '__main__':
    main()
