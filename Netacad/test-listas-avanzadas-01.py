squares = [2 ** i for i in range(10)]

odds = [x for x in squares if x % 2 != 0 ]

temps = [[0.0 for h in range(24)] for d in range(31)]

print(temps)

print(squares)
print(odds)

cubed = [num ** 3 for num in range(5)]
print(cubed)  # output: [0, 1, 8, 27, 64]

table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]
 
print(table)
print(table[0][0])  # output: ':('
print(table[0][3])  # output: ':)' 


cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],
 
        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],
 
        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]
 
print(cube)
print(cube[0][0][0])  # output: ':('
print(cube[2][2][0])  # output: ':)'
  


var = 1
while var < 10:
    print("#")
    var = var << 1

#Iteraciones:
#var = 1 → imprime #

#var = 2 → imprime #

#var = 4 → imprime #

#var = 8 → imprime #

#var = 16 → ya no entra al while (16 >= 10)