from PyQt5.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QLabel

menu_win = QWidget()
menu_win.setStyleSheet('background: khaki')

lb_quest = QLabel('Введіть запитання')
lb_quest.setStyleSheet('color: darkgoldenrod; font-family: ARIAL BLACK')
lb_right_ans = QLabel('Введіть правильну відповідь')
lb_right_ans.setStyleSheet('color: darkgoldenrod; font-family: ARIAL BLACK')
lb_wrong_ans1 = QLabel('Введіть першу хибну відповідь')
lb_wrong_ans1.setStyleSheet('color: darkgoldenrod; font-family: ARIAL BLACK')
lb_wrong_ans2 = QLabel('Введіть другу хибну відповідь')
lb_wrong_ans2.setStyleSheet('color: darkgoldenrod; font-family: ARIAL BLACK')
lb_wrong_ans3 = QLabel('Введіть третю хибну відповідь')
lb_wrong_ans3.setStyleSheet('color: darkgoldenrod; font-family: ARIAL BLACK')

le_quest = QLineEdit()
le_right_ans = QLineEdit()
le_wrong_ans1 = QLineEdit()
le_wrong_ans2 = QLineEdit()
le_wrong_ans3 = QLineEdit()

lb_header_stat = QLabel('Статистика')
lb_header_stat.setStyleSheet('color: darkgoldenrod; font-family: ARIAL BLACK')
lb_statistic = QLabel()

v1_label = QVBoxLayout()
v1_label.addWidget(lb_quest)
v1_label.addWidget(lb_right_ans)
v1_label.addWidget(lb_wrong_ans1)
v1_label.addWidget(lb_wrong_ans2)
v1_label.addWidget(lb_wrong_ans3)

v1_lineEdits = QVBoxLayout()
v1_lineEdits.addWidget(le_quest)
v1_lineEdits.addWidget(le_right_ans)
v1_lineEdits.addWidget(le_wrong_ans1)
v1_lineEdits.addWidget(le_wrong_ans2)
v1_lineEdits.addWidget(le_wrong_ans3)

h1_question = QHBoxLayout()
h1_question.addLayout(v1_label)
h1_question.addLayout(v1_lineEdits)

btn_back = QPushButton('Назад')
btn_back.setStyleSheet('color: darkgoldenrod; font-family: ARIAL BLACK')
btn_addQuestion = QPushButton('Додати запитання')
btn_addQuestion.setStyleSheet('color: darkgoldenrod; font-family: ARIAL BLACK')
btn_clear = QPushButton('Очистити')
btn_clear.setStyleSheet('color: darkgoldenrod; font-family: ARIAL BLACK')

h1_button = QHBoxLayout()
h1_button.addWidget(btn_addQuestion)
h1_button.addWidget(btn_clear)

v1_res = QVBoxLayout()
v1_res.addLayout(h1_question)
v1_res.addLayout(h1_button)
v1_res.addWidget(lb_header_stat)
v1_res.addWidget(btn_back)

menu_win.setLayout(v1_res)
menu_win.resize(400,300)



