# script to calculate the areas of Tonis raviolis :D

raviolis = input('How many raviolis ya got, Toni? ')
count = 0
areas = []

while count < int(raviolis):
    number = count + 1
    length = input('length of Ravioli #' + str(number) + ': ')
    width = input('width of Ravioli #' + str(number) + ': ')
    area = int(length) * int(width)
    areas.append(area)
    print('OK! Ravioli #' + str(number) + ' is ' + str(area) + '. Next Ravioli!')
    count += 1

print('\nOh, we are out of Raviolis to calculate...')
print('\nHere is a list of your Ravioli areas!! ENJOY!! \n')
print(areas)
