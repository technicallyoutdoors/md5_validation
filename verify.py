import customtkinter
import tkinter
import time

customtkinter.set_appearance_mode("dark")

app = customtkinter.CTk()
app.geometry("500x300")
app.title("MD5 Validation")

entry1 = customtkinter.CTkEntry(master=app, text_color="black", width=180, placeholder_text_color="black", placeholder_text="Enter the desired MD5 hash: ", fg_color='#FF6600')
entry1.pack(padx=5, pady=5, anchor=tkinter.CENTER)

entry2 = customtkinter.CTkEntry(master=app, text_color="black", width=180, placeholder_text_color="black", placeholder_text="Enter the actual MD5 hash: ", fg_color='#FF6600')
entry2.pack(padx=5, pady=5, anchor=tkinter.CENTER)


def button_click_event1():
    output1 = entry1.get()
    output2 = entry2.get()
    if output1 == output2:
        md5_pass()
    else: 
        md5_failure()
      

def md5_failure():
    failed = "THE MD5 HASH CANNOT BE VALIDATED, PLEASE TRY AGAIN"
    label = customtkinter.CTkLabel(master=app, text=failed, text_color="black", fg_color="#ff0000", corner_radius=5)
    label.pack(padx=20, pady=20, anchor=tkinter.CENTER)

def md5_pass():
    passed = "CONGRATS, THE MD5 HASH HAS BEEN VALIDATED"
    label = customtkinter.CTkLabel(master=app, text=passed, text_color="black", fg_color="#4169E1", corner_radius=5)
    label.pack(padx=20, pady=20, anchor=tkinter.N)
    # progressbar = customtkinter.CTkProgressBar(master=app)
    # # progressbar.start()
    # # progressbar.pack(padx=20, pady=10)
    # time.sleep(2)
    #progressbar.stop()
    



button1 = customtkinter.CTkButton(app, text="Validate", text_color="black", width=180, fg_color="#FF6600", hover_color="#4169E1", command=button_click_event1)
button1.pack(padx=10, pady=10)

        
if __name__ == "__main__":
    app.mainloop()