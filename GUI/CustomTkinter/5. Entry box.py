# Create an entry box 

my_entry = customtkinter.CTkEntry(app, placeholder_text="Enter your name",
                                  height=150,
                                  width=200,
                                  font=('Helvetica',18),
                                  corner_radius=50,
                                  text_color="green",
                                  placeholder_text_color="blue",
                                  fg_color=("blue","lightblue"))
my_entry.pack(pady=20)