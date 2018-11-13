
#AKSES NILAI DALAM TUPLE PYTHON
print ("=================")

tup1 = ('fisika', 'kimia', 1993, 2017)
tup2 = (1, 2, 3, 4, 5, 6, 7)

print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])

#UPDATE NILAI DALAM TUPLE PYTHON
print ("================")

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

#AKSI SEPERTI DIBAWAH INI TIDAK BISA DILAKUKAN PADA TUPLE PYTHON
#KARENA MEMANG NILAI PADA TUPLE PYTHON TIDAK BISA DIUBAH
#tup1[0] = 100;

#JADI, BUATLAH TUPLE BARU SEBAGAI BERIKUT
tup3 = tup1+tup2
print (tup3)

#HAPUS NILAI DALAM TUPLE PYTHON
print ("===============")

tup = ('fisika', 'kimia', 1993, 2017);

print (tup)
del tup;
print "Setelah menghapus tuple : "
print tup
