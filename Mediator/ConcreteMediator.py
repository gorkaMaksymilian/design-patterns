from Mediator import Mediator

class ConcreteMediator(Mediator):
    def __init__(self, cwiczenia, egzamin, konkurs):
        self.first_checkbox = cwiczenia
        self.second_checkbox = egzamin
        self.third_checkbox = konkurs

    def disable_checkboxes(self):
        self.first_checkbox.status = False
        self.second_checkbox.status = False
        self.third_checkbox.status = False

    def checkbox_selected(self, select):
        if select == '1':
            if self.first_checkbox.status == False:
                self.first_checkbox.status = True
            else:
                self.disable_checkboxes()
        elif select == '2':
            if self.second_checkbox.status == False:
                self.first_checkbox.status = True
                self.second_checkbox.status = True
            else:
                self.disable_checkboxes()
        elif select == '3':
            if self.third_checkbox.status == False:
                self.first_checkbox.status = True
                self.second_checkbox.status = True
                self.third_checkbox.status = True
            else:
                self.disable_checkboxes()
