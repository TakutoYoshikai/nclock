import tkinter
import datetime
import threading
import time



def main():
    root = tkinter.Tk()
    root.title("Nuru Clock")
    width = root.winfo_screenwidth()
    width = width - 200
    root.geometry("200x70+" + str(width) + "+0")

    jp_label = tkinter.Label(text="00:00")
    id_label = tkinter.Label(text="00:00")

    jp_label.config(font=("Helavetica", 20))
    id_label.config(font=("Helavetica bold", 20), foreground="red")

    def job():
        while True:
            jp_now = datetime.datetime.now()
            id_now = jp_now - datetime.timedelta(hours=2)
            jp_time = format(jp_now.hour, "02") + ":" + format(jp_now.minute, "02")
            id_time = format(id_now.hour, "02") + ":" + format(id_now.minute, "02")
            jp_label["text"] = jp_time
            id_label["text"] = id_time
            time.sleep(1)


    jp_label.pack()
    id_label.pack()

    threading.Thread(target=job).start()

    root.mainloop()

if __name__ == "__main__":
    main()
