import os
import zipfile
import tempfile
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from bs4 import BeautifulSoup
import json
import math

def extract_usernames_from_html(file_path):
    with open(file_path, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        usernames = [a.text.strip() for a in soup.find_all("a")]
        return set(usernames)

def extract_usernames_from_json(file_path):
    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)
        usernames = set()
        if isinstance(data, list):
            for entry in data:
                if isinstance(entry, dict) and "string_list_data" in entry:
                    for item in entry["string_list_data"]:
                        usernames.add(item.get("value", "").strip())
        elif isinstance(data, dict):
            for key in data:
                if isinstance(data[key], list):
                    for entry in data[key]:
                        if isinstance(entry, dict) and "value" in entry:
                            usernames.add(entry["value"].strip())
        return usernames

def find_file(filenames, root_dir="."):
    for dirpath, _, files in os.walk(root_dir):
        for filename in filenames:
            if filename in files:
                return os.path.join(dirpath, filename)
    return None

def extract_usernames(file_path):
    if file_path.endswith(".html"):
        return extract_usernames_from_html(file_path)
    elif file_path.endswith(".json"):
        return extract_usernames_from_json(file_path)
    else:
        return set()

def find_non_followers(following_file, followers_file):
    following = extract_usernames(following_file)
    followers = extract_usernames(followers_file)
    not_following_back = following - followers
    return list(not_following_back)

def process_zip(zip_path):
    with tempfile.TemporaryDirectory() as temp_dir:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
        following_names = ["following.html", "following.json"]
        followers_names = ["followers.html", "followers_1.html", "followers.json", "followers_1.json"]
        pending_names = ["pending_follow_requests.html", "pending_follow_requests.json"]
        following_file = find_file(following_names, temp_dir)
        followers_file = find_file(followers_names, temp_dir)
        pending_file = find_file(pending_names, temp_dir)
        if not following_file or not followers_file:
            return None, None, None, "Could not find both following and followers files in the ZIP."
        non_followers = find_non_followers(following_file, followers_file)
        pending_requests = []
        if pending_file:
            pending_requests = list(extract_usernames(pending_file))
        return non_followers, pending_requests, (following_file, followers_file, pending_file), None

def format_columns(items, num_columns=3, col_width=30):
    if not items:
        return ""
    rows = math.ceil(len(items) / num_columns)
    columns = []
    for i in range(num_columns):
        columns.append(items[i*rows:(i+1)*rows])
    lines = []
    for row in range(rows):
        line = ""
        for col in range(num_columns):
            if row < len(columns[col]):
                line += columns[col][row].ljust(col_width)
            else:
                line += " " * col_width
        lines.append(line.rstrip())
    return "\n".join(lines)

def show_result_window(non_followers, pending_requests):
    result_window = tk.Toplevel()
    result_window.title("Instagram Analysis Result")
    result_window.geometry("700x600")

    label1 = tk.Label(result_window, text="People you follow who don't follow you back:", font=("Arial", 12, "bold"))
    label1.pack(pady=(10, 0))

    text1 = scrolledtext.ScrolledText(result_window, width=90, height=15, font=("Consolas", 10))
    text1.pack(padx=10, pady=(0, 10))
    if non_followers:
        text1.insert(tk.END, format_columns(sorted(non_followers)))
    else:
        text1.insert(tk.END, "Everyone you follow follows you back!")
    text1.configure(state='disabled')

    label2 = tk.Label(result_window, text="Pending follow requests:", font=("Arial", 12, "bold"))
    label2.pack(pady=(10, 0))

    text2 = scrolledtext.ScrolledText(result_window, width=90, height=10, font=("Consolas", 10))
    text2.pack(padx=10, pady=(0, 10))
    if pending_requests:
        text2.insert(tk.END, format_columns(sorted(pending_requests)))
    else:
        text2.insert(tk.END, "No pending follow requests found.")
    text2.configure(state='disabled')

def select_zip_and_process():
    zip_path = filedialog.askopenfilename(
        title="Select Instagram Data ZIP",
        filetypes=[("ZIP files", "*.zip")]
    )
    if not zip_path:
        return
    non_followers, pending_requests, files, error = process_zip(zip_path)
    if error:
        messagebox.showerror("Error", error)
        return
    show_result_window(non_followers, pending_requests)

def main():
    root = tk.Tk()
    root.title("Instagram Non-Followers Checker")
    root.geometry("400x250")
    label = tk.Label(root, text="Select your Instagram data ZIP file", font=("Arial", 12))
    label.pack(pady=20)
    btn = tk.Button(root, text="Select ZIP", command=select_zip_and_process, font=("Arial", 12))
    btn.pack(pady=10)
    root.mainloop()

if __name__ == "__main__":
    main()