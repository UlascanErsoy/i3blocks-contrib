#!/usr/bin/env python3 
"""github.com/UlascanErsoy
Battery indicator. Who uses perl anymore.
"""

import subprocess

def get_battery_glyph(percent):
    perc = percent.strip().replace("%","")
    if not perc.isnumeric():
        return ""

    perc = int(perc)

    if 85 <= perc <= 100:
        return "", ""
    elif 75 <= perc < 90:
        return "", ""
    elif 50 <= perc < 75:
        return "", ""
    elif 25 <= perc < 50:
        return "", "#F5A442"
    else:
        return "", "#DD4444"
if __name__ == "__main__":

    out,err= subprocess.Popen(["acpi","-b"],stdout=subprocess.PIPE)\
                        .communicate()

    battery = [item for item in out.decode().split("\n") 
               if not "unavailable" in item]

    if not battery:
        print("NO BAT")
        print("")
        print("#FF0000")

    status = battery[0].split(":")[-1]

    status, percent = status.split(",")[:2]
    icon, color = get_battery_glyph(percent)

    if status.strip() == "Discharging":
        print(f"{icon}{percent}")
        print("")
        print(color)
    elif status.strip() == "Charging":
        print(f"⚡{percent}")
    elif status.strip() == "Full":
        print("")
        print("")
        print("#55AA55")
