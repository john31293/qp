import sys
import requests



URL = 'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1624893932&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d7a2a111e-d551-bad1-c6c0-f1f8b53ba52f&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&pcexp=false&cobrandid=90015'

class a():
    def __init__(self):
        global Status_login
        self.username = input("[-] Email:")
        self.password = input("[-] Password:")
        if Status_login == False:
            self.login()
