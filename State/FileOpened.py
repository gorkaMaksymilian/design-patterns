from FileState import FileState

class FileOpened(FileState):
    def Open(self):
        print('Plik jest juz otwarty.')
        return self

    def Close(self):
        print('Zamykam plik.')
        from FileClosed import FileClosed
        return FileClosed()

    def Read(self):
        print('Zapisuje do pliku.')

    def Write(self):
        print('Czytam z pliku.')

