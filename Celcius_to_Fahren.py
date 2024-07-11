#program untuk convert celcius ke fahrenheit

#pertama input suhu Celcius
celcius = int(input("Celcius= "))

#menghitung nilai fahrenheit
#dengan rumus suhu celcius yang diinput dikalikan 1,8
#lalu ditambah 32
fahrenheit = celcius * 1.8 + 32

#memformat bilangan desimal
#diambil 2 digit setelah koma
format = ("%.2f" % fahrenheit)

#proses pengoutputan
print(f"Suhu {celcius} C sama dengan {format}F")
