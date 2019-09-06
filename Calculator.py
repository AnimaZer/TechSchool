from kivy.app import App
#добавление нужных виджетов
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.anchorlayout import AnchorLayout
#хабариты
from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '500')

class CalculatorApp(App):
    def build(self):
        bl = BoxLayout(orientation = 'vertical')
        gl = GridLayout(cols = 5, size_hint = (1, .6)) 

        self.lbl = Label(text = "0", font_size = 40, text_size = (300, 500 * .4), size_hint = (1, .4), halign = "right", valign = "center" )
        bl.add_widget(self.lbl)
        self.formula = "0"

        gl.add_widget(Button(text = "2с.с.", on_press = self.ss))
        gl.add_widget(Button(text = "8с.с.", on_press = self.ss))
        gl.add_widget(Button(text = "10с.с.", on_press = self.ss))
        gl.add_widget(Button(text = "16с.с.", on_press = self.ss))
        gl.add_widget(Button(text = "inf", on_press = self.inf))

        gl.add_widget(Button(text = "7", on_press = self.add_num))
        gl.add_widget(Button(text = "8", on_press = self.add_num))
        gl.add_widget(Button(text = "9", on_press = self.add_num))
        gl.add_widget(Button(text = "*", on_press = self.add_operation))
        gl.add_widget(Button(text = "квадрат", on_press = self.sqare))

        gl.add_widget(Button(text = "4", on_press = self.add_num))
        gl.add_widget(Button(text = "5", on_press = self.add_num))
        gl.add_widget(Button(text = "6", on_press = self.add_num))
        gl.add_widget(Button(text = "-", on_press = self.add_operation))
        gl.add_widget(Button(text = "корень", on_press = self.sqare))

        gl.add_widget(Button(text = "1", on_press = self.add_num))
        gl.add_widget(Button(text = "2", on_press = self.add_num))
        gl.add_widget(Button(text = "3", on_press = self.add_num))
        gl.add_widget(Button(text = "+", on_press = self.add_operation))
        gl.add_widget(Button(text = "<-", on_press = self.clear))
        
        gl.add_widget(Button(text = ".", on_press = self.add_num))
        gl.add_widget(Button(text = "0", on_press = self.add_num))
        gl.add_widget(Button(text = "=", on_press = self.result))
        gl.add_widget(Button(text = "/", on_press = self.add_operation))
        gl.add_widget(Button(text = "C", on_press = self.clear))

        bl.add_widget(gl)
        return bl
    
    def clear(self, instance):
        if(str(instance.text).lower() == "<-"):
            self.formula = str(self.formula)[:-1]
            if self.formula == "":
                self.formula = "0"
        else:
            self.formula = str("0")
        self.update_label()

    def ss(self, instance):
        if(str(instance.text).lower() == "2с.с."):
            self.formula = str(bin(int(self.formula)))[2:]
            self.update_label()
            self.formula = str(int(self.formula, 2))
        elif(str(instance.text).lower() == "8с.с."):
            self.formula = str(oct(int(self.formula)))[2:]
            self.update_label()
            self.formula = str(int(self.formula, 8))
        elif(str(instance.text).lower() == "10с.с."):
            self.formula = str(self.formula)
            self.update_label()
        elif(str(instance.text).lower() == "16с.с."):
            self.formula = str(hex(int(self.formula)))[2:]
            self.update_label()
            self.formula = str(int(self.formula, 16))
        
        #self.formula = "0"

    def sqare(self, instance):
        if(str(instance.text).lower() == "квадрат"):
           self.formula = str(float(self.formula)**2)
        elif(str(instance.text).lower() == "корень"):
           self.formula = str(float(self.formula)**(1/2))

        self.update_label()

    def inf(self, instance):
        self.lbl.text = str("Сделал илюшко :0")
        self.formula = "0"

    def update_label(self): #обновление лейбла
        self.lbl.text = self.formula
    
    def add_num(self, instance): #добавление числа
        if(self.formula == "0"):
           self.formula = ""
        
        self.formula += str(instance.text)
        self.update_label()
    
    def add_operation(self, instance): #добавление знаков операции
        l = len(str(self.formula))
        if( str(self.formula)[l-1] =="*" and str(self.formula)[l-2] =="/"):
           self.formula[l-2] = "*"
        else:
           self.formula += str(instance.text)
        self.update_label()
    
    def result(self, instance):
        #l = len(str(self.formula))
        #if str(self.formula)[l-1] =="0" and str(self.formula)[l-2] =="/":
        #    self.formula = "0"
        #    self.update_label()
        #else:
        self.lbl.text = str(eval(self.lbl.text))
        self.formula = "0"

if __name__ == "__main__":
    CalculatorApp().run()