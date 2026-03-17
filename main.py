import functools

functools.cache
def fatRec(a:int) -> int:
    '''
    recursive factorial with cache, so it runs faster 
    '''
    if a <= 1:
        return 1
    else:
        return a * fatRec(a-1)


while True:
    try:
        print('digite 0 para sair')
        n = int(input('digite um numero '))
        if n == 0:
            break 
        print(fatRec(n))
    except:
        print ('numero errado tente novamente ') 