# Write a program that generate a file that contains a structured email message

import re
import yagmail

def send_mail( sender_email,receiver_email, subject, msg, receiver_name):
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", receiver_email):
        raise ValueError("Invalid receiver email!")

    body = (
        f"From: {sender_email}\n"
        f"To: {receiver_email}\n"

        f"Hi, {receiver_name}\n"
        f"{msg}\n"
        f"Thanks\n"
    )

    try:
        yag = yagmail.SMTP(sender_email, "pyrv ocdy gqmd pqku")
        yag.send(to=receiver_email, subject=subject, contents=body)
        print("Email sent")
    except Exception as e:
        print(f"Failed {e}")


if __name__ == "__main__":
    send_mail("mohamed.abdelhaqgp@gmail.com","mohamed.abdelhaq99@gmail.com", "testtSubject","Hello from the other siiiide", 'MO')
