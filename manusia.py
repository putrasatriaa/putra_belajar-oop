class Manusia:
    def makan(self):
        print("makan...")

    def minum(self):
        print("minum...")

    def nafas(self):
        print("nafas...")

    def tidur(self):
        print("tidur...")


class Anak(Manusia):
    nangis_sound = "Oek Oek"

    def __init__(self, new_nangis_sound=""):
        self.nangis_sound = new_nangis_sound or self.nangis_sound
        #print(new_nangis_sound)

    def nangis(self, new_nangis_sound):
        self.nangis_sound = new_nangis_sound
        print(self.nangis_sound)

    def nangis2(self, suara_nangis=""):
        print(suara_nangis or self.nangis_sound)

    def minum_susu(self):
        print("Gluk Gluk")


class Remaja(Manusia):
    tawuran_sound = "Ora ora"

    def bandel(self):
        print("sini loo")

    def tawuran(self):
        print(self.tawuran_sound)
        print(self.tawuran_sound)
        print(self.tawuran_sound)
        print(self.tawuran_sound)
        print(self.tawuran_sound)


human = Manusia()
putra = Remaja()

prabu = Anak("Huwe Huqw")  # Oek Oek

prabu.nangis2()
prabu.nangis("sakittttttt")
prabu.nangis2("yeayyyyy")
# prabu.nangis("yeeeeeee")
# prabu.nangis("yahs")
