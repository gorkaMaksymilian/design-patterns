from Proxy import Proxy

if __name__ == '__main__':
    proxy = Proxy()

    while True:
        print('podaj a: ', end = '')
        a = input()
        print('podaj b: ', end = '')
        b = input()
        print('podaj c: ', end = '')
        c = input()

        wynik = proxy.licz(int(a), int(b), int(c))
        if wynik != None:
            print(f'\n{wynik=}')
        else:
            print('\nBrak rozwiazan')



        x = input('Aby wyjsc wybierz 1\nBy kontynuowac wpisz dane != 1\n')
        if x == '1':
           break

