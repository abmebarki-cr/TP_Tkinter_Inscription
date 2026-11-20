# Formulaire d'Inscription - Université de Boumerdes

A modern, native Python desktop application for managing student registrations, built entirely with `tkinter`. Designed as an educational project (TP), it demonstrates modern UI principles without relying on external design libraries.

## Features
* **Modern UI:** Uses `ttk.Style("clam")`, custom hover events, and flat borders for a clean, contemporary look.
* **Photo Upload:** Browse and display a student profile picture with automatic downscaling to fit the UI canvas.
* **Data Validation:** Ensures required fields (Name, Surname, ID, Level) are filled before submission.
* **Real-time Data Table:** Displays all registered students in a scrollable `ttk.Treeview` spreadsheet grid.
* **Export to TXT:** Save the entire session's student registry to a formatted `.txt` file.

## Prerequisites
* Python 3.x installed.
* `tkinter` (included in standard Python distributions).

## Setup & Usage
1. Clone or download this repository.
2. Ensure `uni_logo.png` and `logo_fac.png` are in the exact same directory as the Python script.
3. If your file paths in the code are absolute (e.g., `C:\...`), update them to relative paths (e.g., `file="uni_logo.png"`) for portability across different computers.
4. Run the script:
   ```bash
   python tkin2.py
