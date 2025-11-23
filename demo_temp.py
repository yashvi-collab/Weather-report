from tkinter import *
from tkinter import ttk, messagebox
import requests

#-------------------- Fetch Weather Data --------------------
def get_weather():
    city=city_var.get().strip()   

    if city=="":
        messagebox.showerror("Error","Please select a city!")
        return

    try:
        url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=f24efee065013a66bb3118ded514213a"
        data= requests.get(url).json()

        if data.get("cod") != 200:
            messagebox.showerror("Error",data.get("message","City not found"))
            return
        
        
        w_label_value.config(text=data["weather"][0]["main"])
        wb_label_value.config(text=data["weather"][0]["description"])
        temp_label_value.config(text=str(int(data["main"]["temp"]-273.15))+" °C")
        pressure_label_value.config(text=str(data["main"]["pressure"])+" hPa") 

    except Exception as e:
        messagebox.showerror("Error","Unable to fetch data.")


#--------------------GUI WINDOW ---------------------
win=Tk()
win.title("Climate View - Weather App")
win.geometry("520x600")
win.configure(bg="#d9faff")


#--------------------- Greadient Background---------------------
canvas=Canvas(win,width=520,height=600)
canvas.place(x=0,y=0)

# Light Gradient
for i in range(0,600):
    color=f"#%02x%02x%02x" % (217, 250 -i//4, 255)
    canvas.create_line(0, i, 520, i, fill=color)


#-------------------- Title --------------------
title=Label(
    win,
    text="Climate View",
    font=("Brush Script MT",40,"bold"),
    bg="#d9faff",
    fg="#003366"
)
title.place(x=80,y=20)


#-------------------- Dropdown --------------------
city_var=StringVar()

states_list = [
    'Andrapradesh','ArunachalPradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat',
    'Haryana','HimachalPradesh','Jammu and Kashmir','Jharkhand','Karnataka','Kerala',
    'Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha',
    'Punjab','Rajasthan','Sikkim','TamilNadu','Telangana','Tripura','Uttar Pradesh',
    'Uttarakhand','West Bengal','Andaman and Nicobar Islands','Chandigarh','Dadra and Nagar Haveli',
    'Daman and Diu','Delhi','Ladakh','Lakshadweep','Puducherry']


city_dropdown=ttk.Combobox(
    win,
    values=states_list,
    textvariable=city_var,
    font=("Georgia",16),
)
city_dropdown.place(x=60,y=120,width=400,height=40)


#-------------------- Fetch Button --------------------
fetch_btn=Button(
    win,
    text="Get Weather",
    font=("Georgia",18,"bold"),
    bg="#87CEEB",
    fg="black",
    command=get_weather
)
fetch_btn.place(x=180,y=180,width=160,height=45)


#-------------------- Labels (Beautiful Styling) --------------------
label_font=("Segoe Script", 18, "bold")
value_font=("Georgia",18)

# Weather Type
Label(win,text="Weather:",font=label_font,bg="#d9faff").place(x=60,y=260)
w_label_value=Label(win,text="",font=value_font,bg="#d9faff")
w_label_value.place(x=250,y=260)

# Description
Label(win,text="Description:",font=label_font,bg="#d9faff").place(x=60,y=320)
wb_label_value=Label(win,text="",font=value_font,bg="#d9faff")
wb_label_value.place(x=250,y=320)

# Temperature
Label(win,text="Temperature:",font=label_font,bg="#d9faff").place(x=60,y=380)
temp_label_value=Label(win,text="",font=value_font,bg="#d9faff")
temp_label_value.place(x=250,y=380)

# Pressure
Label(win,text="Pressure:",font=label_font,bg="#d9faff").place(x=60,y=440)
pressure_label_value=Label(win,text="",font=value_font,bg="#d9faff")
pressure_label_value.place(x=250,y=440)


win.mainloop()