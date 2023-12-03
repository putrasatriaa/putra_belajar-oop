class anjing:
    def gigit(self):
        print('arrghharghhh....')
    
    def daging(self):
        print('emmmmmph')

class shepherd(anjing):
    shep_sound = 'gugh gugh gugh'

    def penciuman_tajam(self):
        print('hmmmpphh')

    def kekuatan_lari(self):
        print('Im speed......')
    
    def bark1(self,bark_new_sound = ""):
        self.shep_sound = bark_new_sound or self.shep_sound
        print(self.shep_sound)

class husky(anjing):
    husk_sound = 'hurgh hurgh hurgh'
   
    def iklim(self):
        print("dingin..")
    
    def aktifitas(self):
        print("tinggi")
    
    def bark2(self,bhark_new_sound=""):
        self.husk_sound = bhark_new_sound or self.husk_sound
        print(self.husk_sound)