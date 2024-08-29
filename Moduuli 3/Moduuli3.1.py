fish = float(input("Kuinka pitkä kala on? Ilmoita luku senttimetreinä: "))

if fish < 37:
    print(f"Kala on {37.0 - fish}cm alle sallitun rajan. Sallittu pituus on yli 37cm")
    print("Laske kala veteen!")

else:
    print("Hieno homma! Sait kalan!")