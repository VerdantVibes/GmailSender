from mailersend import emails


def SendEmail():
    mailer = emails.NewEmail(
        "mlsn.09d5bd78dcbbc4582470aa1e1b00af184c32320a51b1fd97ca6d2574aaa658e0"  # example
    )

    mail_body = {}

    mail_from = {
        "name": "",
        "email": "",
    }

    recipients = [
        {
            "name": "",
            "email": "example@gmail.com",
        }
    ]

    reply_to = [
        {
            "name": "Vanya",
            "email": "example@gmail.com",
        }
    ]

    mailer.set_mail_from(mail_from, mail_body)
    mailer.set_mail_to(recipients, mail_body)
    mailer.set_subject("Hello", mail_body)
    mailer.set_html_content("Hi, dev. This is a chance for you.", mail_body)
    mailer.set_plaintext_content("VerdantVibes", mail_body)
    mailer.set_reply_to(reply_to, mail_body)

    mailer.send(mail_body)
