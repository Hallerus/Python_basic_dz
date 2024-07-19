def send_email(message: str, recipient: str, *, sender="university.help@gmail.com"):
    first_level_domain = ['.com', '.ru', '.net']
    sender_domain = ''
    recipient_domain = ''
    for domain in first_level_domain:
        if sender.endswith(domain):
            sender_domain = domain
            # print(f'Sender domain: {domain}')
        if recipient.endswith(domain):
            recipient_domain = domain
            # print(f'Recipient domain: {domain}')

    if '@' in recipient and '@' in sender and sender_domain != '' and recipient_domain != '':
        if sender == recipient:
            print("Нельзя отправить письмо самому себе!")
        elif sender == "university.help@gmail.com":
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
        else:
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на aдрес {recipient}')
    else:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

# send_email(input("Введите текст письма:"), input("Введите e-mail получателя:").lower())
