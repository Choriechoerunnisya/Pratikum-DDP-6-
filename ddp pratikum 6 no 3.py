string = " "
bar = 1

x =int (input("masukan angka = "))

while bar <= x:
    kol = bar

    while kol <= x:
        string = string + "*"
        kol = kol - 1
    string = string + " "
    bar = bar - 1
    print(string)
    
