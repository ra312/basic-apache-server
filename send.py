import smtplib
def send_emails(title,msg):
	server = smtplib.SMTP_SSL('smtp.yandex.com.tr', 465)
	server.ehlo()
	# server.starttls()

	yandex_mail = "akylzhanova.gulnara@yandex.ru"
	yandex_pass = "N7srk@GukaRauan1989"

	send_to_email = "r.akylzhanov@qmul.ac.uk"

	SUBJECT = "I love you"

	title = "My email"



	msg = ("From: %s\r\n  To: %s\r\n\r\n"
	   % (yandex_mail, send_to_email))
	#msg = "Let my people go"
	message = 'Subject: {}\n\n{}'.format(SUBJECT, msg )
	server.login(yandex_mail,yandex_pass)
	#message = 'Subject: {}\n\n{}'.format(title,msg)
	server.sendmail(yandex_mail,send_to_email,msg)
	server.quit()
	print('E-mails successfully sent!')

send_emails('Test Mail', 'Yes its a test mail!')
