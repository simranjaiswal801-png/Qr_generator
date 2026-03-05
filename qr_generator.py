import tkinter as tk
import qrcode
from PIL import ImageTk, Image

def generate_qr():
    data = entry.get()
    
    qr = qrcode.make(data)
    qr.save("qr_code.png")

    img = Image.open("qr_code.png")
    img = img.resize((180,180))
    img = ImageTk.PhotoImage(img)

    qr_label.config(image=img)
    qr_label.image = img

root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x350")
root.configure(bg="#f2f2f2")

title = tk.Label(root,text="QR Code Generator",font=("Arial",18,"bold"),bg="#f2f2f2")
title.pack(pady=10)

entry = tk.Entry(root,width=30)
entry.pack(pady=10)

tk.Button(root,text="Generate QR Code",bg="#673AB7",fg="white",command=generate_qr).pack(pady=10)

qr_label = tk.Label(root,bg="#f2f2f2")
qr_label.pack(pady=10)

root.mainloop()