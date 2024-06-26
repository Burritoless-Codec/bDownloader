# bDownloader

## Description
bDownloader is a GUI and command-line tool for bulk downloading files from URLs. It allows users to input URLs, manage downloads, and view downloaded files.

## Features
- GUI interface for easy URL input and download management.
- Supports viewing downloaded files in the file explorer.
- Command-line interface for quick batch downloads.

## Requirements
- Python 3.x
- tkinter (standard library)
- webbrowser (standard library)
- urllib (standard library)
- platform (standard library)
## Built and Tested
### Made with 
![Static Badge](https://img.shields.io/badge/Python-3.12-blue?style=flat-square)

### Tested on 
#### Windows
![Static Badge](https://img.shields.io/badge/Windows-10%2022H2-Green?style=flat-square)

#### Linux

 ![Static Badge](https://img.shields.io/badge/Debian-12-Green?style=flat-square) ![Static Badge](https://img.shields.io/badge/Ubuntu-24.04%20LTS-Green?style=flat-square)

I have found it necessary to install the Tkinter package (python3-tk) in order to enable the graphical user interface (GUI) functionality on my systems. This step may be specific to my setup, but it ensures proper functionality of the GUI-based application.
```bash
sudo apt-get update
sudo apt-get install python3-tk
```


## Installation
No installation is required. Simply run the script using Python.

## Usage
### GUI Mode
1. Launch the GUI by running the script.
2. Enter one URL per line in the text area.
3. Click the "Download" button to start downloading.
4. Use the "View in explorer" button to open the downloads folder.

### Command-line Mode
1. Run the script in the command line.
2. Enter URLs separated by commas when prompted.
3. Follow the on-screen instructions to manage downloads.

## Contributing
Contributions are welcome! Fork the repository, make your changes, and submit a pull request.

## License
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.


## Contact
For issues or inquiries, please contact [Burritoless-Codec](https://github.com/Burritoless-Codec).
