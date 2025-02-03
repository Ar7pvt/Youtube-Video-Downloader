

import os
import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp

# Create the main application window
root = tk.Tk()
root.geometry('500x350')
root.title("YouTube Video Downloader")

# Labels
tk.Label(root, text='YouTube Video Downloader', font='arial 15 bold').pack(pady=10)
tk.Label(root, text='Paste Video URL:', font='arial 12').pack(pady=5)

# URL Entry Box
video_link = tk.StringVar()
url_entry = tk.Entry(root, width=50, textvariable=video_link)
url_entry.pack(pady=5)

# Variable for save location
save_path = tk.StringVar()

def select_save_location():
    """Opens a file dialog to choose save location"""
    folder_selected = filedialog.askdirectory()
    save_path.set(folder_selected)

# Save Location Button
tk.Button(root, text="Choose Save Location", command=select_save_location).pack(pady=5)
tk.Label(root, textvariable=save_path, font='arial 10').pack(pady=5)

def download_video():
    """Downloads the video using yt_dlp"""
    url = video_link.get()
    path = save_path.get()
    
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return
    
    if not path:
        messagebox.showerror("Error", "Please select a save location")
        return

    messagebox.showinfo("Downloading", "Your video is being downloaded...")

    ydl_opts = {
        'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
        'format': 'best[ext=mp4]',  # Downloads best MP4 format (video + audio)
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Download Completed!")
    except Exception as e:
        messagebox.showerror("Error", f"Download failed: {e}")

# Download Button
tk.Button(root, text="Download", font='arial 12 bold', command=download_video).pack(pady=20)

# Run the application
root.mainloop()
