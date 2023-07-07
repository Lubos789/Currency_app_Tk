from tkinter import *
import requests


# Barvy
main_color = "#14085f"

# Okono
window = Tk()
window.minsize(400, 120)
window.resizable(False, False)
window.title("Prevod men")
window.config(bg=main_color)

# Funkce
def count():
    notification_label["text"] = ""
    try:
        currency_from = drop_down_from.get()
        currency_to = drop_down_to.get()
        amount = int(user_input.get())

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={amount}"

        payload = {}
        headers = {
            "apikey": "cvUVx1LptPik10BRoTR2pd0ZlUmrrv4d"
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        response.raise_for_status()
        result = response.json()
        result_label.config(text=round(result["result"], 2))
        course_label.config(text=f"Kurz:\n{round(result['info']['rate'], 3)}")
    except:
        notification_label["text"] = "Pole neni vyplneno!!!"


# uzivatelsky vstup
user_input = Entry(width=20, font=("Arial", 12), justify=CENTER)
user_input.insert(0, "0")
user_input.grid(row=0, column=0, padx=10, pady=(10, 0))

# Roletka - z jake meny
drop_down_from = StringVar(window)
drop_down_from.set("CZK")
drop_down_from_options = OptionMenu(window, drop_down_from, "EUR", "USD", "CZK")
drop_down_from_options.grid(row=0, column=1, padx=10, pady=(10, 0))


# Roletka - na jakou menu
drop_down_to = StringVar(window)
drop_down_to.set("EUR")
drop_down_to_options = OptionMenu(window, drop_down_to, "EUR", "USD", "CZK")
drop_down_to_options.grid(row=1, column=1, padx=10, pady=(10, 0))

# Button recount
count_button = Button(text="Prepocitat", font=("Arial", 12), command=count)
count_button.grid(row=0, column=2, padx=10, pady=(10, 0))

# Label pro zobrazeni vysledku prepoctu
result_label = Label(text="0", bg=main_color, fg="white", font=("Arial", 12))
result_label.grid(row=1, column=0)

course_label = Label(bg=main_color, fg="white", font=("Arial", 12))
course_label.grid(row=1, column=2)

notification_label = Label(bg=main_color, fg="white", font=("Arial", 12))
notification_label.grid(row=2, column=0)


# Hlavni cyklus
window.mainloop()