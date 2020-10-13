import pyb
lcd = pyb.LCD('X')
lcd.light(True)
lcd.write('Hello uPy!\n')
