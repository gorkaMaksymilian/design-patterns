from ObliczPodatek import ObliczPodatek

class PodatekPolska(ObliczPodatek):
    def kwotaPodatku(self, kwota):
        return kwota*0.10
