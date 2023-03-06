import customtkinter
import tkinter
import time

customtkinter.set_appearance_mode("dark")

app = customtkinter.CTk()
app.geometry("500x300")
app.title("MD5 Validation")

entry1 = customtkinter.CTkEntry(master=app, text_color="black", width=180, placeholder_text_color="black",
                                placeholder_text="Enter the desired MD5 hash: ", fg_color='#FF6600')
entry1.pack(padx=2, pady=2, anchor=tkinter.CENTER)

entry2 = customtkinter.CTkEntry(master=app, text_color="black", width=180, placeholder_text_color="black",
                                placeholder_text="Enter the actual MD5 hash: ", fg_color='#FF6600')
entry2.pack(padx=2, pady=2, anchor=tkinter.CENTER)


def button_click_event1():
    output1 = entry1.get()
    output2 = entry2.get()
    global no_text_entry
    if len(output1) < 1:
        no_text_entry = "No entry detected, please enter an MD5 hash output before proceeding"
        global no_text_label
        no_text_label = customtkinter.CTkLabel(
            master=app, text=no_text_entry, text_color="black", fg_color="#ff0000", corner_radius=5)
        no_text_label.pack(padx=20, pady=20, anchor=tkinter.CENTER)
    if len(output2) < 0:
        no_text_entry = "No entry detected, please enter an MD5 hash output before proceeding"
        no_text_label = customtkinter.CTkLabel(
            master=app, text=no_text_entry, text_color="black", fg_color="#ff0000", corner_radius=5)
        no_text_label.pack(padx=20, pady=20, anchor=tkinter.CENTER)
    if output1 == output2 and len(output2 and output1) > 1:
        md5_pass()
    if output1 != output2 and len(output2 and output1) > 1:
        md5_failure()
    


def md5_failure():
    failed = "THE MD5 HASH CANNOT BE VALIDATED, PLEASE TRY AGAIN"
    global md5_failure_label
    md5_failure_label = customtkinter.CTkLabel(
        master=app, text=failed, text_color="black", fg_color="#ff0000", corner_radius=5)
    md5_failure_label.pack(padx=20, pady=20, anchor=tkinter.CENTER)
    # time.sleep(3)
    # label.destroy()


def md5_pass():
    passed = "CONGRATS, THE MD5 HASH HAS BEEN VALIDATED"
    global md5_pass_label
    md5_pass_label = customtkinter.CTkLabel(
        master=app, text=passed, text_color="black", fg_color="#4169E1", corner_radius=5)
    md5_pass_label.pack(padx=20, pady=20, anchor=tkinter.N)
  
  
def reset_validation():
    md5_pass_label.pack_forget()
    md5_failure_label.pack_forget()
    no_text_label.pack_forget()
    
    
    


button1 = customtkinter.CTkButton(app, text="Validate", text_color="black", width=180,
                                  fg_color="#FF6600", hover_color="#4169E1", command=button_click_event1)
button1.pack(padx=10, pady=10)

button2 = customtkinter.CTkButton(app, text="Reset", text_color="black", width=180,
                                  fg_color="#FF6600", hover_color="#4169E1", command=reset_validation)
button2.pack(padx=10, pady=10)


if __name__ == "__main__":
    app.mainloop()
