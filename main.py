import tkinter as tk
import subprocess

# create window for application
window = tk.Tk()
window.title("Schedule Shutdown")
window.minsize(width=400, height=400)
window.config(padx=50, pady=50)

# function that convert time to second


def convert_to_second(hour: int, minute: int):
    return hour * 60 * 60 + minute * 60


# function that create subprocess
def schedule_shutdown_subprocess():
    hour = int(hour_slider.get())
    minute = int(minute_slider.get())
    second = convert_to_second(hour, minute)
    try:
        mess = subprocess.run(["powershell", "-command", "shutdown", "-s", "-t", f"{second}"], check=True)
        status_label["text"] = "Successful"
    except Exception as e:
        status_label["text"] = "Failed"
        print(e)


# create hour label
tk.Label(window, text="Hour", font=("Arian", 15), padx=20).grid(row=0, column=0)

# create hour slider
hour_slider = tk.Scale(window, from_=0, to=24, orient=tk.HORIZONTAL)
hour_slider.grid(row=0, column=2)

# create minute label
tk.Label(window, text="Minute", font=("Arian", 15), padx=20).grid(row=1, column=0)

# create minute slider
minute_slider = tk.Scale(window, from_=0, to=60, orient=tk.HORIZONTAL)
minute_slider.grid(row=1, column=2)

# create schedule shutdown button
shutdown_button = tk.Button(window, text="Shutdown", command=schedule_shutdown_subprocess)
shutdown_button.grid(row=2, column=1)

# create status label
status_label = tk.Label(window, text="")
status_label.grid(row=3, column=1)
# mainloop
window.mainloop()
