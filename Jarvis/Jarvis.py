import pyttsx3
import speech_recognition as sr
import datetime
import os
import json
from requests import get
import wmi
import psutil
import platform
import wikipedia
import webbrowser
import pywhatkit
import sys
import smtplib
import pyautogui
import time
from time import sleep
import pyjokes
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import PyPDF2
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime,  QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUi import Ui_jarvisUi


engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voices', voice[1].id)

#Jarvis speaking code
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#Jarvis trying to understand the command code


# Fetching news code
def news():
    news_url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=3d7d2570874a4de697f837fc650bb57b"
    news_page = requests.get(news_url).json()
    articles = news_page["articles"]
    headlines = []
    days = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for a in articles:
        headlines.append(a["title"])
    for i in range(len(days)):
        speak(f"Today's {days[i]}  news is: {headlines[i]}")

#Jarvis greeting code
def greeting():
    hour = int(datetime.datetime.now().hour)
    timee = time.strftime("%I:%M %p")
    if (hour >0 and hour <=12):
        speak(f"Good morning sir its {timee}")
    elif (hour >12 and hour <18):
        speak(f"Good afternoon sir its {timee}")
    else:
        speak(f"Good evening sir its {timee}")
    speak("Your assistant Jarvis at your service sir...How can I help you")

# Pdf reading code
def pdf_reader():
    speak("Sir can u please enter the correct file location of the pdf u need me to read out please")
    pdflocation = input()
    book = open(pdflocation, 'rb')
    pdfreader = PyPDF2.PdfFileReader(book)
    pagecount = pdfreader.numPages
    speak(f"Sir there are totally {pagecount} pages in the book u told me to read sir")
    speak("Sir please enter the page number of the book u need me to read ")
    pagenumber = int(input("Enter the page number sir: "))
    page = pdfreader.getPage(pagenumber)
    contents = page.extractText()
    speak(contents)



class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()
    def run(self):
        self.permission = self.receivecommand().lower()
        if "wakeup" or "wake up" in self.permission:
            greeting()
        self.tasks()

    def receivecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening.....")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=2, phrase_time_limit=6)

        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language="en-in")
            print(f"Boss said:{query}")

        except Exception as e:
            speak("Can you come again sir please")
            return "none"
        return query

    def tasks(self):
        while True:
            self.query = self.receivecommand().lower()
            if "open notepad" in self.query:
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)

            elif "close notepad" in self.query:
                speak("Ok sir, Closing notepad")
                os.system("taskkill /f /im notepad.exe")

            elif "open d drive" in self.query:
                dpath = "D:"
                os.startfile(dpath)

            elif "open chrome" in self.query:
                cpath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(cpath)

            elif "close chrome" in self.query:
                speak("Ok sir, Closing chrome")
                os.system("taskkill /f /im chrome.exe")

            elif "open command prompt" in self.query:
                os.system("start cmd")

            elif "close command prompt" in self.query:
                speak("Ok sir, Closing cmd")
                os.system("taskkill /f /im cmd.exe")

            elif "play movie" in self.query:
                movie_dir = "D:\\movies"
                movies = os.listdir(movie_dir)
                os.startfile(os.path.join(movie_dir, movies[1]))

            elif "academics" in self.query:
                academicspath = "D:\\Academics"
                os.startfile(academicspath)

            elif "ai projects" in self.query:
                aiprojectspath = "D:\\AI Proj"
                os.startfile(aiprojectspath)

            elif "bi folder" in self.query:
                bipath = "D:\\bi"
                os.startfile(bipath)

            elif "certificates" in self.query:
                certificatespath = "D:\\CERTIFICATES"
                os.startfile(certificatespath)

            elif "courses" in self.query:
                coursespath = "D:\\Courses"
                os.startfile(coursespath)

            elif "prithvi" in self.query:
                prithvipath = "D:\\Prithvi"
                os.startfile(prithvipath)
            elif "your source folder" in self.query:
                jarvispath = "D:\\myjarvis"
                os.startfile(jarvispath)

            elif "my research" in self.query:
                researchpath = "D:\\Research"
                os.startfile(researchpath)

            elif "setups" in self.query:
                setupspath = "D:\\Setups"
                os.startfile(setupspath)

            elif "my image" in self.query:
                myimagepath = "D:\\sam.png"
                os.startfile(myimagepath)

            elif "music" in self.query:
                music_dir = "D:\\music"
                songs = os.listdir(music_dir)
                for song in songs:
                    if song.endswith(".mp3"):
                        os.startfile(os.path.join(music_dir, song))

            elif "wikipedia" in self.query:
                speak("Searching Wikipedia please give me a moment sir...")
                query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                speak(results)

            elif "ip address" in self.query:
                ip = get("https://api.ipify.org").text
                speak(f"Sir your ip address is: {ip}")

            elif "running process" in self.query:
                f = wmi.WMI()
                speak("Sir your running processes are:")
                for process in f.Win32_Process():
                    # Displaying the P_ID and P_Name of the process
                    speak(f"{process.Name:}")

            elif "task manager" in self.query:
                taskmanagerpath = "C:\\Windows\\system32\\Taskmgr.exe"
                os.startfile(taskmanagerpath)

            elif "ram usage" in self.query:
                psutil.cpu_percent()
                psutil.virtual_memory()
                dict(psutil.virtual_memory()._asdict())
                speak(f"Sir you have used {psutil.virtual_memory().percent} percentage of RAM and ")

            elif "memory available" in self.query:
                psutil.cpu_percent()
                psutil.virtual_memory()
                dict(psutil.virtual_memory()._asdict())
                speak(
                    f"Sir your available memory is: {int(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)} percentage")

            elif "cpu usage" in self.query:
                speak(f"Sir you have used: {psutil.cpu_percent()} percentage of your cpu")


            elif "system information" in self.query:
                uname = platform.uname()
                speak(f"System: {uname.system}")
                speak(f"Node Name: {uname.node}")
                speak(f"Release: {uname.release}")
                speak(f"Version: {uname.version}")
                speak(f"Machine: {uname.machine}")
                speak(f"Processor: {uname.processor}")

            elif "cpu information" in self.query:
                speak(f"Physical cores:{psutil.cpu_count(logical=False)}")
                speak(f"Total cores:{psutil.cpu_count(logical=True)}")
                cpufreq = psutil.cpu_freq()
                speak(f"Max Frequency: {cpufreq.max:.2f}Mhz")
                speak(f"Min Frequency: {cpufreq.min:.2f}Mhz")
                speak(f"Current Frequency: {cpufreq.current:.2f}Mhz")
                speak("CPU Usage Per Core:")
                for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
                    speak(f"Core {i}: {percentage}%")
                speak(f"Total CPU Usage: {psutil.cpu_percent()}%")

            elif "battery information" in self.query:
                speak(f"Sir you have used {psutil.sensors_battery()} percentage of battery")

            elif "disk info" in self.query:
                def get_size(bytes, suffix="B"):
                    factor = 1024
                    for unit in ["", "K", "M", "G", "T", "P"]:
                        if bytes < factor:
                            return f"{bytes:.2f}{unit}{suffix}"
                        bytes /= factor
                    return bytes

                speak("Sir your Disk Information:")
                speak("Partitions and Usage:")
                # get all disk partitions
                partitions = psutil.disk_partitions()
                for partition in partitions:
                    speak(f" Device: {partition.device}")
                    speak(f"  Mountpoint: {partition.mountpoint}")
                    speak(f"  File system type: {partition.fstype}")
                    try:
                        partition_usage = psutil.disk_usage(partition.mountpoint)
                    except PermissionError:
                        # this can be catched due to the disk that
                        # isn't ready
                        continue
                    speak(f"  Total Size: {get_size(partition_usage.total)}")
                    speak(f"  Used: {get_size(partition_usage.used)}")
                    speak(f"  Free: {get_size(partition_usage.free)}")
                    speak(f"  Percentage: {partition_usage.percent}%")
                # get IO statistics since boot
                disk_io = psutil.disk_io_counters()
                speak(f"Total read: {get_size(disk_io.read_bytes)}")
                speak(f"Total write: {get_size(disk_io.write_bytes)}")

            elif "memory information" in self.query:
                def get_size(bytes, suffix="B"):
                    factor = 1024
                    for unit in ["", "K", "M", "G", "T", "P"]:
                        if bytes < factor:
                            return f"{bytes:.2f}{unit}{suffix}"
                        bytes /= factor
                    return bytes

                speak("Sir your memory information:")
                # get the memory details
                svmem = psutil.virtual_memory()
                speak(f"Total: {get_size(svmem.total)}")
                speak(f"Available: {get_size(svmem.available)}")
                speak(f"Used: {get_size(svmem.used)}")
                speak(f"Percentage: {svmem.percent}%")
                speak("Swap Memory")
                # get the swap memory details (if exists)
                swap = psutil.swap_memory()
                speak(f"Total: {get_size(swap.total)}")
                speak(f"Free: {get_size(swap.free)}")
                speak(f"Used: {get_size(swap.used)}")
                speak(f"Percentage: {swap.percent}%")

            elif "open youtube" in self.query:
                webbrowser.open("https://www.youtube.com/")

            elif "open hotstar" in self.query:
                webbrowser.open("https://www.hotstar.com/in")

            elif "open whatsapp" in self.query:
                webbrowser.open("https://web.whatsapp.com/")

            elif "open linkedin" in self.query:
                webbrowser.open("https://www.linkedin.com/feed/")

            elif "open my github profile" in self.query:
                webbrowser.open("https://github.com/Vasanthengineer4949")

            elif "open ineuron dashboard" in self.query:
                webbrowser.open("https://canvas.instructure.com/")

            elif "open colab" in self.query:
                webbrowser.open("https://colab.research.google.com/notebooks/intro.ipynb#recent=true")

            elif "open my gmail inbox" in self.query:
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

            elif "open hackerank" in self.query:
                webbrowser.open("https://www.hackerrank.com/dashboard")

            elif "open spotify" in self.query:
                webbrowser.open("https://open.spotify.com/playlist/5fJ6lH9LAhKKL73CACax60")

            elif "open stack overflow" in self.query:
                webbrowser.open("https://stackoverflow.com/")

            elif "open google" in self.query:
                speak("Sir, what do you want me to search on google?")
                command = self.receivecommand().lower()
                webbrowser.open(f"{command}")

            elif "send whatsapp message" in self.query:
                pywhatkit.sendwhatmsg("+919025594724", "This is a testing message from Vasanth", 19, 15)

            elif "play song in youtube" in self.query:
                speak("Sir, what song do you want me to play on youtube")
                songcommand = self.receivecommand().lower()
                pywhatkit.playonyt(f"{songcommand}")

            elif "play video in youtube" in self.query:
                speak("Sir, what video do you want me to play on youtube")
                videocommand = self.receivecommand().lower()
                pywhatkit.playonyt(f"{videocommand}")

            elif "set alarm" in self.query:
                hourt = int(datetime.datetime.now().hour)
                if hourt == 8:
                    music_dir = "D:\\music"
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))

            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif "shut down the system" in self.query:
                os.system("shutdown /s /t 5")

            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")

            elif "switch the window" in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                sleep(1)
                pyautogui.keyUp("alt")

            elif "tell me news" in self.query:
                speak("Just give me a moment fetching some top headlines for you......")
                news()

            elif "send email" in self.query:
                speak("Whom should I mail to sir, Enter the email id")
                to = str(input())
                speak("Do you need to send any file sir?")
                query = self.receivecommand().lower()
                if "yes" in query:
                    email = "email"
                    password = "password redacted"
                    send_to_email = to
                    speak("Okay sir, Can you please say the subject of the mail sir")
                    query = self.receivecommand().lower()
                    subject = query
                    speak("And sir what about the message of the mail sir")
                    contentii = self.receivecommand().lower()
                    message = contentii
                    speak("Sir can you now please mention the correct path of the file to be attached please")
                    file_location = input("Enter the file location here sir: ")
                    speak("Sir excuse me for a moment sir sending the email now sir")

                    msg = MIMEMultipart()
                    msg["From"] = email
                    msg["To"] = send_to_email
                    msg["Subject"] = subject

                    msg.attach(MIMEText(message, "plain"))

                    filename = os.path.basename(file_location)
                    attachment = open(file_location, "rb")
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header("Content-Disposition", "attachment; filename= %s" % filename)

                    msg.attach(part)

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email, password)
                    content = msg.as_string()
                    server.sendmail(email, send_to_email, content)
                    server.quit()
                    speak("Email sent successfully sir")

                else:
                    email = "email"
                    password = "redacted"
                    send_to_email = to
                    speak("And sir what about the message of the mail sir")
                    contentii = self.receivecommand().lower()
                    message = contentii
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email, password)
                    content = msg.as_string()
                    server.sendmail(email, send_to_email, message)
                    server.quit()
                    speak("Email sent successfully sir")

            elif "screenshot" in self.query:
                speak("Sir, please can you give me a name for this screenshot sir")
                name = input("Enter here sir: ")
                speak("Sir please holdout the screen for a minute for a minute to take a screenshot sir")
                time.sleep(2)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("Successfully taken the screenshot sir")

            elif "where" in self.query:
                speak("Wait a moment sir, let me check")
                send_url = "http://api.ipstack.com/check?access_key=09dcd7a4a1569efaef378a9d076224df"
                geo_req = requests.get(send_url)
                geo_json = json.loads(geo_req.text)
                latitude = geo_json['latitude']
                longitude = geo_json['longitude']
                city = geo_json['city']
                region = geo_json['region_name']
                country = geo_json['country_name']
                speak(f"I guess if I am not wrong we are near {city} area in {region} of {country} sir")

            elif "impress" in self.query:
                speak("Set the path of the person's image u want to impress")
                impresspath = input("Enter path:")
                pywhatkit.image_to_ascii_art(impresspath, "impress.jpg")

            elif "pdf" in self.query:
                pdf_reader()

            elif "no" in self.query:
                speak("Thank you for using me, Have a good day sir, whenever again you need help your assistant will be at service. Bye sir")
                sys.exit()

            speak("Do you need me to do any other help sir")







startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarvisUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("D:\jarvis\jarvis1.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("D:\jarvis\jarvis2.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("D:\jarvis\jarvis3.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        # timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QTime.currentDate()
        label_time = current_time.toString("hh:mm:ss")
        label_date = current_date.toString(Qt.ISODate)
        self.ui.label_5.setText(label_date)
        self.ui.label_7.setText(label_time)

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())

