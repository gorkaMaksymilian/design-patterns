from ObliczPodatek import ObliczPodatek

class PodatekNiemcy(ObliczPodatek):
    def kwotaPodatku(self, kwota):
        return kwota*0.30
