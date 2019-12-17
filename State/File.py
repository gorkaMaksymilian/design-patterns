from FileClosed import FileClosed

class File:
    def __init__(self):
        self.current_state = FileClosed()

    def Open(self):
        self.current_state = self.current_state.Open()

    def Close(self):
        self.current_state = self.current_state.Close()

    def Read(self):
        self.current_state.Read()

    def Write(self):
        self.current_state.Write()
