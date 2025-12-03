# Auto-File-Organizer
A simple Python script to automatically organize files into folders based on their extensions.

# Auto File Organizer 📂

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python) ![License](https://img.shields.io/badge/License-MIT-green)

A simple and efficient Python script to organize messy directories by automatically sorting files into specific folders based on their extensions.

## 🚀 About The Project
This project is a system automation tool written in Python. It scans the current directory for specific file types (currently `.png` and `.jpg`) and moves them into a dedicated folder named **"Resimler"**. It helps in keeping the Downloads or Desktop folders clean and organized.

## ⚙️ Features
- **Automatic Detection:** Scans the directory where the script is located.
- **Folder Creation:** Automatically creates a target folder if it doesn't exist.
- **File Moving:** Safely moves files using the `shutil` library.
- **Scalable:** Easily expandable to support other file types like PDFs, documents, or videos.

## 🛠️ Built With
- [Python](https://www.python.org/)
- `os` module (Standard Library)
- `shutil` module (Standard Library)

## 💻 How to Use

1. **Clone the repository**
   ```bash
   git clone [https://github.com/HamidHan/Auto-File-Organizer.git](https://github.com/HamidHan/Auto-File-Organizer.git)
Navigate to the project directory

Bash

cd Auto-File-Organizer
Run the script

Bash

python main.py
Note: Make sure to place the script inside the folder you want to organize before running it.

📝 Code Overview
Here is the core logic of the script:

Python

# Checks if the file is an image
if dosya.endswith(".png") or dosya.endswith(".jpg"):
    # Moves the file to the target folder
    shutil.move(kaynak, hedef)
🔜 Future Improvements
[ ] Add support for Document files (.pdf, .docx, .txt).

[ ] Add a Graphical User Interface (GUI) using Tkinter.

[ ] Allow users to select the target folder path manually.

🤝 Contributing
Contributions are welcome! If you have any suggestions to make this better, please fork the repo and create a pull request.

Fork the Project

Create your Feature Branch

Commit your Changes

Push to the Branch

Open a Pull Request

📄 License
Distributed under the MIT License.
