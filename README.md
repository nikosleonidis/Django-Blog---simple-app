# Django-Blog---simple-app
This application is designed to get acquainted with Django framework, please do not hesitate to ask questions.

Инструкция доступна на русском и английском языках.
The instruction is available in Russian and English.

------------------------------------------------   ВНИМАНИЕ   ------------------------------------------------

## Следуй ⏭ инструкции, чтобы развернуть этот проект у себя на устройстве 💻 👇 - Русский

----------------------------------------------   MacOS Linux   -----------------------------------------------
Выполните следующие команды:

Для работы с языком Python мы используем команду "python3"

1. cd "backend" - Осуществляет переход в папку "backend", в ней содержится файл "manage.py", которому мы 
   даем команды

2. python3 -m venv venv ("venv" второй раз - Это название папки, оно может быть любым) - создает виртуальное 
окружение python внутри проекта.

3. source venv/bin/activate - Осуществляет переход в виртуальную среду python.

Далее обращаемся через команду "python", так как находимся в виртуальном окружении

3. pip install -r requirements.txt - Устанавливает все используемые в проекте зависимости, чтобы нам не 
   пришлось устанавливать их вручную.

4. python manage.py makemigrations - Создает файл инициализации для миграции в базу данных

5. python manage.py migrate - Осуществляет миграцию в базу данных, необходимо для применения всех 
   изменений в проекте. По умолчанию база данных ничего не принимает. 

6. python manage.py runserver - Запускает проект, после запуска создает базу данных. По умолчанию django 
   использует "SQLite". Поздравляю! Теперь проект готов к использованию. 🥳

Спасибо за то что прочитал до конца, если возникнут вопросы не стесняйся задавать. Успехов! 😉


-----------------------------------------------   ATTENTION   -----------------------------------------------

## Follow ⏭ instructions to deploy this project on your device 💻 👇 - English

----------------------------------------------   MacOS Linux   -----------------------------------------------
Run the following commands:

To work with the Python language, we use the "python3" command

1. cd "backend" - Goes to the "backend" folder, it contains the "manage.py" file, to which we give commands

2. python3 -m venv venv ("venv" Second time - This is the name of the folder, it can be any) - creates a virtual Python environment within the project.

3. source venv/bin/activate - migrates to the python virtual environment.

Next, we contact us through the "python" command, as we are in a virtual environment

3. pip install -r requirements.txt - Installs all the dependencies used in the project so that we do not have to install them manually.

4. python manage.py makemigrations - Creates an initialization file for migration to the database

5. python manage.py migrate - Migrates to the database, necessary to apply all changes to the project. By default, the database does not accept anything. 

6. python manage.py runserver - Starts the project, creates a database after launch. By default, django 
   uses SQLite. Congratulations! Now the project is ready for use. 🥳

Thank you for reading to the end, if you have any questions, do not hesitate to ask. Good luck! 😉


------------------------------------------------   ВНИМАНИЕ   ------------------------------------------------

## Следуй ⏭ инструкции, чтобы развернуть этот проект у себя на устройстве 💻 👇 - Русский

------------------------------------------------   Windows   ------------------------------------------------
Выполните следующие команды:

Для работы с языком Python мы используем команду "python", так же как и в виртуальной среде.

1. cd "backend" - Осуществляет переход в папку "backend", в ней содержится файл "manage.py", которому мы 
   даем команды

2. python -m venv venv ("venv" второй раз - Это название папки, оно может быть любым) - создает виртуальное 
окружение python внутри проекта.

3. venv\Scripts\activate.bat - Осуществляет переход в виртуальную среду python.

Чтобы убедиться что вы в виртуальном окружении выполните следующую команду:
pip list - отображает список всех установленных пакетов, если пакетов слишком много, вероятно, вы 
обращаетесь напрямую к питону. Попробуйте выйти из среды разработки и повторить все согласно инструкции.

3. pip install -r requirements.txt - Устанавливает все используемые в проекте зависимости, чтобы нам не 
   пришлось устанавливать их вручную.

4. python manage.py makemigrations - Создает файл инициализации для миграции в базу данных

5. python manage.py migrate - Осуществляет миграцию в базу данных, необходимо для применения всех 
   изменений в проекте. По умолчанию база данных ничего не принимает. 

6. python manage.py runserver - Запускает проект, после запуска создает базу данных. По умолчанию django 
   использует "SQLite". Поздравляю! Теперь проект готов к использованию. 🥳

Спасибо за то что прочитал до конца, если возникнут вопросы не стесняйся задавать. Успехов! 😉


-----------------------------------------------   ATTENTION   -----------------------------------------------

## Follow ⏭ instructions to deploy this project on your device 💻 👇 - English

------------------------------------------------   Windows   ------------------------------------------------
Run the following commands:

To work with the Python language, we use the "python" command, as well as in a virtual environment.

1. cd "backend" - Goes to the "backend" folder, it contains the "manage.py" file, to which we give commands

2. python -m venv venv ("venv" Second time - This is the name of the folder, it can be any) - creates a virtual Python environment within the project.

3. venv\Scripts\activate.bat - migrates to the python virtual environment.

To make sure you are in a virtual environment, run the following command:
pip list - displays a list of all installed packages, if there are too many packages, you're probably
accessing the python global folder. Try to exit the development environment and repeat everything according to
the instructions.

3. pip install -r requirements.txt - Installs all the dependencies used in the project so that we do not have to install them manually.

4. python manage.py makemigrations - Creates an initialization file for migration to the database

5. python manage.py migrate - Migrates to the database, necessary to apply all changes to the project. By default, the database does not accept anything. 

6. python manage.py runserver - Starts the project, creates a database after launch. By default, django 
   uses SQLite. Congratulations! Now the project is ready for use. 🥳

Thank you for reading to the end, if you have any questions, do not hesitate to ask. Good luck! 😉



<img width="1440" alt="registration" src="https://user-images.githubusercontent.com/65124365/168424282-619b397a-6c1e-4fd7-a6bc-fb36a95d2e96.png">
<img width="1440" alt="login" src="https://user-images.githubusercontent.com/65124365/168424271-dcb79de7-cabe-4cff-88b4-c9f9fe0d0338.png">
<img width="1440" alt="home" src="https://user-images.githubusercontent.com/65124365/168424301-27306ba6-f66d-4206-a38a-da1c83df7eb1.png">
<img width="1440" alt="create-update" src="https://user-images.githubusercontent.com/65124365/168424326-c4cc1400-9524-42df-b0b2-338cbec5ccee.png">
<img width="1440" alt="detail" src="https://user-images.githubusercontent.com/65124365/168424309-b80862e1-0697-4168-8233-1b7987fc996e.png">
<img width="1440" alt="profile" src="https://user-images.githubusercontent.com/65124365/168424333-fc150ad0-6477-4e55-9078-0babe14bea81.png">
<img width="1440" alt="logout-modal" src="https://user-images.githubusercontent.com/65124365/168424337-2dbae1a7-1753-4d29-98b4-2c0326337dbf.png">
<img width="1440" alt="logout" src="https://user-images.githubusercontent.com/65124365/168424358-9d379798-61ca-4651-8e2c-55b36881ffd9.png">

