from PIL import image
import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root_tk = customtkinter.CTk()
root_tk.geometry("720x480")

def login(self):
    print("test")
    

frame = customtkinter.CTkFrame(master=root_tk)
frame.pack(pady=0, padx=0, fill="both", expand=True)

my_image = customtkinter.CTkImage(light_image=Image.open(""))

label = customtkinter.CTkLabel(master=frame, text="Login System", font=("SF Pro", 24))
label.pack(pady=12, padx=10) 

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text = "Username", width=160, height=40, corner_radius=0)
entry1.pack(padx=10, pady=12)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text = "Password", width=160, height=40, show="*", corner_radius=0)
entry2.pack(padx=10, pady=12)

button = customtkinter.CTkButton(master=frame, text="Login", command=login, corner_radius=20, height=30, width=100)
button.pack(padx=10, pady=12)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(padx=10, pady=12)

root_tk.mainloop()
