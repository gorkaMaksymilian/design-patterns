from FileState import FileState

class FileClosed(FileState):
    def Open(self):
        print('Otwieram plik.')
        from FileOpened import FileOpened
        return FileOpened()

    def Close(self):
        print('Plik jest juz zamkniety.')
        return self

    def Read(self):
        print('Plik jest zamkniety nie moge czytac.')

    def Write(self):
        print('Plik jest zamkniety nie moge pisac.')
