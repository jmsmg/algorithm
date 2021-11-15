def ft_rec_fibonacci(n):
    if n == 0 or n == 1:
        return (1)
    return ft_rec_fibonacci(n-2) + ft_rec_fibonacci(n-1) 

print(ft_rec_fibonacci(2))
