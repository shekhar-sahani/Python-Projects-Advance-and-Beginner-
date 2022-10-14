import pyqrcode 
from pyqrcode import QRCode
import png 
  
# String which represent the QR code 
s = "https://upcoming-anime.vercel.app/"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.png('myqr.png', scale=8)
