# Fuzzy File Mover GUI

A Python GUI tool to **move files from one folder to another** based on filename similarity (fuzzy matching).  
Supports recursive scanning, adjustable similarity threshold, and ignoring file extensions.

<img width="737" height="641" alt="image" src="https://github.com/user-attachments/assets/f039997f-c89c-45aa-91da-7a2b165bc937" />


---

## Features

- Recursively scans **both source and destination folders** for files  
- Uses fuzzy string matching (via [`rapidfuzz`](https://github.com/maxbachmann/RapidFuzz)) to compare filenames  
- Adjustable similarity threshold slider (50% - 100%)  
- Option to ignore file extensions when comparing  
- Preview list of matched files before moving  
- One-click move operation with log output  

---

## Requirements

- Python 3.x  
- [`tkinter`](https://docs.python.org/3/library/tkinter.html) (for the GUI)  
- [`rapidfuzz`](https://pypi.org/project/rapidfuzz/) (for fuzzy matching)  

---

## Installation

### Fedora

- sudo dnf install python3-tkinter
- pip install rapidfuzz


### Other Linux distros / Windows / MacOS
- Install tkinter and pip appropriate for your system.
- Install rapidfuzz with pip:

---

## Usage
 1. Clone or download this repository.
 2. Open a terminal or command prompt and navigate to the folder containing the script.
 3. Run the GUI tool:

    python3 move_similar_files_gui.py
    
 4. In the GUI:

    - Select your Source Folder (A) and Destination Folder (B).

    - Adjust the Similarity Threshold slider as desired.

    - Check or uncheck Ignore File Extensions depending on your needs.

    - Click Preview Matches to view potential file moves.

    - Click Move Matched Files to execute the file transfer.

---

## License

This project is licensed under the GNU License. See the LICENSE file for details.

---

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests for improvements or bug fixes.

---

## Acknowledgments

  Thanks to rapidfuzz for providing efficient fuzzy string matching.

  Built using Python’s built-in tkinter for a lightweight and portable GUI.
    
