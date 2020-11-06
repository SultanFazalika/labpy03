modal=100000000
a=modal*0
b=modal*(1/100)
c=modal*(5/100)
d=modal*(2/100)
for x in range(1,3):
    print("Laba bulan ke-", x, "sebesar: ", a)
for y in range(3,5):
    print("Laba bulan ke-", y, "sebesar: ", b)
for z in range(5,8):
    print("Laba bulan ke-", z, "sebesar: ", c)
for zz in range(8,9):
    print("Laba bulan ke-", zz, "sebesar: ", d)
total=(a*2)+(b*2)+(c*3)+d
print("Total laba adalah: ", total)