class kucing:
   def cakar(self):
        print('sing sing sing')

   def dry_food(self):
        print('haph..')
    
class britis_short_hair(kucing):
    british_sound = "meow meow meow"

    def ramah(self):
        print('ramah..')
    
    def angry(self):
        print('not funny')
    
    def miaw1(self,miaw_new_sound=""):
        self.british_sound = miaw_new_sound or self.british_sound
        print(self.british_sound)

class siberian(kucing):
    siber_sound = 'miaoo....'

    def masa_hidup(self):
        print('not longer..')
    
    def bulu(self):
        print('ketebalan')
    
    def miaw2(self,miao_new_sound=""):
        self.siber_sound = miao_new_sound or self.siber_sound
        print(self.siber_sound)