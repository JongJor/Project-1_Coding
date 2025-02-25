def calculate_WaterLvl(air_pressure):
    WaterLvl = (760 - air_pressure) * 11  

    if WaterLvl > 2500:
        risk = "ระดับอันตราย"
    elif WaterLvl >= 0:
        risk = "ระดับปกติ"
    else:
        risk = "ระดับต่ำผิดปกติ"

    return WaterLvl, risk

air_pressure = float(input("กรุณาป้อนค่าความดันอากาศ (mmHg): "))

WaterLvl, risk = calculate_WaterLvl(air_pressure)
print(f"ความสูงจากระดับน้ำทะเล: {WaterLvl:.2f} เมตร")
print(f"ระดับความเสี่ยง: {risk}")
