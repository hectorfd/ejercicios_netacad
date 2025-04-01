hat_list = [1,2,3,4,5]
number = int(input('enter a number integer as replacement:'))
# replacing the third element
hat_list[2] = number
# delete the last element
del hat_list[-1]

print('la lista es:',hat_list,' y su longitud es:', len(hat_list))