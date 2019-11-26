import pyqrcode
from pyqrcode import QRCode
import sys


def generateQR():
    issuer = "ACME%20Co"
    account = "chief@yahooligans.com"
    key = "HXDMVJECJJWSRB3HWIZR4IFUGFTMXBOZ"
    uriStr = f"otpauth://totp/{issuer}:{account}?secret={key}&issuer={issuer}"
    uri = pyqrcode.create(uriStr)
    uri.svg("myqr.svg", scale = 10)

# def generateOTP():


def main():
#   call functions here
    generateQR()
  
if __name__== "__main__":
  main()

