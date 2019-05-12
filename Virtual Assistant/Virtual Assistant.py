import speech_recognition as sr
import os
import wikipedia
import pyttsx3
from PyQt5 import QtGui, QtWidgets, uic
import PyQt5
import webbrowser
import time
import subprocess
from googletrans import Translator
from bs4 import BeautifulSoup
import requests

from interface import Ui_MainWindow

class Virtual_Assistant(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.commands)
        self.pushButton_2.clicked.connect(self.settings)

        self._recognizer = sr.Recognizer()
        self._microphone = sr.Microphone()

    def settings(self):
        self.ui = uic.loadUi("command.ui")
        self.ui.show()

    def speech_recognition(self):
        """Recognize speech"""
        with self._microphone as source:
            self.speech_synthesizer('Слушаю')
            print('Говорите')
            audio = self._recognizer.record(source, duration = 3.3)
            try:
                text = self._recognizer.recognize_google(audio, language="ru_RU")
                text = text.lower()
                print(text.lower())
                return text
            except sr.UnknownValueError:
                self.speech_synthesizer('Вы ничего не сказали')

    def speech_synthesizer(self, text):
        """Text-to-speech synthesis"""
        engine = pyttsx3.init()
        ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
        engine.setProperty('rate', 200)
        engine.setProperty('volume', 1)
        engine.setProperty('voice', ru_voice_id)
        text = engine.say(text)
        engine.runAndWait()
        return text

    def commands(self):
        """Voice Assistant Commands"""
        phrase = self.speech_recognition()

        #======[Поисковые запросы]======#
        try:

            if phrase.find('найди') != -1:
                phrase = phrase.replace('найди', '')  # Убираем слово "найди".
                Search().google(phrase)  # Производим поисковой запрос.
                self.speech_synthesizer('Занимаюсь поиском' + phrase)

            if phrase.find('слушать песню') != -1:
                phrase = phrase.replace('слушать песню', '')
                Search().song_search(phrase)
                self.speech_synthesizer('Занимаюсь поиском песни' + phrase)

            if phrase.find('смотреть фильм') != -1:
                phrase = phrase.replace('смотреть фильм', '')
                Search().film_search(phrase)
                self.speech_synthesizer('Занимаюсь поиском фильма' + phrase)

            #======[Открытие программ/сайтов]======#

                # ======[Программы]======#

            if phrase.find('калькулятор') != -1 or phrase.find('открой калькулятор') != -1:
                os.startfile('calc')
                self.speech_synthesizer('калькулятор запущен')

            if phrase.find('блокнот') != -1 or phrase.find('открой блокнот') != -1 :
                os.startfile('notepad')
                self.speech_synthesizer('блокнот запущен')

            if phrase.find('paint') != -1:
                os.startfile('mspaint')
                self.speech_synthesizer('пеинт запущен')

            if phrase.find('браузер') != -1 or phrase.find("google chrome")!=-1:
                webbrowser.open('https://www.google.com.ua/?hl=ru')
                self.speech_synthesizer('Гугл хром запущен')

            if phrase.find('photoshop') != -1:
                Open().open_photoshop()
                self.speech_synthesizer('фотошоп запущен')

            if phrase.find('telegram') != -1:
                Open().open_telegram()
                self.speech_synthesizer('телеграм открыт')

            if phrase.find('атом') != -1:
                Open().open_atom()
                self.speech_synthesizer('атом запускается')

            if phrase.find('вибер') != -1 or phrase.find('viber') != -1:
                Open().open_viber()
                self.speech_synthesizer('Вайбер открыт')

            if phrase.find('почту') != -1 or phrase.find('почта') != -1:
                webbrowser.open('https://mail.google.com/mail/u/0/?pli=1#inbox')
                self.speech_synthesizer('Почта открыта')

            if phrase.find('пайчарм') != -1 or phrase.find('pycharm') != -1:
                os.startfile('C:\\Program Files\\JetBrains\\PyCharm 2018.2.2\\bin\\pycharm64.exe')
                self.speech_synthesizer('Пайчарм запущен')

            if phrase.find('ворд') != -1 or phrase.find('word') != -1:
                os.startfile('C:\\Program Files\\Microsoft Office\\root\Office16\\WINWORD.exe')
                self.speech_synthesizer('Ворд запущен')

            if phrase.find('саблим') != -1 or phrase.find('sublime') != -1:
                os.startfile('C:\Program Files\Sublime Text 3\sublime_text.exe')
                self.speech_synthesizer('Саблим запущен')

                # ======[Сайты]======#

            if phrase.find('youtube') != -1:
                Open().open_youtube()
                self.speech_synthesizer('Ю туб открыт')

            if phrase.find('кинопоиск') != -1:
                Open().open_kinopoisk()
                self.speech_synthesizer('кинопоиск открыт')

            if phrase.find('википедию') != -1 or phrase.find('википедия') != -1:
                Open().open_wikipedia()
                self.speech_synthesizer('википедия октрыта')

            #=========[Выключение/перезагрузка компьютера]========#

            if phrase.find('выключи компьютер') != -1:
                self.speech_synthesizer('Компьютер будет выключен')
                Shutdown_Reboot().shutdown()

            if phrase.find('перезагрузи компьютер') != -1:
                self.speech_synthesizer('Компьютер будет перезагружен')
                Shutdown_Reboot().reboot()

            # =========[Перевод слов]======== #

            if phrase.find('переведи слово') != -1 or \
               phrase.find('переведи предложение') != -1:
                phrase = phrase.replace('переведи слово', '')
                phrase = phrase.replace('переведи предложение', '')
                if phrase.find('на английский') != -1:
                    phrase = phrase.replace('на английский', '')
                if phrase.find('на русский') != -1:
                    phrase = phrase.replace('на русский', '')
                    Translate().translate_russian(phrase)

            # =========[Google Maps]======== #

            if phrase.find('поесть') != -1 or phrase.find('рестораны') != -1 or phrase.find('кафе') != -1 or\
                    phrase.find('ресторан') != -1 or phrase.find('еда') != -1 or phrase.find('ресторанов') != -1:

                webbrowser.open('https://www.google.com.ua/maps/search/Рестораны+кафе+винница')
                self.speech_synthesizer('Я открыла вам карту для просмотра мест где можно поесть')

            if phrase.find('проложи маршрут') != -1:
                phrase = phrase.replace('проложи маршрут','')
                route = phrase.rpartition('до')
                routes = []
                for value in route:
                    routes.append(value.replace('от', '').strip())
                route_a = routes[0]
                route_b = routes[2]
                Google_Maps().plot_the_route(route_a, route_b)
                self.speech_synthesizer('Я занимаюсь постройкой маршрута')

            # =========[Новости]======== #

            if phrase.find('новости') != -1:
                News().news_for_today()

            # =========[Список дел]======== #

            if phrase.find('добавь в список дел') != -1 or phrase.find('добавь в список задач') != -1 or phrase.find('добавь список задач') != -1 :
                phrase = phrase.replace('добавь в список дел','')
                phrase = phrase.replace('добавь в список задач', '')
                Tasks().add_task(phrase)

            if phrase.find('удали из списка дел') != -1 or phrase.find('удаление списка дел') != -1\
                    or phrase.find('удали из списка задач') != -1 or phrase.find('удаление списка задач') != -1:
                phrase = phrase.replace('удали из списка дел','')
                phrase = phrase.replace('удаление списка дел', '')
                phrase = phrase.replace('удали из списка задач', '')
                phrase = phrase.replace('удаление списка задач', '')
                Tasks().delete_task(phrase)

            if phrase.find('список дел') != -1 or phrase.find('список задач') != -1:
                Tasks().task_list()

            # =========[Погода]======== #

            if phrase.find('погода на сегодня') != -1 or phrase == 'прогноз погоды' or phrase.find('прогноз погоды на сегодня') != -1:
                Weather().weather('сегодня')

            if phrase.find('погода на завтра') != -1 or phrase.find('прогноз погоды на завтра') != -1:
                Weather().weather('завтра')

            if phrase.find('погода на неделю') != -1 or phrase.find('прогноз погоды на неделю') != -1:
                Weather().weather('неделя')

            # =========[Курсы валют]======== #

            if phrase.find('курс доллара') != -1 or phrase.find('доллар') != -1:
                Currency().currency_parsing('доллар')

            if phrase.find('курс евро') != -1 or phrase.find('евро') != -1:
                Currency().currency_parsing('евро')

            if phrase.find('курс рубля') != -1 or phrase.find('рубль') != -1:
                Currency().currency_parsing('рубль')

        except(TypeError, ValueError, AttributeError, SyntaxError, RuntimeError):
            self.speech_synthesizer('Вы неправильно произнесли команду')


class Weather(Virtual_Assistant):
    """Weather forecast"""

    def weather(self, choice):
        """Weather forecast"""

        BASE_URL = 'https://sinoptik.ua/погода-винница/10-дней'
        r = requests.get(BASE_URL)
        soap = BeautifulSoup(r.text, 'html.parser')
        temperature = soap.select('div.temperature')
        date = soap.select('p.date')
        weather = soap.select('div.wDescription.clearfix')
        days = soap.select('a.day-link')

        days_information = []  # Дни недели.
        for day in days:
            days_information.append(day.get_text())

        weather_information = []  # Информация о погоде.
        for i in weather:
            weather = i.get_text().strip()
            weather_information.append(weather)

        date_information = []  # Даты.
        for value in date:
            text = value.get_text()
            date_information.append(text)

        temperature_information = []  # Температура
        for msg in temperature:
            txt = msg.get_text().replace('мин.', 'минимум').replace('макс.', 'максимум')
            temperature_information.append(txt)

        if choice == 'сегодня':
            print('cегодня ' + temperature_information[0] + weather_information[0])
            self.speech_synthesizer('Сегодня ' + temperature_information[0] + weather_information[0])

        if choice == 'завтра':
            print(days_information[1] + temperature_information[1])
            self.speech_synthesizer(days_information[1] + temperature_information[1])

        if choice == 'неделя':
            print(days_information[0] + temperature_information[1] + '\n'
                                           + days_information[1] + temperature_information[2] + '\n'
                                           + days_information[2] + temperature_information[3] + '\n'
                                           + days_information[3] + temperature_information[4] + '\n'
                                           + days_information[4] + temperature_information[5] + '\n'
                                           + days_information[5] + temperature_information[6])
            self.speech_synthesizer(days_information[0] + temperature_information[1] + '\n'
                                           + days_information[1] + temperature_information[2] + '\n'
                                           + days_information[2] + temperature_information[3] + '\n'
                                           + days_information[3] + temperature_information[4] + '\n'
                                           + days_information[4] + temperature_information[5] + '\n'
                                           + days_information[5] + temperature_information[6])


class Translate(Virtual_Assistant):
    """Translator of words into different languages"""

    def translate_english(self, text):
        """Translation of words into English"""
        translator = Translator()
        translated = translator.translate(text, src='ru', dest='en')
        print(translated.text)
        return self.speech_synthesizer(translated.text)

    def translate_russian(self, text):
        """Translation of words into Russian"""
        translator = Translator()
        translated = translator.translate(text, src='en', dest='ru')
        print(translated.text)
        return self.speech_synthesizer(translated.text)


class Google_Maps(Virtual_Assistant):
    """Work with Google maps"""

    def plot_the_route(self, route_a, route_b):
        """Paving the route"""
        plot_the_route = webbrowser.open('https://www.google.com.ua/maps/dir/'
                                         + route_a + '/' + route_b)
        return plot_the_route

class Shutdown_Reboot(Virtual_Assistant):
     """Reboot and shutdown computer"""

     def reboot(self):
         reboot = os.system("shutdown -t 0 -r -f")
         return reboot

     def shutdown(self):
         off = os.system('shutdown /p /f')
         return off

class Tasks(Virtual_Assistant):
    """Tasks"""

    def add_task(self, text):
        lines = []
        task = text
        lines.append(task)
        with open(r"tasks.txt", "a") as file:
            count = 0
            for line in lines:
                count += 1
                file.seek(count)
                file.write(line + '\n')
                return self.speech_synthesizer('Задача ' + task + 'добавлена в список задач')

    def delete_task(self, text):
        f = open('tasks.txt')
        output = []
        for line in f:
            if not text in line:
                output.append(line)
        f.close()
        f = open('tasks.txt', 'w')
        f.writelines(output)
        f.close()
        return self.speech_synthesizer('Задача '+ text + 'удалена из списка задач')

    def task_list(self):
        if os.stat("tasks.txt").st_size == 0:
            return self.speech_synthesizer('Ваш список задач пуст')
        else:
            with open('tasks.txt', 'r') as file:
                string = file.read()
                print(string)
                return self.speech_synthesizer(string)

class News(Virtual_Assistant, QtWidgets.QMainWindow):
    """News for today"""

    def news_for_today(self):
        BASE_URL = 'https://gordonua.com/news.html'
        r = requests.get(BASE_URL)
        soap = BeautifulSoup(r.text, 'html.parser')
        news = soap.select('div.lenta_head')
        articles = []
        for article in news:
            text = article.get_text().strip()
            articles.append(text)
        self.speech_synthesizer('Сейчас я зачитаю вам все новости на сегодня')
        for article in articles:
            self.speech_synthesizer(article)

class Currency(Virtual_Assistant):
    """Exchange Rates"""

    def currency_parsing(self, currency):
        BASE_URL = 'https://finance.i.ua/'
        r = requests.get(BASE_URL)
        soap = BeautifulSoup(r.text, 'html.parser')
        rate = soap.select('td')
        rates = []
        for value in rate:
            text = value.get_text()
            rates.append(text)

        if currency == 'доллар':
            print('Курс доллара: ' + rates[6][0:2] + ' гривен ' + rates[6][3:5] + ' копеек')
            self.speech_synthesizer('Курс доллара: ' + rates[6][0:2] + ' гривен ' + rates[6][3:5] + ' копеек')

        if currency == 'евро':
            print('Курс евро: ' + rates[9][0:2] + ' гривен ' + rates[9][3:5] + ' копеек')
            self.speech_synthesizer('Курс евро: ' + rates[9][0:2] + ' гривен ' + rates[9][3:5] + ' копеек')

        if currency == 'рубль':
            print('Курс рубля: ' + rates[12][0] + ' гривен ' + rates[12][2:4] + ' копеек')
            self.speech_synthesizer('Курс рубля: ' + rates[12][0] + ' гривен ' + rates[12][2:4] + ' копеек')


class Search(Virtual_Assistant):
    """Search for something"""

    def google(self, request):
        search = webbrowser.open('https://www.google.com/search?q=' + request)
        return search

    def song_search(self, song):
        search = webbrowser.open('https://music.youtube.com/search?q=' + song)
        return search

    def film_search(self, film):
        search = webbrowser.open('http://hdrezka.ag/index.php?do='
                                 'search&subaction=search&q=' + film)
        return search

class Open(Virtual_Assistant):
    """Opening programs or sites"""

    #======[Открытие программ]======#

    def open_photoshop(self):

        open = os.startfile("C:\Program Files (x86)"
                            "\Photoshop CS6\Photoshop.exe")
        return open

    def open_telegram(self):
        open = os.startfile("C:\\Users\\Python Developer\\AppData\\"
                            "Roaming\\Telegram Desktop\\Telegram.exe")
        return open

    def open_atom(self):
        open = os.startfile("C:\\Users\\Python Developer\\"
                            "AppData\Local\\atom\\atom.exe")
        return open

    def open_viber(self):
        open = os.startfile("C:\\Users\\Python Developer\\AppData\\Local\\Viber\\Viber.exe")
        return open

    #======[Открытие сайтов]======#

    def open_youtube(self):
        open = webbrowser.open('http://www.youtube.com')
        return open

    def open_kinopoisk(self):
        open = webbrowser.open('https://www.kinopoisk.ru/')
        return open

    def open_wikipedia(self):
        open = webbrowser.open('https://ru.wikipedia.org')
        return open

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Virtual_Assistant()
    window.show()
    sys.exit(app.exec())

