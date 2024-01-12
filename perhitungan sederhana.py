# latihan koversi satuan temperatur
# program konversi celcius ke lainnya

print("PROGRAM KONVERSI TEMPERATURE")

celcius = float(input("Masukan Suhu :"))
print("suhunya adalah", celcius, "C")

# reamur
reamur = (4/5) * celcius
print("suhunya adalah", reamur, "R")

# fahrenheit 
fahrenheit = ((9/5) * celcius) + 32
print("suhunya adalah", fahrenheit, "F")

# kelvin
kelvin = celcius + 273
print("suhunya adalah", kelvin, "K")


# PR

# program konversi fahrenheit ke lainnya

# fahrenheit ke kelvin
fahrenheit_kelvin = ((fahrenheit - 32) * 5/9) + 273.15
print("suhunya adalah", fahrenheit_kelvin, "K")

# program konversi kelvin ke lainnya
kelvin_fahrenheit = (1.8 * (kelvin - 273)) + 32
print("suhunya adalah", kelvin_fahrenheit, "F")
