from tkinter import *
import qrcode
import os

os.system("cls")
root = Tk()
root.title("Qr Generator")
root.geometry("1000x550")
root.config(bg="#000080")
root.resizable(False, False)

image_icon=PhotoImage(file="MYPROJECT/Qr/Test.png")
root.iconphoto(False,image_icon)

def generate():
    name = title.get()
    text = entry.get()
    if name and text:  # Check if both fields are filled
        try:
            qr = qrcode.make(text)
            # Using os.path.join for proper path handling
            save_path = os.path.join("MYPROJECT", "Qr", f"{name}.png")
            # Create directories if they don't exist
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            qr.save(save_path)
            
            global Image
            Image=PhotoImage(file=save_path)
            Image_view.config(image=Image)
            status_label.config(text="QR Code Berhasil di buat")
        except Exception as e:
            status_label.config(text=f"Error: {str(e)}")
    else:
        status_label.config(text="Kamu Harus mengisi label diatas")


Image_view=Label(root,bg="#000080")
Image_view.pack(padx=50,pady=10,side=RIGHT)

Label(root, text="Title", fg="white", bg="#008080", font=15).place(x=50, y=170)
title = Entry(root, width=13, font="arial 15")
title.place(x=50, y=200)

#Isi konten
Label(root, text="Content", fg="white", bg="#008080", font=15).place(x=50, y=235)
entry = Entry(root, width=26, font="arial 14")
entry.place(x=50, y=260)


Button(root, text="Generate", width=20, height=2, bg="#CCCCFF", fg="black", command=generate).place(x=50, y=300)


status_label = Label(root, text="", fg="#008080", bg="#000080", font=15)
status_label.place(x=50, y=350)

root.mainloop()