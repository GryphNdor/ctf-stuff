from egcd import egcd

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
phi = (p - 1)*(q - 1)


gfc, a, b = egcd(e,phi)

print(a)