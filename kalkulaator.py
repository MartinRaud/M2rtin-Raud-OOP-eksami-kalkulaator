from math import pi, sqrt

class calc: #loome klassi
    def __init__(self,a,b): #määrame algväärtused igal kutsumisel
        self.a = a # esimese arvu määramine
        self.b = b # teise arvu määramine

    def liitmine(self): #Liitmise meetod              
        return self.a + self.b # väljastab tulemuse
    def lahutamine(self): #Lahutamise meetod              
        return self.a - self.b
    def korrutamine(self): #Korrutamise meetod             
        return self.a * self.b
    def jagamine(self): #Jagamise meetod                
        return self.a / self.b
    def jaak(self): #jäägi meetod                    
        return self.a % self.b
    def astendamine(self): #astendamise meetod                
        return self.a ** self.b
    def ruutjuur(self): #ruutjuure meetod
        return sqrt(self.a) #kasutan math'ist sqrt et leida ruutjuurt
    def ringiP(self): #ringi ümbermõõt
        return 2 * pi * self.a #kasutan math'ist pi et saada pii väärtust
    def ringiS(self): #ringi pindala
        return pi * self.a ** 2 # kasutan jälle piid

a = int(input("Sisesta esimene number: ")) # küsin esimese arvu
b= int(input("Sisesta teine number: ")) # ja teise arvu

kalk = calc(a,b) #loon uue kalkulaatori objektina
while True: #kuni kohtab break käsku
    def menu(): # määrame menüü, 
        x = ('1. Liitmine \n2. lahutamine\n3. korrutamine\n4. jagamine\n5. Jäägi leidmine\n6. Astendamine\n7. Ruutjuure leidmine\n8. Ringi ümbermõõdu leidmine\n9. Ringi pindala leidmine. ')
        print(x) #väljastab eelnevalt kirjutatud menüü valikud
    
    menu() # kutsume menüü
    valik = int(input("Sisestage üks valikutest: ")) # küsime valikut numbrina
    if valik == 1: # Esimene valik oli liitmine
        print("Vastus: ", kalk.liitmine()) #Väljastab liitmise tulemuse
        break # Lõpetab while True 
    elif valik == 2: # Teine valik oli lahutamine
        print("Vastus: ",kalk.lahutamine()) #Väljastab lahutamise tulemuse
        break # Lõpetab while True
    elif valik == 3: # kolmas valik oli korrutamine
        print("Vastus: ",kalk.korrutamine()) #Väljastab korrutamise tulemuse
        break # Lõpetab while True
    elif valik == 4: # neljas valik oli jagamine
        print("Vastus: ",kalk.jagamine()) #Väljastab jagamise tulemuse
        break # Lõpetab while True
    elif valik == 5: # viies valik oli jäägi leidmine
        print("Vastus: ",kalk.jaak()) #Väljastab jäägi tulemuse
        break # Lõpetab while True
    elif valik == 6: # kuues valik oli astendamine
        print("Vastus: ",kalk.astendamine()) #Väljastab astendamise tulemuse
        break # Lõpetab while True
    elif valik == 7: # seitsmes valik oli ruutjuure leidmine
        print("Vastus: ",kalk.ruutjuur()) #Väljastab ruutjuure tulemuse
        break # Lõpetab while True
    elif valik == 8: # kaheksas valik oli ringi ümbermõõdu leidmine
        print("Vastus: ",kalk.ringiP()) #Väljastab ringi ümbermõõdu
        break # Lõpetab while True
    elif valik == 9: # üheksas valik oli ringi pindala leidmine
        print("Vastus: ",kalk.ringiS()) #Väljastab ringi pindala
        break # Lõpetab while True
    elif valik == 0: # lõpetamine ilma mingi tehinguta
        print('Alustage uuesti')
        break # Lõpetab while True