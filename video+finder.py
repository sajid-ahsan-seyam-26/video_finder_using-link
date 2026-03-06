import tkinter as tk
import webbrowser

def play_video():
    url = url_entry.get()
    if url == "":
        tk.messagebox.showerror("Error","Please enter YouTube URL")
    else:
        webbrowser.open(url)

# main window
root = tk.Tk()
root.title("YouTube Player")
root.geometry("400x150")

tk.Label(root, text="Paste YouTube Link:", font=("Arial",12)).pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

tk.Button(root, text="Play Video", command=play_video, bg="red", fg="white", font=("Arial",12)).pack(pady=10)

root.mainloop()
