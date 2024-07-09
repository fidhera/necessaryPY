# Program Spam Chattttttttttttttttttttttttttttttt
import pyautogui as pt
import time

limit = input("Enter limit:") # Input Jumlah Pesan
message = input("Enter message:") # Input Kata Yang Ingin Dikirim
i = 0
time.sleep(5)

while i < int(limit):
    pt.typewrite(message)
    # pesan ditulis ketika cursor berada di box input
    pt.press("enter")

    i+=1
