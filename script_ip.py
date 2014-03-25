import smtplib
import os, sys
    
def send_mail(ip):
        SMTP_SERVER = "smtp.gmail.com"
        SMTP_PORT = 587

	session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
	session.ehlo()
	session.starttls()
	session.login('raspcam@gmail.com', 'raspcam123')
	session.sendmail('raspcam@gmail.com', ['mcdlima@gmail.com'], ip)
	print "Email enviado"
	session.quit()
	
ip_public = "ip_public " + os.popen("wget http://ipecho.net/plain && cat plain && rm plain").read() + "\n"

eth0 =os.popen("ifconfig eth0 | grep \"inet addr\"").read()
if eth0 != "":
	eth0 = "ip_local eth0: " + eth0.split(":")[1].split(" ")[0] + "\n"
	
eth1 = os.popen("ifconfig eth1 | grep \"inet addr\"").read()
if eth1 != "":
	eth1 = "ip_local eth1: " + eth1.split(":")[1].split(" ")[0] + "\n"

wlan0 = os.popen("ifconfig wlan0 | grep \"inet addr\"").read()
if wlan0 != "":
	wlan0 = "ip_local wlan0: " + wlan0.split(":")[1].split(" ")[0] + "\n"
	
send_mail(ip_public + eth0 + eth1 + wlan0)
