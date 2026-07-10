import customtkinter as ctk
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
app.geometry("700x600")
app.resizable(False, False)
app.configure(fg_color=BG_COLOR)

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

search_btn = ctk.CTkButton(
    search_frame,
    text="Search",
    width=120,
    height=40,
    font=("Segoe UI", 15, "bold"),
    fg_color=BUTTON_COLOR,
    hover_color=BUTTON_HOVER,
    text_color="white",
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

label_widgets = {}

for i, item in enumerate(labels):
    row = i % 9
    col = (i // 9) * 2

    name = ctk.CTkLabel(
        result_frame,
        text=item + ":",
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