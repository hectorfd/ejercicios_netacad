beatles = []

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

for i in range(2):
    value = str(input("Introduce el nombre del beatle: "))
    beatles.append(value)

print(beatles)
    
for j in range(2):
    del beatles[-1]

beatles.insert(0, "Ringo Starr")
print(beatles)
