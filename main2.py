from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel, QSpinBox, QApplication
from PyQt5.QtCore import Qt

win = QWidget()
win.setWindowTitle('Memory Card')
win.resize(600,500)
win.setStyleSheet('background: khaki')

button_menu = QPushButton('Меню')
button_menu.setStyleSheet('color: darkgoldenrod; font-family: ARIAL BLACK')
button_rest = QPushButton('Відпочити')
button_rest.setStyleSheet('color: darkgoldenrod; font-family: ARIAL BLACK')
button_answer = QPushButton('Відповісти')
button_answer.setStyleSheet('color: darkgoldenrod; font-family: ARIAL BLACK')

rb_ans1 = QRadioButton('1')
rb_ans2 = QRadioButton('2')
rb_ans3 = QRadioButton('3')
rb_ans4 = QRadioButton('4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rb_ans1)
RadioGroup.addButton(rb_ans2)
RadioGroup.addButton(rb_ans3)
RadioGroup.addButton(rb_ans4)

lb_question = QLabel('Запитання')
lb_question.setStyleSheet('color: darkgoldenrod; font-size:20px; font-family: ARIAL BLACK')
lb_rest = QLabel('Відпочинок')
lb_rest.setStyleSheet('color: darkgoldenrod; font-family: ARIAL BLACK')
lb_result = QLabel('Результат')
lb_right_answer = QLabel('Відповідь')

Sp_rest = QSpinBox()
Gb_question = QGroupBox('Варіанти відповіді')
Gb_question.setStyleSheet('color: darkgoldenrod; font-family: ARIAL BLACK')
Gb_answer = QGroupBox()

rb_v1 = QVBoxLayout()
rb_v2 = QVBoxLayout()
rb_h1 = QHBoxLayout()

rb_v1.addWidget(rb_ans1)
rb_v1.addWidget(rb_ans2)
rb_v2.addWidget(rb_ans3)
rb_v2.addWidget(rb_ans4)
rb_h1.addLayout(rb_v1)
rb_h1.addLayout(rb_v2)
Gb_question.setLayout(rb_h1)

v1 = QVBoxLayout()
v1.addWidget(lb_result)
v1.addWidget(lb_right_answer)
Gb_answer.setLayout(v1)

h1_main = QHBoxLayout()
h2_main = QHBoxLayout()
h3_main = QHBoxLayout()
h4_main = QHBoxLayout()
v1_main = QVBoxLayout()

h1_main.addWidget(button_menu)
h1_main.addStretch(1)
h1_main.addWidget(button_rest)
h1_main.addWidget(Sp_rest)
h1_main.addWidget(lb_rest)
h2_main.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
h3_main.addWidget(Gb_answer)
h3_main.addWidget(Gb_question)
Gb_answer.hide()

h4_main.addStretch(1)
h4_main.addWidget(button_answer, stretch=2)
h4_main.addStretch(1)

v1_main.addLayout(h1_main, stretch=1)
v1_main.addLayout(h2_main, stretch=2)
v1_main.addLayout(h3_main, stretch=8)
v1_main.addLayout(h4_main)
v1_main.setSpacing(5)

win.setLayout(v1_main)
win.resize(550,450)

