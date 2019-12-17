from ConcreteColleague import ConcreteColleague
from ConcreteMediator import ConcreteMediator

if __name__ == '__main__':
    cwiczenia = ConcreteColleague('1. Cwiczenia zaliczone.')
    egzamin = ConcreteColleague('2. Wyklad (egzamin) zaliczony.')
    konkurs = ConcreteColleague('3. Przedmiot zaliczony.')

    mediator = ConcreteMediator(cwiczenia, egzamin, konkurs)

    cwiczenia.set_mediator(mediator)
    egzamin.set_mediator(mediator)
    konkurs.set_mediator(mediator)

    while True:
        print(cwiczenia)
        print(egzamin)
        print(konkurs)
        print('4. Wyjscie z programu.')
        wybor = input('Akcja: ')

        if wybor == '1':
            cwiczenia.changed()
        elif wybor == '2':
            egzamin.changed()
        elif wybor == '3':
            konkurs.changed()
        elif wybor == '4':
            break
        else:
            print(f'Brak akcji dla {wybor}')

