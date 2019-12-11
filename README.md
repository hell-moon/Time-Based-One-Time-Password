Time Based One Time Password

This is a python3 script that can generate a qr code with the URI that Google' Authenticator app expects.

This script depends on the pyqrcode library.  
    If not already installed on flip server, can be installed with:
        pip3 install --user pyqrcode

The script takes one argument, with two possible options:
    Option 1:
        [--generate-qr]
            This will create a .svg file with the following URI encoded QR code:
            "otpauth://totp/ACME%20Co:chief@yahooligans.com?secret=HXDMVJECJJWSRB3HWIZR4IFUGFTMXBOZ&issuer=ACME%20Co"
            Scanning the QR code with the Google Authenticator app will add this example account to the app and 
            generate the corresponding OTP every 30 seconds
    Option 2:
        [--get-otp]
            This will take the key from the QR code and generate the TOTP according to the RFC 6238
            The script will continue to run until stopped (ctrl+c)
            Every 30 seconds it will generate the new OTP 

