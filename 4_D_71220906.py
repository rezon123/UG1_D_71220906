print("--------Nilai ke 1--------")
nilaiharian=int(input("masukkan nilai harian  : "))
nilaiuts=int(input("masukkan nilai uts  : "))
nilaiuas=int(input("masukkan nilai uas  : "))

print("--------Nilai ke 2--------")     
nh=int(input("masukkan nilai harian  : "))
nu=int(input("masukkan nilai uts  : "))
nua=int(input("masukkan nilai uas  : "))
harian=nilaiharian*30/100 
uts=nilaiuts*30/100 
uas=nilaiuas*40/100 

nilai_yang_didapat=harian+uts+uas

# print("Nilai Harian     : %d" %harian)
# print("Nilai UTS        : %d" %uts)
# print("Nilai UAS        : %d" %uas)
# print("Nilai yang didapat      :" , float(nilai_yang_didapat))

if nilai_yang_didapat >= 100 :
    print("\nNilai Huruf    : A")
elif nilai_yang_didapat >= 79 :
    print("\nNilai Huruf    : B")
elif nilai_yang_didapat >= 59 :
    print("\nNilai Huruf    : C")
elif nilai_yang_didapat >= 39 :
    print("\nNilai Huruf    : D")
elif nilai_yang_didapat <= 19 :
    print("\nNilai Huruf    : E")

if nilai_yang_didapat >=71 :
    print("nilai yang didapat   : 71.0")
else :
    print("nilai yang didapat   : 49.0")

