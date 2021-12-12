from PyQt5.QtCore import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout
import json
app = QApplication([])
with open('notes_data.json','w', encoding = 'utf-8') as file:
    json.dump(notes.file)
'''Интерфейс приложения'''
notes_win = QWidget()
notes_win.setWindowTittle('Умные заметки')
notes_win.resize(900,600)
list_notes = QListWidget()
list_notes_label = QLabel('Список заметок')
button_note_create = QPushButton('Создать заметку')
button_note_del = QPushButton('Удалить заметку')
button_note_save = QPushButton('Сохранить заметку')
field_tag = QLineEdit('')
field_tag.setPlaceholderText('Введите тег...')
field_tag = QTextEdit()
button_tag_add = QPushButton('Добавить к заметке')
button_tag_del = QPushButton('Открепить от заметки')
button_tag_search = QPushButton('Искать заметки по тегу')
list_tags = QListWidget()
list_tags_label = QLabel('Список тегов')
layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)
layout_notes = QHBoxLayout()
col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)
col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_2.addWidget(button_tag_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)
col_2.addLayout(row_3)
col_2.addLayout(row_4)
layout_notes.addLayout(col_1, stretch = 3)
layout_notes.addLayout(col_2, stretch = 2)
notes_win.setLayout(layout_notes)
def add_note():
    note_name,ok = QInputDialog.getText(notes_win,'Добавить заметку','Название заметки:')
    if ok and note_name != '':
        notes[notes] = {'текст': '','теги': []}
        list_notes.addItem(note_name)
        list_tags.addItems(notes[note_name]['теги'])
        print(notes)
def show_note():
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_text.setText(notes[key]['текст'])
    list_tags.clear()
    list_tags.addItems(notes[key]['теги'])
def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]['текст'] = field_text.toPlainText()
        with open('notes_data.json','w',encoding='utf-8') as file:
            json.dump(notes,file, sort_keys=True,ensure_ascii=False)
            print(notes)
    else:
        print('Заметка для сохранения не выбрана!')
def del_note():
     if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes(key)
        list_notes.clear()
        field_text.clear()
        list_notes.addItems(notes)
        with open('notes_data.json',)

''' Работа с тегами заметки'''
def add_tag():
    if list_tags.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = field_tag.text()
        if not tag in notes[key]['теги']:
            notes[key]['теги'].append(tag)
            list_tags.addItem(tag)
            field_tag.clear()
            with open('notes_data.json','w', encoding= 'utf-8') as file:
                json.dump(notes,file,sort_keys=True,ensure_ascii= False)
                print(notes)
        else:
            print('Заметка для добавления тега не выбрана!')
def del_tag():
    if list_tags.selectedItems():
        key = list_notes.selectedItems()[0].text()  
        tag = list_tags.selectedItems()[0].text()  
        notes[key]['теги'].remove(tag)
        list_tags.clear()
        list_tags.addItems(notes[key]['теги'])
        with open('notes_data.json','w', encoding= 'utf-8') as file:
                json.dump(notes,file,sort_keys=True,ensure_ascii= False)
                print(notes)
        else:
            print('Тег для удаления не выбран')
def search_teg():
    print(button_tag_search.text())
    tag = field_tag.text()
    if button_tag_search.text() == 'Искать заметки по тегу' and tag :
        print(tag)
        notes_filtered ={}
        for note in notes:
            if tag in notes[note]['теги']:
                notes_filtered[note]=notes[note]
        button_tag_search.setText('Сбросить поиск')
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes_filtered)
        print(button_tag_search.text())
    elif button_tag_search.text() == 'Сбросить поиск':
        field_tag.clear()
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes)
        button_tag_search.setText('Искать заметки по тегу')
        print(button_tag_search.text())
    else:
        pass
'''Запуск приложения'''
button_note_create.clicked.connect(add_note)
list_notes.itemClicked.connect(show_note)
button_note_save.clicked.connect(save_note)
button_note_del.clicked.connect(del_note)
notes_win.show()
with open('notes_data.json', 'r', encoding = 'utf-8') as file:
    notes = json.load(file)
list_notes.addItems(notes)
app.exec_()