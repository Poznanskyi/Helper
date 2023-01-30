PERSONAL ASSISTANT 'HELPER''

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Інструкція по роботі з асистентом

______________________________________________________________________________________________________

'HELPER'- проект створений саме для Вас, з інтерфейсом командного рядка

'Helper' вміє:

1. Зберігати контакти з іменами, адресами, номерами телефонів, email та днями народження до книги контактів;
2. Виводити список контактів, у яких день народження через задану кількість днів від поточної дати;
3. Перевіряти правильність введеного номера телефону та email під час створення або редагування запису та повідомляти користувача у разі некоректного введення;
4. Здійснювати пошук контактів серед контактів книги;
5. Редагувати та видаляти записи з книги контактів;
6. Зберігати нотатки з текстовою інформацією;
7. Проводити пошук за нотатками;
8. Редагувати та видаляти нотатки;
9. Додавати в нотатки "теги", ключові слова, що описують тему та предмет запису;
10. Здійснювати пошук та сортування нотаток за ключовими словами (тегами);
11. Сортувати файли у зазначеній папці за категоріями (зображення, документи, відео та ін.).



from setuptools import setup, find_namespace_packages

setup(
    name='Helper',
    version='0.1',
    description='Personal Assistant "Helper" with a command line interface',
    url='https://github.com/MartynyukAndriy/Helper',
    author='Martynyuk Andriy, Dmytro Poznanskyi, Mykola Tyshko, Dmytro Lyfenko, Roman Ovcharenko',
    author_email='andriy.martynyuk.if@gmail.com',
    license='MIT',
    include_package_data=True,
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['helper = helper.main:main']}
)

______________________________________________________________________________________________________

Встановлення
Для встановлення даного персонального помічника вам потрібні python 3.6+ та pip.

Скопіюйте репозиторій на ваш комп'ютер
Перейдіть до директорії Helper
Запустіть командний рядок (cmd)
Пропишіть команду: pip install -e .
Для запуску, вам потрібно прописати команду  helper в cmd, від імені адміністратора

______________________________________________________________________________________________________

Основні команди з якими працює PERSONAL ASSISTANT 'HELPER'

Робота з книгою контактів:
==========================
add:     Додає контакт до адресної книги. Поля для введення телефону, адреси, електронної пошти, дня народження
search:  Searches for contacts in the address book by the following fields: name / phone.
change:  Пошук контактів в адресній книзі за такими полями: ім'я / телефон.
show:    Показуває контакти стільки, скільки вкаже користувач.
showall: Показує всі нотатки.
del:     Видалення контакту або видалення телефону / адреси / електронної пошти / дня народження в контакті.
cancel:  Команда скасування будь-де в помічнику.
birthdays: Показує кількість днів до чийо-гось дня народження.
good bye, close, exit: Для виходу з программи.

Робота з нотатками:
===================
add:      Додає нотатку до блокнота.
search:   Шукає нотатки в блокноті за такими полями: назва / тег / статус.
change:   Змінює інформацію в примітці: ім'я / примітка / тег / статус.
show:     Показує нотатки стільки, скільки вкаже користувач
showall:  Показує всі нотатки
del:      Видалення нотатки або видалення завершених нотаток.
cancel:   Команда скасування будь-де в помічнику.
good bye, close, exit: Для виходу з программи.