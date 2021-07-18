abc = "abcdefghijklmnopqrstuvwxyz"

def print_rangoli(size):
    lim = abc[:size]
    lett = ''
    #print(lim,size)
    for i in range(size-1,-1,-1):
        lett = lett[:((size-1)-i)] + lim[i] + lett[:((size-1)-i)][::-1]
        new = list(lett)
        new = '-'.join(lett)
        #print(new)
        print((new).center((((size*4)-4) + 1), '-'))
    for i in range(1,size):
        lett = lett[:((size-1)-i)] + lim[i] + lett[:((size-1)-i)][::-1]
        new = list(lett)
        new = '-'.join(lett)
        #print(new)
        print((new).center((((size*4)-4) + 1), '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
