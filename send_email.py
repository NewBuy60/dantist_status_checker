import smtplib
from email.mime.text import MIMEText

def send_email(message):
    sender = "namsaraev.kolya@gmail.com"
    password = "vfvrirvliuuufdtr"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg['Subject'] = 'Стоматолог онлайн!!!'
        server.sendmail(sender, sender, msg.as_string())

        print("Сообщение было доставлено успешно")
    except Exception as _ex:
        print(f'{_ex}\nПожалуйста, проверьте ваш логин и пароль')

def main():
    message = input("Введите ваше сообщение: ")
    send_email(message=message)

if __name__ == "__main__":
    main() 