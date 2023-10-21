from PyQt5.QtWidgets import QApplication
from random import choice, shuffle
from time import sleep

app = QApplication([])
from main2 import*
from main3 import*

def menu_generation():
    menu_win.show()
    win.hide()
button_menu.clicked.connect(menu_generation)

class Question:
    def __init__(self, question, answer, wrong_ans1, wrong_ans2, wrong_ans3 ):
        self.question = question
        self.answer = answer
        self.wrong_ans1 = wrong_ans1
        self.wrong_ans2 = wrong_ans2
        self.wrong_ans3 = wrong_ans3
        self.isAsking = True
        self.count_ask = 0
        self.count_right = 0
    def got_right(self):
        self.count_ask += 1
        self.count_right += 1
    def got_wrong(self):
        self.count_ask += 1

q1 = Question('Хто кинув молоток і перо на Місяць, щоб продемонструвати, що без повітря вони падають з однаковою швидкістю?','Девід Р. Скотт','Тім Бернерс-Лі','Джордж Сорос','Еміль Берлінер')
q2 = Question('Якби Земля перетворилася в чорну діру, який би був діаметр її горизонту подій?','20mm','10mm','30mm','40mm')
q3 = Question('Якби ви впали в безповітряну, без тертя діру, проїжджаючи всю землю, скільки часу знадобиться, щоб впасти на інший бік? (До найближчої хвилини.)','42 хвилин','10 хвилин','35 хвилин','112 хвилин')
q4 = Question('Скільки сердець має восьминіг?','Три','Одне','Два','Чотири')
q5 = Question('Хто винайшов грамофон?','Еміль Берлінер','Девід Р. Скотт','Тім Бернерс-Лі','Джордж Сорос')
q6 = Question('Скільки років пройде космічний корабель, запущений із Землі, щоб прибути на планету Плутон?',"Дев'ять з половиною років",'Одинадцять років','Шість з половиною років','Чотири роки')
q7 = Question('Яка найбільша молекула входить до складу людського тіла?','Хромосома 1','Бактерія','Клітина','Вірус')
q8 = Question('Яка середня температура поверхні на Венері?','460 ° C','90 ° C','250 ° C','300 ° C')
q9 = Question('Наука, яка досліджує всесвіт','Астрономія','Географія','Фізика','Математика')
q10 = Question('Скільки магнітних полюсів на планеті','2','3','4','1')

radio_buttons = [rb_ans1,rb_ans2,rb_ans3,rb_ans4]
questions = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]

def new_question():
    global cur_q
    cur_q = choice(questions)
    lb_question.setText(cur_q.question)
    lb_right_answer.setText(cur_q.answer)
    shuffle(radio_buttons)
    radio_buttons[0].setText(cur_q.wrong_ans1)
    radio_buttons[1].setText(cur_q.wrong_ans2)
    radio_buttons[2].setText(cur_q.wrong_ans3)
    radio_buttons[3].setText(cur_q.answer)
new_question()

def check():
    RadioGroup.setExclusive(False)
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == lb_right_answer.text():
                lb_result.setText('Правильно!')
                answer.setChecked(False)
                break
    else:
        lb_result.setText('Неправильно!')
    RadioGroup.setExclusive(True)
def click_ok():
    if button_answer.text() == 'Відповісти':
        check()
        Gb_question.hide()
        Gb_answer.show()
        button_answer.setText('Наступне запитання')
    else:
        new_question()
        Gb_question.show()
        Gb_answer.hide()
        button_answer.setText('Відповісти')
button_answer.clicked.connect(click_ok)
def rest():
    win.hide()
    n = Sp_rest.value()*60
    sleep(n)
    win.show()
button_rest.clicked.connect(rest)
def back_menu():
    menu_win.hide()
    win.show()
btn_back.clicked.connect(back_menu)
def clear():
    le_quest.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()
btn_clear.clicked.connect(clear)
def add_question():
    new_q = Question(le_quest.text(), lb_right_answer.text(),le_wrong_ans1.text(),le_wrong_ans2.text(),le_wrong_ans3.text())
    questions.append(new_q)
    clear()
btn_addQuestion.clicked.connect(add_question)

win.show()
app.exec_()
