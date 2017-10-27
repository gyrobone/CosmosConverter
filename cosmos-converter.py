def miles_to_km(miles):
    try:
        m = int(miles)
    except ValueError:
        print("Please Type Number")
        return
    km = m * 1.60934
    print("Kilometers: ~" + str(km))

def km_to_au(kilometers):
    try:
        km = int(kilometers)
    except ValueError:
        print("Please Type Number")
        return
    au = km * 6.68459e-9
    print("Astronomical Units: ~" + str(au))

def au_to_ly(astro_units):
    try:
        au = int(astro_units)
    except ValueError:
        print("Please Type Number")
        return
    ly = au * 1.5813e-5
    print("Lightyears: ~" + str(ly))

def ly_to_au(lightyears):
    try:
        ly = int(lightyears)
    except ValueError:
        print("Please Type Number")
        return
    au = ly * 63241.1
    print("Astronomical Units: ~" + str(au))

def ly_to_pc(lightyears):
    try:
        ly = int(lightyears)
    except ValueError:
        print("Please Type Number")
        return
    pc = ly * 0.306601
    print("Parsecs: ~" + str(pc))

def pc_to_kpc(parsecs):
    try:
        pc = int(parsecs)
    except ValueError:
        print("Please Type Number")
        return
    kpc = pc * 0.001
    print("Kiloparsecs: ~" + str(kpc))

def kpc_to_Mpc(kiloparsecs):
    try:
        kpc = int(kiloparsecs)
    except ValueError:
        print("Please Type Number")
        return
    Mpc = kpc * 0.001
    print("Megaparsecs: ~" + str(Mpc))

def convert(value, start_unit):
    try:
        n = int(value)
    except ValueError:
        print("Please Type Number")
        return
    unit = start_unit.lower()
    if unit=="miles":
        miles_to_km(n)
    elif unit=="km":
        km_to_au(n)
    elif unit == "au":
        au_to_ly(n)
    elif unit == "ly":
        ly_to_pc(n)
        ly_to_au(n)
    elif unit == "pc":
        pc_to_kpc(n)
    elif unit == "kpc":
        kpc_to_Mpc(n)
    else:
        print("Please Enter Valid Unit")

value = input("Value?")
unit = input("Unit?")
convert(value, unit)