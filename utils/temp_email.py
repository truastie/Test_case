from temp_mails import Tenminemail_com

def get_temp_email():
    mail= Tenminemail_com()
    print(f"Ваш временный email: {mail.email}")
    return mail

def get_latest_email(mail):
    data = mail.wait_for_new_email(delay=1.0, timeout=120)
    email_content = mail.get_mail_content(message_id=data["id"])
    return email_content

mail = get_temp_email()
print("Жду новое письмо...")
email_content = get_latest_email(mail)
print("Письмо получено:")
print(email_content)