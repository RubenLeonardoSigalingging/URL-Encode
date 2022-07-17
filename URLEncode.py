#!/usr/bin/env python3


from os import system
import sys
import urllib.parse


def URL_Encode(Website):
	return (Website)


def URL_Decode(Website):
	return (Website)


import pyfiglet
Judul=pyfiglet.Figlet(font="cybermedium")
print("\033[92m")
print(Judul.renderText("URLEnc"))
print("\033[91m[\033[94m1\033[91m] \033[94mURL Encode Tool")
print("\033[91m[\033[94m2\033[91m] \033[94mURL Decode Tool\n")

Pilih=int(input("\033[91m[\033[94m!\033[91m] \033[94mPilih: \033[92m"))
if Pilih==1:
	if sys.platform=="win32" or sys.platform=="win64":
		system("cls")
		Judul=pyfiglet.Figlet(font="cybermedium")
		print("\033[92m")
		print(Judul.renderText("URLEnc"))
		Website=input("\033[91m[\033[94m!\033[91m] \033[94mWebsite: \033[92m")
		Website=Website.__str__()
		print("\n")
		Website=urllib.parse.quote_plus(Website)
		print(f"\033[91m[\033[94m!\033[91m] \033[94mURL Encode: \033[92m{Website}")


	elif sys.platform=="linux" or sys.platform=="linux2" or sys.platform=="linux3":
		system("clear")
		Judul=pyfiglet.Figlet(font="cybermedium")
		print("\033[92m")
		print(Judul.renderText("URLEnc"))
		Website=str(input("\033[91m[\033[94m!\033[91m] \033[94mWebsite: \033[92m"))
		Website=urllib.parse.quote_plus(Website)
		print("\n")
		print(f"\033[91m[\033[94m!\033[91m] \033[94mURL Encode: \033[92m{Website}")


elif Pilih==2:
	if sys.platform=="win32" or sys.platform=="win64":
		system("cls")
		Judul=pyfiglet.Figlet(font="cybermedium")
		print("\033[92m")
		print(Judul.renderText("URLEnc"))
		Website=str(input("\033[91m[\033[94m!\033[91m] \033[94mWebsite: \033[92m"))
		Website=urllib.parse.unquote_plus(Website)
		print("\n")
		print(f"[!] URL Decode: {Website}")


	elif sys.platform=="linux" or sys.platform=="linux2" or sys.platform=="linux3":
		system("clear")
		Judul=pyfiglet.Figlet(font="cybermedium")
		print("\033[92m")
		print(Judul.renderText("URLEnc"))
		Website=str(input("\033[91m[\033[94m!\033[91m] \033[94mWebsite: \033[92m"))
		Website=urllib.parse.unquote_plus(Website)
		print("")
		print(f"\033[91m[\033[94m!\033[91m] \033[94mURL Decode: \033[92m{Website}")