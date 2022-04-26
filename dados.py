# -*- coding: utf-8 -*-
"""
@author: Equipo Rojo Baya (Cruz Anaya Aime Arey, BArrera Reyes Pablo Raziel)
"""
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
import random

class Dado(App):
    #constructor
    def init(self, **kwargs):
        #llamar al constructor de la clase base (App)
        super().__init__(**kwargs)
        #defino un atributo
        
    #evento
    def btnGen_dado(self,obj):
        #Generar el numero en el dado
        num = random.randint(1,6)
        #Cambiar la etiqueta (atributo)
        self.lblNum.text = str(num)

    #Todos los elementos visuales 
    #se definenen o encadenan aqui
    def build(self):
        #definir un layout
        gdl = GridLayout(rows=3,cols=1)
        lblTitulo = Label(text="DADO")
        gdl.add_widget(lblTitulo)
        gdl2 = GridLayout(cols=2)
        lbl_resp = Label(text="Ha caido un:")
        gdl2.add_widget(lbl_resp)
        lblNum = Label(text="6")
        gdl2.add_widget(lblNum)
        gdl.add_widget(gdl2)
        #botón
        btnGen = Button(text="TIRAR")
        btnGen.background_color = [0.80,0.20,0.86,1]
            #Enlazar
        btnGen.bind(on_press=self.btnGen_dado) 
        gdl.add_widget(btnGen)
        #Atributos
        self.lblNum = lblNum
        self.gdl = gdl
        return gdl

if __name__ == '__main__':
    D = Dado()
    D.run()
