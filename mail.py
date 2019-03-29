import smtplib
import os


class MyMail:
    sender = ''
    recipient = ''
    pwd = ''
    subject = ''
    body = ''

    def __init__(self, e, r, p, s, b):
        self.sender = e
        self.recipient = r
        self.pwd = p
        self.subject = s
        self.body = b
        self.msg = f'Subject: {self.subject}\n\n{self.body}'

    def set_letter(self, subj, body):
        self.subject = subj
        self.body = body

    def email(self):
        try:
            # With will handle open/closing of our resource //arg1 = email server arg2 = port number
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()  # identify ourselves
                smtp.starttls()  # encrypts traffic
                smtp.ehlo()
                smtp.login(self.sender, self.pwd)  # LOGS IN
                smtp.sendmail(self.sender, self.recipient, self.msg)
        except():
            print("Email was not sent successfully...")

def pause():
    programPause = input("Press the <ENTER> key to continue...")

def main():
    option = 0
    mail_obj = MyMail('', '', '', '', '')
    while option != 5:
        os.system("clear")
        print("Email Application\nChoose from the following menu:\n")
        print("[1]. Create mail (will override previous email)")
        print("[2]. Send mail")
        print("[3]. Display your written email")
        print("[4]. Store email in a file")
        print("[5]. Exit")
        option = (input("Option: "))
        os.system('clear')
        if option == '1':
            sender = input("Enter sender's email: ")
            recip = input("Enter recipient email: ")
            pwd = input("Enter SENDERS password ")
            subj = input("Enter subject ")
            body = input("\n\nBody: ")
            os.system('clear')
            mail_obj = MyMail(sender, recip, pwd, subj, body)
        elif option == '2':
            print("Sending email. . .")
            mail_obj.email()
            print("Email successfully sent.\n")
        elif option == '3':
            os.system("clear")
            print("FROM: {0}\nTO: {1}\nSUBJECT: {2}\nBODY: {3}".format(mail_obj.sender,
                                                                       mail_obj.recipient,
                                                                       mail_obj.subject,
                                                                       mail_obj.body))
            print("\n")
            pause()
        elif option == '4':
            s = "FROM: {0}\nTO: {1}\nSUBJECT: {2}\nBODY: {3}".format(mail_obj.sender,
                                                                       mail_obj.recipient,
                                                                       mail_obj.subject,
                                                                       mail_obj.body)
            f_name = input("Enter file name (Will be saved as .txt)\t")+".txt"
            f_obj = open(f_name, "w")
            f_obj.write(s)
            print("File saved.")
            f_obj.close()
            os.system("clear")
        elif option == '5':
            exit()
        else:
            print("Not an option")



if  __name__=='__main__':
    main()





