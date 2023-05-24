from tkinter import *


class Application(Frame):
    """GUI-приложение, создающее рассказ на основе пользовательского ввода"""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Создаёт элементы управления"""

        Label(self, text = "Введите данные для создания новой истории").grid(row=0, column=0, columnspan=2, sticky=W)

        Label(self, text = "Имя персонажа:").grid(row = 1,column = 0,sticky = W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row = 1, column = 1, sticky = W)

        Label(self, text = "Существительное во мн.ч.:").grid(row = 2, column = 0, sticky = W)
        self.noun_ent = Entry(self)
        self.noun_ent.grid(row = 2, column = 1, sticky = W)

        Label(self, text = "Глагол в инфинитиве:").grid(row = 3, column = 0, sticky = W)
        self.verb_ent = Entry(self)
        self.verb_ent.grid(row = 3, column = 1, sticky = W)

        Label(self, text = "Прилагательное (-ые):").grid(row = 4, column = 0, sticky = W)
        self.is_itchy = BooleanVar()
        Checkbutton(self,
                    text = "Нетерпеливый",
                    variable = self.is_itchy).grid(row = 4, column = 1, sticky = W)
        
        self.is_joyous = BooleanVar()
        Checkbutton(self,
                    text = "Радостный",
                    variable = self.is_joyous).grid(row = 4, column = 2, sticky = W)
        
        self.is_electric = BooleanVar()
        Checkbutton(self,
                    text = "Электрический",
                    variable = self.is_electric).grid(row = 4, column = 3, sticky = W)
        
        Label(self, text = "Части тела:").grid(row = 5, column = 0, sticky = W)
        self.body_part = StringVar()
        self.body_part.set(None)
        body_parts = ["рука", "нога", "указательный палец руки"]
        column = 1
        for part in body_parts:
            Radiobutton(self,
                        text = part,
                        variable = self.body_part,
                        value = part).grid(row = 5, column = column, sticky = W)
            column += 1
            
        Button(self,
               text = "Создать шедевр",
               command = self.tell_story).grid(row = 6, column = 0, sticky = W)
        
        self.story = Text(self, width = 64, height = 16, wrap = WORD)
        self.story.grid(row=8, column=0, columnspan=4)

    def tell_story(self):
        person = self.person_ent.get()
        noun = self.noun_ent.get()
        verb = self.verb_ent.get()
        adjectives = ""
        if self.is_itchy.get():
            adjectives += "нетерпеливое, "
        if self.is_joyous.get():
            adjectives += "радостное, "
        if self.is_electric.get():
            adjectives += "электрическое, "
        body_part = self.body_part.get()
        story = f"Знаменитый юрист {person} уже совсем отчаялся довершить дело всей своей жизни - поиск затерянного города, в котором, по легенде, обитали {noun.title()}. Но однаждый {noun} и {person} столкнулись лицом к лицу. Мощное, {adjectives} ни с чем не сравнимое чувство охватило душу юриста. После стольких лет поисков, цель была достигнута. {person} ощутил, как его {body_part} поднялась вверх. И тут внезапно {noun} перешли в атаку и {person} получил по сраке. Мораль? Если задумали {verb}, надо делать это с осторожностью"
        self.story.delete(0.0, END)
        self.story.insert(0.0, story)

if __name__ == '__main__':
    root = Tk()
    root.title("Creator Small Stories")
    root.resizable(False, False)
    app = Application(root)
    root.mainloop()