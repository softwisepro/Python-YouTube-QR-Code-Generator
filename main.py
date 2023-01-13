# This project is developed by Eric Kweyunga.
# This project belongs to Petonia and it is free to be shared among the programmers.
# it is an opensource anyone can edit the codes and generate his/her own functionalities.

# For your program to run this program correctly you need to read the read_me.txt document.

import sys
import pyqrcode 
from pyqrcode import QRCode 
  
# Link to your Youtube channel
qrc = input('Enter a link to your youtube channel: ')
   
# Create and save the png file naming "youtubeqrc.png"
argument = input('do you want to create a qrcode for your Youtube channel(yes/no): ')

while True:
    
    # function generate qr code
    def generate_qr_code():
        # Generate QR code
        url = pyqrcode.create(qrc)
        url.svg("youtubeQRcode.svg", scale = 10)

    # function run
    def run():
        # Generate QR code function
        generate_qr_code()
        print('Your youtube QRcode was successfully generated')

    # function exit from program
    def exit_program():
        # exit program
        exit()


    if argument.lower().startswith("y"):
        run()
        break

    elif argument.lower().startswith("n"):
        print('Your request was canceled')
        run()
        break
        
    else:
        print('Choose "y" for yes & "n" for no')
        run()
        
exit_program()
    
    
