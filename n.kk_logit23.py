import smtplib
import ssl
from email.message import EmailMessage

def loe_küsimused_vastused(failinimi):
    küs_vas = {}
    with open(failinimi, "r", encoding="utf-8") as fail:
        for line in fail:
            n = line.find(":")
            küs_vas[line[:n].strip()] = line[n + 1:].strip()
    return küs_vas

def kirjuta_küsimused_vastused(failinimi, küs_vas):
    with open(failinimi, "w", encoding="utf-8") as fail:
        for küs, vas in küs_vas.items():
            fail.write(f"{küs}:{vas}\n")

def esita_küsimustik_kirjuta_email(küs_vas, küsitavate_arv, sender_email, password, receiver_email):
    õiged_vastused = 0

    for i in range(küsitavate_arv):
        küs = list(küs_vas.keys())[i]
        oodatud_vastus = küs_vas[küs]

        vastus = input(f"{küs}\nSinu vastus: ").strip()

        if vastus.lower() == oodatud_vastus.lower():
            print("Õige!\n")
            õiged_vastused += 1
        else:
            print(f"Vale! Õige vastus on: {oodatud_vastus}\n")

        if i == küsitavate_arv - 1:
            print("Viktoriin lõppenud!")

    smtp_server = "smtp.gmail.com"
    port = 587

    msg = EmailMessage()
    msg.set_content(f"Kokku esitati {küsitavate_arv} küsimust. Õigete vastuste arv: {õiged_vastused}")
    msg["Subject"] = "Tulemused"
    msg["From"] = "Eldarushko"
    msg["To"] = receiver_email

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)
            server.login(sender_email, password)
            server.send_message(msg)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    failinimi = "Küsimus.txt"
    küs_vas = loe_küsimused_vastused(failinimi)

    küsitavate_arv = int(input("Mitu küsimust soovid esitada? "))

    sender_email = "nik.kirsanov17@gmail.com"
    password = input("Kirjuta oma salasõna ja vajuta enter: ")
    receiver_email = "nik.kirsanov17@gmail.com"

    esita_küsimustik_kirjuta_email(küs_vas, küsitavate_arv, sender_email, password, receiver_email)
