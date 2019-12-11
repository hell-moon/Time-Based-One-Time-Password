'''
    Xiao Kuang
    CS370-Programming Project 2
    This program can incorporate a Google Authenticator URI into a QR code, 
    and also generate an OTP that mirrors the same TOTP that GA will generate
'''


# comment out because flip servers dont support pyqrcode library
import pyqrcode
from pyqrcode import QRCode

import sys
import hmac
import hashlib
import struct
import time
import base64


# comment out because flip servers don't support pyqrcode library
def generateQR(key):
    '''
        URI must match this format: https://github.com/google/google-authenticator/wiki/Key-Uri-Format
    '''
    issuer = "ACME%20Co"
    account = "chief@yahooligans.com"
    uriStr = f"otpauth://totp/{issuer}:{account}?secret={key}&issuer={issuer}"
    uri = pyqrcode.create(uriStr)
    # create svg qr code picture
    uri.svg("myqr.svg", scale = 10)


def Truncate(hmac_sha1_digest):
    """5.4.  Example of HOTP Computation for Digit = 6

   The following code example describes the extraction of a dynamic
   binary code given that hmac_result is a byte array with the HMAC-
   SHA-1 result:

        int offset   =  hmac_result[19] & 0xf ;
        int bin_code = (hmac_result[offset]  & 0x7f) << 24
           | (hmac_result[offset+1] & 0xff) << 16
           | (hmac_result[offset+2] & 0xff) <<  8
           | (hmac_result[offset+3] & 0xff) ;
    """
    offset = int(hmac_sha1_digest[-1],16) 
    binary = int(hmac_sha1_digest[(offset*2):((offset*2)+8)], 16) & 0x7fffffff
    return str(binary)

def HOTP(K, C):
    #   step 1: generate HMAC-SHA-1 value, let HS = HMAC-SHA1(K,T)
    hmac_sha1_digest = hmac.new(key = base64.b32decode(K), msg = struct.pack(b"!Q", C), digestmod=hashlib.sha1).hexdigest()
    # print("digest: {}",hmac_sha1_digest)
    return Truncate(hmac_sha1_digest)[-6:]

def generateTOTP(K):
    '''
        T = unix time in seconds divided by the 30 second window size
    '''
    windowSeconds = 30
    clock = time.time()
    T = int(clock/windowSeconds)
    return HOTP(K,T)

def main():
    '''
        the same key must be passed to the qr code and the totp functions
    '''
    key = "HXDMVJECJJWSRB3HWIZR4IFUGFTMXBOZ"
    oldotp = None

#   call functions here
 #comment this out because qr code part of code does not work on flip servers (library not supported)
    if (sys.argv[1] == '--generate-qr'):
        generateQR(key)
    elif (sys.argv[1] == '--get-otp'):


    # if (sys.argv[1] == '--get-otp'):
        while(True):
            # check if otp has changed, every 5 seconds
            otp = generateTOTP(key)
            if otp != oldotp:
                print(otp)
                oldotp = otp
            time.sleep(1)
    else:
        print("Error, please use one of these arguments\n\t1. --generate-qr\n\t2.  --get-otp\n")
  
  
if __name__== "__main__":
  main()

