import tkinter
import datetime
import threading
import time
import pytz
from playsound import playsound
import os


sound_path = os.path.dirname(os.path.abspath(__file__)) + "/../sound.mp3"

def main():
    root = tkinter.Tk()
    root.title("Nuru Clock")
    root.resizable(False, False)
    width = root.winfo_screenwidth()
    y = width - 200
    root.geometry("200x70+" + str(y) + "+0")

    jp_label = tkinter.Label(text="00:00")
    id_label = tkinter.Label(text="00:00")

    jp_label.config(font=("Helavetica", 20))
    id_label.config(font=("Helavetica bold", 20), foreground="red")

    def job():
        while True:
            jp_now = datetime.datetime.now(tz=pytz.timezone("Asia/Tokyo"))
            id_now = jp_now - datetime.timedelta(hours=2)

            jp_time = format(jp_now.hour, "02") + ":" + format(jp_now.minute, "02")
            id_time = format(id_now.hour, "02") + ":" + format(id_now.minute, "02")

            jp_label["text"] = jp_time
            id_label["text"] = id_time
            if jp_now.hour == 19 and jp_now.minute == 30 and jp_now.second == 0:
                playsound(sound_path)
            time.sleep(1)

    jp_label.pack()
    id_label.pack()

    threading.Thread(target=job).start()

    root.mainloop()

if __name__ == "__main__":
    main()
