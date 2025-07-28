import os
import shutil
import tkinter as tk
from tkinter import filedialog, scrolledtext, ttk
from rapidfuzz import fuzz

match_results = []

def get_name(filename, ignore_ext):
    return os.path.splitext(filename)[0] if ignore_ext else filename

def get_all_files_recursive(folder):
    """Returns a list of all file paths inside a folder, recursively."""
    all_files = []
    for root, _, files in os.walk(folder):
        for f in files:
            full_path = os.path.join(root, f)
            all_files.append(full_path)
    return all_files

def preview_matches(source_folder, destination_folder, treeview, log_output, threshold, ignore_extensions):
    global match_results
    match_results.clear()
    treeview.delete(*treeview.get_children())

    if not os.path.isdir(source_folder) or not os.path.isdir(destination_folder):
        log_output.insert(tk.END, "Invalid source or destination folder.\n")
        return

    source_paths = get_all_files_recursive(source_folder)
    dest_paths = get_all_files_recursive(destination_folder)

    for src_path in source_paths:
        if not os.path.isfile(src_path):
            continue
        src_file = os.path.basename(src_path)
        src_name = get_name(src_file, ignore_extensions)

        for dst_path in dest_paths:
            dst_file = os.path.basename(dst_path)
            dst_name = get_name(dst_file, ignore_extensions)
            score = fuzz.partial_ratio(src_name, dst_name)

            if score >= threshold:
                match_results.append((src_path, dst_file, score))
                treeview.insert("", "end", values=(src_file, dst_file, score))
                break

    if not match_results:
        log_output.insert(tk.END, "No similar files found.\n")
    else:
        log_output.insert(tk.END, f"Found {len(match_results)} potential matches.\n")

def move_previewed_matches(destination_folder, log_output):
    moved = 0
    for src_path, dst_file, score in match_results:
        src_file = os.path.basename(src_path)
        dst_path = os.path.join(destination_folder, src_file)
        if os.path.exists(src_path):
            shutil.move(src_path, dst_path)
            log_output.insert(tk.END, f"Moved '{src_file}' (matched '{dst_file}', score: {score})\n")
            moved += 1
    if moved == 0:
        log_output.insert(tk.END, "No files were moved.\n")
    else:
        log_output.insert(tk.END, f"\nTotal files moved: {moved}\n")

def browse_folder(entry_field):
    folder = filedialog.askdirectory()
    if folder:
        entry_field.delete(0, tk.END)
        entry_field.insert(0, folder)

def run_preview():
    log_output.delete(1.0, tk.END)
    threshold = similarity_slider.get()
    ignore_ext = ignore_ext_var.get()
    preview_matches(source_entry.get(), dest_entry.get(), match_tree, log_output, threshold, ignore_ext)

def run_move():
    move_previewed_matches(dest_entry.get(), log_output)

# GUI setup
root = tk.Tk()
root.title("Fuzzy File Matcher (Recursive Both Folders)")

# Folder selectors
tk.Label(root, text="Source Folder (A):").grid(row=0, column=0, sticky='e')
source_entry = tk.Entry(root, width=50)
source_entry.grid(row=0, column=1)
tk.Button(root, text="Browse", command=lambda: browse_folder(source_entry)).grid(row=0, column=2)

tk.Label(root, text="Destination Folder (B):").grid(row=1, column=0, sticky='e')
dest_entry = tk.Entry(root, width=50)
dest_entry.grid(row=1, column=1)
tk.Button(root, text="Browse", command=lambda: browse_folder(dest_entry)).grid(row=1, column=2)

# Threshold slider
tk.Label(root, text="Similarity Threshold (%):").grid(row=2, column=0, sticky='e')
similarity_slider = tk.Scale(root, from_=50, to=100, orient=tk.HORIZONTAL, length=200)
similarity_slider.set(80)
similarity_slider.grid(row=2, column=1)

# Ignore extensions checkbox
ignore_ext_var = tk.BooleanVar()
ignore_ext_check = tk.Checkbutton(root, text="Ignore File Extensions", variable=ignore_ext_var)
ignore_ext_check.grid(row=2, column=2, sticky='w')

# Buttons
tk.Button(root, text="Preview Matches", command=run_preview, bg='blue', fg='white').grid(row=3, column=0, pady=10)
tk.Button(root, text="Move Matched Files", command=run_move, bg='green', fg='white').grid(row=3, column=2, pady=10)

# Treeview for preview
columns = ("Source File", "Matched Destination File", "Match Score")
match_tree = ttk.Treeview(root, columns=columns, show="headings", height=10)
for col in columns:
    match_tree.heading(col, text=col)
    match_tree.column(col, width=200)
match_tree.grid(row=4, column=0, columnspan=3, padx=10)

# Log output
log_output = scrolledtext.ScrolledText(root, width=70, height=10)
log_output.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()

