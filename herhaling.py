repeat = True

while repeat == True: 
    vraag = input('grote? ')

    if vraag == 'small':
        repeat = False
    elif vraag == 'medium':
        repeat = False
    elif vraag == 'large':
        repeat = False
    else:
        print('fout')

repeat = True

while repeat == True: 
    aantal = input('aantal? ')

    if aantal.isdigit() and int(aantal) < 12:
        repeat = False