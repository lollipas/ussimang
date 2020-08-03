
import tkinter
from tkinter import messagebox
import random
import time
ploki_suurus = 20


#NB!
#USS SOOB TOIDU AINULT SIIS ARA KUI TA LAHEB KOGU PEA OSAS SELLE VASTU!




class Uss:
    def __init__(self,aken,varv):
        self.aken = aken
        
        
        self.keha_x=0
        self.keha_y=0
        self.pea_x= 0
        self.pea_y = 0
        self.ussi_positsioonid=[(100,100),(80,100),(60,100)]   
        self.ouna_positsioonid = self.ouna_spawn()
        self.skoor = 0
        self.uss_pilt = tkinter.PhotoImage(file="uss.ppm") 
        self.oun_pilt = tkinter.PhotoImage(file = "oun.ppm")
        self.coords = self.aken.coords
        aken.create_image(*self.ouna_positsioonid, image = self.oun_pilt, tag="oun")     
        self.aken.height = self.aken.winfo_height()
        self.aken.width = self.aken.winfo_width()
        self.liikumis_suund = "Right"
        self.aken.bind_all("<Key>", self.klaviatuur)
        self.kaotus = False

        
        for xpositsioon1,ypositsioon1 in self.ussi_positsioonid:    
            self.uss = aken.create_image(xpositsioon1,ypositsioon1, image=self.uss_pilt, tags = "uss")
            

        
   
    def ouna_soomine(self):
        print(self.ussi_positsioonid,self.ouna_positsioonid)    
        if self.ussi_positsioonid[0] == self.ouna_positsioonid:    
            self.ussi_positsioonid.append(self.ussi_positsioonid[-1])
            self.skoor += 1
            aken.create_image(*self.ussi_positsioonid[-1], image=self.uss_pilt, tags = "uss")  
            self.ouna_positsioonid = self.ouna_spawn()
            self.coords(aken.find_withtag("oun"), *self.ouna_positsioonid)
               


    def ouna_spawn(self):
        while True:
            x_positsioon = random.randint(1, 29) * 10
            y_positsioon = random.randint(3, 30) * 10
            ouna_positsioon = (x_positsioon, y_positsioon)

            if  ouna_positsioon not in self.ussi_positsioonid:
                return ouna_positsioon

                

    def liigu(self):
        
 
        self.uss_pea_asukohtX1,self.uss_pea_asukohtY1 = self.ussi_positsioonid[0]

        
        if self.liikumis_suund == "Up":
             uus_pea_positsioon = (self.uss_pea_asukohtX1, self.uss_pea_asukohtY1 - 10)
             
        elif self.liikumis_suund == "Down":
            uus_pea_positsioon = (self.uss_pea_asukohtX1, self.uss_pea_asukohtY1 + 10)
            
        elif self.liikumis_suund == "Right":
            uus_pea_positsioon = (self.uss_pea_asukohtX1 + 10, self.uss_pea_asukohtY1)
            
        elif self.liikumis_suund == "Left":
            uus_pea_positsioon = (self.uss_pea_asukohtX1 - 10, self.uss_pea_asukohtY1)
            
                  
        self.ussi_positsioonid = [uus_pea_positsioon] + self.ussi_positsioonid[:-1]
       
        for osa, positsioon in zip(aken.find_withtag("uss"), self.ussi_positsioonid):
             aken.coords(osa, positsioon)
             

        if self.uss_pea_asukohtX1>= self.aken.width:
            self.kaotus = True  
                  
            tkinter.messagebox.showinfo('Kaotus', 'Läksid mängualast välja! ' 'Punktide arv: {}'.format(self.skoor))

        if self.uss_pea_asukohtX1<= 0:
            self.kaotus = True 
            tkinter.messagebox.showinfo('Kaotus', 'Läksid mängualast välja! ' 'Punktide arv: {}'.format(self.skoor))
        
        if self.uss_pea_asukohtY1 >= self.aken.height:
            self.kaotus = True
            tkinter.messagebox.showinfo('Kaotus', 'Läksid mängualast välja! ' 'Punktide arv: {}'.format(self.skoor))
        if self.uss_pea_asukohtY1 <= 0:
            self.kaotus = True
            tkinter.messagebox.showinfo('Kaotus', 'Läksid mängualast välja! ' 'Punktide arv: {}'.format(self.skoor))
        if (self.uss_pea_asukohtX1,self.uss_pea_asukohtY1) in self.ussi_positsioonid[2:]:
            self.kaotus = True
            tkinter.messagebox.showinfo('Kaotus', 'Sõid ennast ära! Punktide arv: {}'.format(self.skoor))
            

    def klaviatuur(self, e):
        uus_suund = e.keysym

        k6ik_suunad= ("Up", "Down", "Left", "Right")
        vastas_suunad = ({"Up", "Down"}, {"Left", "Right"})

        if (
            uus_suund in k6ik_suunad
            and {uus_suund, self.liikumis_suund} not in vastas_suunad
        ):
            self.liikumis_suund = uus_suund


tk = tkinter.Tk()
tk.title("Ussimäng")
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1) 
aken = tkinter.Canvas(tk,width=400,height=500)
aken.pack()
tk.update()
aken_width = aken.winfo_width()

uss=(Uss(aken,'black'))

while uss.kaotus == False:
    uss.liigu()
    uss.ouna_soomine()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.05)
    
    