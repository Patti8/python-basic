#Perulangan dibagi 3:
#While Loop
#For Loop
#Nested Loop

#Example WHILE LOOP
count = 0
while (count < 9):
    print ('The count is:', count)
    count = count + 1

print ("Good bye!")

#Example FOR LOOP
#1
angka = [1,2,3,4,5]
for x in angka:
    print(x)
#2
buah = ["nanas", "apel", "jeruk"]
for makanan in buah:
    print("Saya suka makan", makanan)

#Example NESTED LOOP
i = 2
while(i < 100):
    j = 2
    while(j <= (i/j)):
        if not(i%j): break
        j = j + 1
    if (j > i/j) : print(i, " is prime")
    i = i + 1

print "Good bye!"
