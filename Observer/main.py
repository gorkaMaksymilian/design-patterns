from ConcreteObserver import ConcreteObserver
from ConcreteSubject import ConcreteSubject

if __name__ == '__main__':
    first_subject = ConcreteSubject()
    second_subject = ConcreteSubject()

    first_observer = ConcreteObserver(first_subject, 'Obserwator 1')
    second_observer = ConcreteObserver(first_subject, 'Obserwator 2')
    third_observer = ConcreteObserver(second_subject, 'Obserwator 3')


    first_subject.SetState()

