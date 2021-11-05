text = [' + -- + - + - ',
        ' + --- + - +  ',
        ' + -- + - + - ',
        ' + - + - + - + ']

for i in text:
    print(int(i.strip().replace(' ', '').replace('+', '1').replace('-', '0'), 2))

# ord () : char -> int
# chr() : int -> char

j = []

for i in text:
    j.append(chr(int(i.strip().replace(' ', '').replace('+', '1').replace('-', '0'), 2)))

print(''.join(j))
