n = int(input('Digite um número: '))
print('O dobro de {} vale {}\nO triplo de {} vale {}'.format(n, (n*2), n, (n*3)))
print('A raiz quadrada de {} vale {:.2f}'.format(n, (n**(1/2))))

#ou

n = int(input('Digite um número: '))
print('O dobro de {} vale {}\nO triplo de {} vale {}'.format(n, (n*2), n, (n*3)))
print('A raiz quadrada de {} vale {:.2f}'.format(n, pow(n, (1/2))))
