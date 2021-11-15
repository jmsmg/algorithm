def console():
    if input('>') == 'exit':
        return None
    if input('>') == 'hi':
        print('hello world')
    console()
console()
