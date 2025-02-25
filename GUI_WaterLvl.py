import tkinter as tk

# Function to calculate Water Level and Risk
def calculate_WaterLvl(air_pressure):
    WaterLvl = (760 - air_pressure) * 11  

    if WaterLvl > 2500:
        risk = "ระดับอันตราย"
    elif WaterLvl >= 0:
        risk = "ระดับปกติ"
    else:
        risk = "ระดับต่ำผิดปกติ"

    return WaterLvl, risk

# Function that runs when the "Calculate" button is pressed
def on_calculate():
    try:
        air_pressure = float(air_pressure_entry.get())  # Get the value from the input field
        WaterLvl, risk = calculate_WaterLvl(air_pressure)  # Call the function to calculate water level and risk
        result_label.config(text=f"ความสูงจากระดับน้ำทะเล: {WaterLvl:.2f} เมตร\nระดับความเสี่ยง: {risk}")  # Update the result label
    except ValueError:
        result_label.config(text="กรุณาป้อนค่าความดันอากาศที่ถูกต้อง")  # Handle invalid input

# Function to clear the input and result
def on_clear():
    air_pressure_entry.delete(0, tk.END)  # Clear the input field
    result_label.config(text="")  # Clear the result label

# Function to exit the program
def on_exit():
    window.quit()

# Create the main window
window = tk.Tk()
window.title("การคำนวณระดับน้ำทะเล")

# Set window size and background color (sea theme)
window.geometry("500x400")  # Resize the window
window.configure(bg="#ADD8E6")  # Set background color to light blue (sea theme)

# Create and pack the widgets (labels, entry fields, buttons)
air_pressure_label = tk.Label(window, text="กรุณาป้อนค่าความดันอากาศ (mmHg):", bg="#ADD8E6", font=("Segoe UI", 14, "bold"))
air_pressure_label.pack(pady=10)

air_pressure_entry = tk.Entry(window, font=("Verdana", 14))
air_pressure_entry.pack(pady=10)

# Create a smaller button and change the color to sea tones
calculate_button = tk.Button(window, text="คำนวณ", command=on_calculate, font=("Comic Sans MS", 14, "bold"), width=15, height=1, bg="#20B2AA", fg="white")
calculate_button.pack(pady=10)

# Create Clear and Exit buttons with matching sea colors
clear_button = tk.Button(window, text="ล้าง", command=on_clear, font=("Comic Sans MS", 14), width=15, height=1, bg="#66CDAA", fg="white")
clear_button.pack(pady=5)

exit_button = tk.Button(window, text="ออก", command=on_exit, font=("Comic Sans MS", 14), width=15, height=1, bg="#4682B4", fg="white")
exit_button.pack(pady=5)

# Result label to display the output
result_label = tk.Label(window, text="", bg="#ADD8E6", font=("Segoe UI", 14))
result_label.pack(pady=10)

# Start the GUI main loop
window.mainloop()

