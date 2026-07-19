import customtkinter as ctk
from tkinter import messagebox
from weather import get_weather
from PIL import Image 
BG_COLOR = "#0F172A"          # Window Background
FRAME_COLOR = "#1E293B"       # Main Frame
CARD_COLOR = "#334155"        # Result Frame
BUTTON_COLOR = "#2563EB"      # Search Button
BUTTON_HOVER = "#1D4ED8"      # Button Hover
ENTRY_COLOR = "#475569"       # Entry Background
TEXT_COLOR = "#F8FAFC"        # White Text
LABEL_COLOR = "#93C5FD"       # Light Blue Labels

# ---------------- Appearance ----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ---------------- Window ----------------
app = ctk.CTk()
app.title("Weather App")
app.geometry("700x650")
app.resizable(False, False)
app.configure(fg_color=BG_COLOR)

#-------------Load Icon----------------
city_icon = ctk.CTkImage(

    light_image=Image.open("assets/city.png"),
    dark_image=Image.open("assets/city.png"),
    size=(22, 22)
)

condition_icon = ctk.CTkImage(
    light_image=Image.open("assets/condition.png"),
    dark_image=Image.open("assets/condition.png"),
    size=(22, 22)
)

earth_icon = ctk.CTkImage(
    light_image=Image.open("assets/earth.png"),
    dark_image=Image.open("assets/earth.png"),
    size=(22, 22)
)


humidity_icon = ctk.CTkImage(
    light_image=Image.open("assets/humidity.png"),
    dark_image=Image.open("assets/humidity.png"),
    size=(22, 22)
)
feels_like_icon = ctk.CTkImage(
    light_image=Image.open("assets/feels_like.png"),
    dark_image=Image.open("assets/feels_like.png"),
    size=(22, 22)
)
pressure_icon = ctk.CTkImage(
    light_image=Image.open("assets/pressure-gauge.png"),
    dark_image=Image.open("assets/pressure-gauge.png"),
    size=(22, 22)
)
rain_icon = ctk.CTkImage(
    light_image=Image.open("assets/rain.png"),
    dark_image=Image.open("assets/rain.png"),
    size=(22, 22)
)
snowflake_icon = ctk.CTkImage(
    light_image=Image.open("assets/snowflake.png"),
    dark_image=Image.open("assets/snowflake.png"),
    size=(22, 22)
)

region_icon = ctk.CTkImage(
    light_image=Image.open("assets/region.png"),
    dark_image=Image.open("assets/region.png"),
    size=(22, 22)
)

wind_speed_icon = ctk.CTkImage(
    light_image=Image.open("assets/wind_speed.png"),
    dark_image=Image.open("assets/wind_speed.png"),
    size=(22, 22)
)
temperature_icon = ctk.CTkImage(
    light_image=Image.open("assets/temperature.png"),
    dark_image=Image.open("assets/temperature.png"),
    size=(22, 22)
)
uv_index_icon = ctk.CTkImage(
    light_image=Image.open("assets/uv-index.png"),
    dark_image=Image.open("assets/uv-index.png"),
    size=(22, 22)
)
will_it_rain_icon = ctk.CTkImage(
    light_image=Image.open("assets/will_it_rain.png"),
    dark_image=Image.open("assets/will_it_rain.png"),
    size=(22, 22)
)
will_it_snow_icon = ctk.CTkImage(
    light_image=Image.open("assets/will_it_snow.png"),
    dark_image=Image.open("assets/will_it_snow.png"),
    size=(22, 22)
)
wind_direction_icon = ctk.CTkImage(
    light_image=Image.open("assets/wind_directon.png"),
    dark_image=Image.open("assets/wind_directon.png"),
    size=(22, 22)
)
wind_icon = ctk.CTkImage(
    light_image=Image.open("assets/wind.png"),
    dark_image=Image.open("assets/wind.png"),
    size=(22, 22)
)

# ---------------- Main Frame ----------------
main_frame = ctk.CTkFrame(app, corner_radius=15,fg_color=FRAME_COLOR)
main_frame.pack(fill="both", expand=True, padx=15, pady=15)

# ---------------- Title ----------------
title = ctk.CTkLabel(
    main_frame,
    text="🌤 Weather App",
    font=("Segoe UI", 28, "bold"),
    text_color="yellow",
)
title.pack(pady=15)

# ---------------- Search Frame ----------------
search_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
search_frame.pack(pady=10)

city_entry = ctk.CTkEntry(
    search_frame,
    width=350,
    height=40,
    placeholder_text="Enter City Name",
    font=("Segoe UI", 15),
    fg_color=ENTRY_COLOR,
    text_color=TEXT_COLOR,
    border_color=BUTTON_COLOR,
)
city_entry.pack(side="left", padx=10)

def search_weather():
    city=city_entry.get().strip()
    weather =get_weather(city)
    if weather is None:
        messagebox.showerror("Error! ,City Not Found.")
        return
    for key in weather:
        label_widgets[key].configure(text=str(weather[key]))
    label_widgets["Chance of Rain"].configure(
    text=f"{weather['Chance of Rain']}%"
    )
    label_widgets["Chance of Snow"].configure(
    text=f"{weather['Chance of Snow']}%"
    )
    if weather["Will It Rain?"] == 1:
        rain = "Yes"
    else:
        rain = "No"
    label_widgets["Will It Rain?"].configure(text=rain)

    if weather["Will It Snow?"] == 1:
        snow = "Yes"
    else:
        snow = "No"
    label_widgets["Will It Snow?"].configure(text=snow)

    label_widgets["Humidity"].configure(
    text=f"{weather['Humidity']}%"
    )

search_btn = ctk.CTkButton(
    search_frame,
    text="Search",
    width=120,
    height=40,
    font=("Segoe UI", 15, "bold"),
    fg_color=BUTTON_COLOR,
    hover_color=BUTTON_HOVER,
    text_color="white",
    command=search_weather
)
search_btn.pack(side="left")

# ---------------- Result Frame ----------------
result_frame = ctk.CTkFrame(main_frame, corner_radius=12,fg_color=CARD_COLOR,)
result_frame.pack(fill="both", expand=True, padx=20, pady=20)

# ---------------- Configure Grid ----------------
result_frame.grid_columnconfigure(0, weight=1)
result_frame.grid_columnconfigure(1, weight=1)

# ---------------- Labels ----------------
labels = [
    "City",
    "Region",
    "Country",
    "Temperature (C)",
    "Temperature (F)",
    "Feels Like (C)",
    "Feels Like (F)",
    "Humidity",
    "Condition",
    "Wind Speed (kph)",
    "Wind Direction",
    "Wind Degree",
    "Pressure (mb)",
    "Chance of Rain",
    "Chance of Snow",
    "Will It Rain?",
    "Will It Snow?",
    "UV Index"
]
icon ={
        "City" : city_icon,
        "Region" : region_icon,
        "Country" : earth_icon,
        "Condition" : condition_icon,
        "Temperature (C)" : temperature_icon,
        "Temperature (F)" : temperature_icon,
        "Humidity" : humidity_icon,
        "Condition" : condition_icon,
        "Feels Like (C)" : feels_like_icon,
        "Feels Like (F)" : feels_like_icon,
        "Chance of Rain" : rain_icon,
        "Chance of Snow" : snowflake_icon,
        "Wind Speed (kph)" : wind_speed_icon,
        "Wind Direction" : wind_direction_icon,
        "Wind Degree" : wind_icon,
        "Pressure (mb)" : pressure_icon,
        "UV Index" : uv_index_icon,
        "Will It Rain?" : will_it_rain_icon,
        "Will It Snow?" : will_it_snow_icon,

    }

label_widgets = {}

for i, item in enumerate(labels):
    row = i % 9
    col = (i // 9) * 2

    name = ctk.CTkLabel(
        result_frame,
        text="  " + item + ":",
        image=icon[item],
        compound="left",
        font=("Segoe UI", 14, "bold"),
        text_color=LABEL_COLOR,
    )
    name.grid(row=row, column=col, padx=(20, 5), pady=10, sticky="w")

    value = ctk.CTkLabel(
        result_frame,
        text="----------",
        font=("Segoe UI", 14)
    )
    value.grid(row=row, column=col + 1, padx=(0, 20), pady=10, sticky="w")

    label_widgets[item] = value

app.mainloop()