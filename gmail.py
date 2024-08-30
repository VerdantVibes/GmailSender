from mailersend import emails

def SendEmail():
    mailer = emails.NewEmail('mlsn.09d5bd78dcbbc4582470aa1e1b00af184c32320a51b1fd97ca6d2574aaa658e0')

    mail_body = {}

    mail_from = {
        "name": "Hassam",
        "email": "MS_0gIZpS@trial-zr6ke4nozmelon12.mlsender.net",
    }

    recipients = [
        {
            "name": "normanscott",
            "email": "normanscott1211@gmail.com",
        }
    ]

    reply_to = [
        {
            "name": "normanscott",
            "email": "normanscott1211@gmail.com",
        }
    ]

    mailer.set_mail_from(mail_from, mail_body)
    mailer.set_mail_to(recipients, mail_body)
    mailer.set_subject("There is booking on Pakistan site!", mail_body)
    mailer.set_html_content("Hi, dev. This is a chance for you. Please close the booking.", mail_body)
    mailer.set_plaintext_content("There is booking on Pakistan site", mail_body)
    mailer.set_reply_to(reply_to, mail_body)

    mailer.send(mail_body)