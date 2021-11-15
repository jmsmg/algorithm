def ft_reverse(str):
    if str == '':
        return None
    else:
        ft_reverse(str[1:])
        print(str[0])

print(ft_reverse('hello'))
