import tkinter as tk
from tkinter import filedialog, messagebox
from encryption_tool import encrypt_file, decrypt_file

def browse_file():
    path = filedialog.askopenfilename()
    select_file.delete(0, tk.END)
    select_file.insert(0, path)

def perform(action):
    file_path = select_file.get()
    password = password_input.get()
    if not file_path or not password:
        return messagebox.showerror("Oops!", "⚠️ Please select a file and enter password.")

    try:
        if action == "enc":
            encrypt_file(file_path, password)
            messagebox.showinfo(
                "Encryption Complete",
                "✅ File Encrypted Successfully!\n\n🔐 Built by Charu"
            )
        else:
            decrypt_file(file_path, password)
            messagebox.showinfo(
                "Decryption Complete",
                "✅ File Decrypted Successfully!\n\n🔐 Built by Charu"
            )
    except Exception as e:
        messagebox.showerror("Error", f"❌ {str(e)}")


root = tk.Tk()
root.title("Charu's Encryption Tool 🔐")
root.geometry("450x280")
root.configure(bg="#f0f8ff")

tk.Label(root, text="💡 AES-256 File Encryption", font=("Arial Rounded MT Bold", 14), bg="#f0f8ff", fg="#003366").pack(pady=10)

select_file = tk.Entry(root, width=45)
select_file.pack()
tk.Button(root, text="📁 Browse File", command=browse_file, bg="#00bfff", fg="white", width=15).pack(pady=6)

password_input = tk.Entry(root, show="*", width=30)
password_input.pack(pady=5)
tk.Label(root, text="Enter Secret Password", bg="#f0f8ff", fg="#003366").pack()

btn_frame = tk.Frame(root, bg="#f0f8ff")
btn_frame.pack(pady=20)

encrypt_btn = tk.Button(btn_frame, text="Encrypt 🔒", command=lambda: perform("enc"), bg="#32cd32", fg="white", width=15)
decrypt_btn = tk.Button(btn_frame, text="Decrypt 🔓", command=lambda: perform("dec"), bg="#ff6347", fg="white", width=15)

encrypt_btn.grid(row=0, column=0, padx=15)
decrypt_btn.grid(row=0, column=1, padx=15)

root.mainloop()
