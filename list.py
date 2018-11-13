# access value in the Python list

list1 = ['fisika', 'kimia', 1993, 2017]
list2 = [1, 2, 3, 4, 5, 6, 7]

print ("list[0]: ", list1[0])
print ("list[1:5]: ", list2[1:5])
 
#UPDATE NILAI DALAM LIST PYTHON

print ("=====================")

list = ['fisika', 'kimia', 193, 2017]
print ("Nilai ada pada index : ", list[2])

list[2] = 2001
print ( "NIlai baru ada pada index 2 : ", list[2])

#HAPUS NILAI DALAM LIST PYTHON
print ("=====================")

list = ['fisika','kimia', 1993, 2017]

print (list)
del list[2]
print ("Setelah dihapus nilai pada index 2 : ", list)
