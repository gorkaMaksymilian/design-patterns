class Singleton:
    __instance = None

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("It is a Singleton you can not make another instance")
        else:
            Singleton.__instance = self

    def talk(self):
        print("Hello World!")

    def name(self):
        print("Singleton")


