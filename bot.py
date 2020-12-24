#!/usr/bin/python
# -*- coding: utf-8 -*-
import telebot, requests, random, datetime, sys, time, argparse, json, re, sqlite3, smtplib
from datetime import datetime as dt
from telebot import types
from random import randint

bot = telebot.TeleBot("")
owner = 355821673
link = "https://example.com/folder/"

global four
global five
def deletekeyboard(message):
	keyboard = telebot.types.ReplyKeyboardRemove()
	bot.send_message(message.chat.id, "Keyboard deleted", reply_markup=keyboard)

def cancel(message):
	bot.send_message(message.chat.id, "Отменено")
	homebuttons(message)

def hello(message):
	post = requests.post(link+"uploaduser.php", data={"tgid":message.chat.id})
	if str(message.chat.id)[0] == "-":
		bot.send_message(message.chat.id, "Привет, {}.\nЯ говнобот-игра от @FSystem88.\nПеред приготовлением просьба проконсультироваться у врача в инструкции.".format(post.json()["name"]))
	else:
		bot.send_message(message.chat.id, "Привет, {}.\nЯ говнобот-игра от @FSystem88.\nВаш баланс: {}\nПеред приготовлением просьба проконсультироваться у врача в инструкции.".format(post.json()["name"], post.json()["balance"]))
	
def homebuttons(message):
	keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.row('Играть', 'Узнать баланс')
	keyboard.row('Изменить имя', 'Рейтинг')
	keyboard.row('Инструкция', 'Донатерная')
	if str(message.chat.id)[0] == '-':
		keyboard.row('Скрыть кнопки')
	keyboard.row('Турнир')
	bot.send_message(message.chat.id, '''Игровое меню:''', reply_markup=keyboard)

def olduser(message):
	keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.row('Возобновить', 'Сбросить')
	post=requests.post(link+"uploaduser.php", data={'tgid':message.chat.id})

	bot.send_message(message.chat.id, ''' Сохранённые данные:\nName: {}\nBalance: {}'''.format(post.json()["name"], post.json()["balance"]), reply_markup=keyboard)

def newuser(message):
	name = message.chat.first_name
	if str(message.chat.id)[0] == "-":
		name = message.chat.title
		chatid = str(message.chat.id)[1:]
		requests.post(link+"tablechat.php", data={'chatid':chatid})
	requests.post(link+"auth.php", data={"tgid":message.chat.id,"name":name,"username":message.chat.username})
	bot.send_message(owner, "Новый пользователь: <a href='tg://user?id={}'>{}</a>\nUsername: @{}\niD: <code>{}</code>\n".format(message.chat.id, name, message.chat.username, message.chat.id), parse_mode="HTML")
	hello(message)
	homebuttons(message)

def level(message):
	keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.row('Легкий')
	keyboard.row('Средний')
	keyboard.row('Сложный')
	keyboard.row('Рулетка')
	keyboard.row('Отмена')
	bot.send_message(message.chat.id, '''Выберите уровень сложности:''', reply_markup=keyboard)

def task_light(message):
	global four 
	text = message.text
	if text == "Отмена":
		if str(message.chat.id)[0] == "-":
			chatid = str(message.chat.id)[1:]
			bot.send_message(message.chat.id, "Игрок <b><a href='tg://user?id={}'>{}</a></b> отменил задание.\n<b>-5</b>".format(message.from_user.id, message.from_user.first_name), parse_mode="html")
			requests.post(link+"minusC.php", data={"tgid":message.from_user.id, "chatid":chatid, "balance":"5"})
		cancel(message)
	else:
		if text == str(four):
			if str(message.chat.id)[0] == "-":
				chatid = str(message.chat.id)[1:]
				bot.send_message(message.chat.id, "Игрок <b><a href='tg://user?id={}'>{}</a></b> ответил правильно.\n<b>+5</b>".format(message.from_user.id, message.from_user.first_name), parse_mode="html")
				requests.post(link+"plusC.php", data={"chatid":chatid, "tgid":message.from_user.id, "name":message.from_user.first_name, "username":message.from_user.username, "balance":"5"})
			else:
				bot.send_message(message.chat.id, "Поздравляю, Вы ответили правильно.\n<b>+ 5 баллов</b>", parse_mode="html")
				requests.post(link+"plus.php", data={"tgid":message.chat.id, "balance":"10"})
			homebuttons(message)
		else:
			if str(message.chat.id)[0] == "-":
				chatid = str(message.chat.id)[1:]
				bot.send_message(message.chat.id, "Игрок <b><a href='tg://user?id={}'>{}</a></b> ответил не правильно.\n<b>-5</b>".format(message.from_user.id, message.from_user.first_name), parse_mode="html")
				requests.post(link+"minusC.php", data={"tgid":message.from_user.id, "chatid":chatid, "balance":"5"})
			else:
				bot.send_message(message.chat.id, "Увы, но Вы ответили неправильно.")
			homebuttons(message)

def task_midle(message):
	global five 
	text = message.text
	if text == "Отмена":
		if str(message.chat.id)[0] == "-":
			chatid = str(message.chat.id)[1:]
			bot.send_message(message.chat.id, "Игрок <b><a href='tg://user?id={}'>{}</a></b> отменил задание.\n<b>-15</b>".format(message.from_user.id, message.from_user.first_name), parse_mode="html")
			requests.post(link+"minusC.php", data={"tgid":message.from_user.id, "chatid":chatid, "balance":"15"})
		cancel(message)
	else:
		if text == str(five):
			if str(message.chat.id)[0] == "-":
				chatid = str(message.chat.id)[1:]
				bot.send_message(message.chat.id, "Игрок <b><a href='tg://user?id={}'>{}</a></b> ответил правильно.\n<b>+15</b>".format(message.from_user.id, message.from_user.first_name), parse_mode="html")
				requests.post(link+"plusC.php", data={"tgid":message.from_user.id, "chatid":chatid, "balance":"15"})
			else:
				bot.send_message(message.chat.id, "Поздравляю, Вы ответили правильно.\n<b>+ 15 баллов</b>", parse_mode="html")
				requests.post(link+"plus.php", data={"tgid":message.chat.id, "balance":"30"})
			homebuttons(message)
		else:
			if str(message.chat.id)[0] == "-":
				chatid = str(message.chat.id)[1:]
				bot.send_message(message.chat.id, "Игрок <b><a href='tg://user?id={}'>{}</a></b> ответил не правильно.\n<b>-15</b>".format(message.from_user.id, message.from_user.first_name), parse_mode="html")
				requests.post(link+"minusC.php", data={"tgid":message.from_user.id, "chatid":chatid, "balance":"15"})
			else:
				bot.send_message(message.chat.id, "Увы, но Вы ответили неправильно.")
			homebuttons(message)

def task_hard(message):
	global five 
	text = message.text
	if text == "Отмена":
		if str(message.chat.id)[0] == "-":
			chatid = str(message.chat.id)[1:]
			bot.send_message(message.chat.id, "Игрок <b><a href='tg://user?id={}'>{}</a></b> отменил задание.\n<b>-100</b>".format(message.from_user.id, message.from_user.first_name), parse_mode="html")
			requests.post(link+"minusC.php", data={"tgid":message.from_user.id, "chatid":chatid, "balance":"100"})
		cancel(message)
	else:
		if text == str(five):
			if str(message.chat.id)[0] == "-":
				chatid = str(message.chat.id)[1:]
				bot.send_message(message.chat.id, "Игрок <b><a href='tg://user?id={}'>{}</a></b> ответил правильно.\n<b>+100</b>".format(message.from_user.id, message.from_user.first_name), parse_mode="html")
				requests.post(link+"plusC.php", data={"tgid":message.from_user.id, "chatid":chatid, "balance":"100"})
			else:
				bot.send_message(message.chat.id, "Поздравляю, Вы ответили правильно.\n<b>+ 100 баллов</b>", parse_mode="html")
				requests.post(link+"plus.php", data={"tgid":message.chat.id, "balance":"200"})
			homebuttons(message)
		else:
			if str(message.chat.id)[0] == "-":
				chatid = str(message.chat.id)[1:]
				bot.send_message(message.chat.id, "Игрок <b><a href='tg://user?id={}'>{}</a></b> ответил не правильно.\n<b>-100</b>".format(message.from_user.id, message.from_user.first_name), parse_mode="html")
				requests.post(link+"minusC.php", data={"tgid":message.from_user.id, "chatid":chatid, "balance":"100"})
			else:
				bot.send_message(message.chat.id, "Увы, но Вы ответили неправильно.")
			homebuttons(message)
			
def game(message):
	if message.text == "Легкий":
		if str(message.chat.id)[0] != "-":
			requests.post(link+"minus.php", data={"tgid":message.chat.id, "balance":"5"})
			bot.send_message(message.chat.id, "Заранее списано 5 монет.")
		global four
		one = 0.1
		two = 0.1
		three = 0.1
		four = 0.1
		fakeone = 0.1
		faketwo = 0.1
		fakethree = 0.1
		while '.' in str(one) or '.' in str(two) or '.' in str(three) or '.' in str(four) or '.' in str(fakeone) or '.' in str(faketwo) or '.' in str(fakethree):
			arithmetic = {
				"+": lambda x, y: x + y,
				"-": lambda x, y: x - y,
				"*": lambda x, y: x * y,
				"/": lambda x, y: x / y,
			}
			one=randint(0, 100)
			number = random.randint(1, 10)
			arithm = random.choice(list(arithmetic.keys()))
			two = arithmetic[arithm](one, number)
			three = arithmetic[arithm](two, number)
			four = arithmetic[arithm](three, number)

			fakeone = arithmetic[random.choice(list(arithmetic.keys()))](one, random.randint(1, 10))
			faketwo = arithmetic[random.choice(list(arithmetic.keys()))](two, random.randint(1, 10))
			fakethree = arithmetic[random.choice(list(arithmetic.keys()))](three, random.randint(1, 10))
		print("{}, {}, {}, {}".format(one, two, three, four)) 
		


		array = [str(fakeone), str(faketwo), str(fakethree), str(four)]
		a = random.choice(array)
		array.remove(str(a))
		b = random.choice(array)
		array.remove(str(b))
		c = random.choice(array)
		array.remove(str(c))
		d = random.choice(array)
		array.remove(str(d))

		bot.send_message(message.chat.id, "Уровень: Легкий.\nСтавка: 5 монет.")
		keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.row(a,b,c,d)
		keyboard.row("Отмена")
		bot.send_message(message.chat.id, "Вот тебе последовательность:\n<b>{}</b> ► <b>{}</b> ► <b>{}</b> ► <b>???</b>".format(one, two, three), parse_mode="html", reply_markup=keyboard)
		four= str(four)
		bot.register_next_step_handler(message, task_light)

	elif message.text == "Средний":
		if str(message.chat.id)[0] != "-":
			requests.post(link+"minus.php", data={"tgid":message.chat.id, "balance":"15"})
			bot.send_message(message.chat.id, "Заранее списано 30 монет.")
		global five
		one = 0.1
		two = 0.1
		three = 0.1
		four = 0.1
		five = 0.1
		fakeone = 0.1
		faketwo = 0.1
		fakethree = 0.1
		fakefour = 0.1
		while '.' in str(one) or '.' in str(two) or '.' in str(three) or '.' in str(four) or '.' in str(five) or '.' in str(fakeone) or '.' in str(faketwo) or '.' in str(fakethree) or '.' in str(fakefour):
			arithmetic1 = {
				"*": lambda x, y: x * y,
				"/": lambda x, y: x / y,
			}
			arithmetic2 = {
				"+": lambda x, y: x + y,
				"-": lambda x, y: x - y,
			}
			arithmeticF = {
				"+": lambda x, y: x + y,
				"-": lambda x, y: x - y,
				"*": lambda x, y: x * y,
				"/": lambda x, y: x / y,
			}
			one=randint(0, 100)
			number1 = random.randint(1, 10)
			number2 = random.randint(0, 100)

			arithm1 = random.choice(list(arithmetic1.keys()))
			arithm2 = random.choice(list(arithmetic2.keys()))
			two = arithmetic1[arithm1](one, number1)
			three = arithmetic2[arithm2](two, number2)
			four = arithmetic1[arithm1](three, number1)
			five = arithmetic2[arithm2](four, number2)

			fakeone = arithmeticF[random.choice(list(arithmeticF.keys()))](one, random.randint(1, 10))
			faketwo = arithmeticF[random.choice(list(arithmeticF.keys()))](two, random.randint(1, 10))
			fakethree = arithmeticF[random.choice(list(arithmeticF.keys()))](three, random.randint(1, 10))
			fakefour = arithmeticF[random.choice(list(arithmeticF.keys()))](three, random.randint(1, 10))
		print("{}, {}, {}, {}, {}".format(one, two, three, four, five)) 
		


		array = [str(fakeone), str(faketwo), str(fakethree), str(fakefour), str(five)]
		a = random.choice(array)
		array.remove(str(a))
		b = random.choice(array)
		array.remove(str(b))
		c = random.choice(array)
		array.remove(str(c))
		d = random.choice(array)
		array.remove(str(d))
		e = random.choice(array)
		array.remove(str(e))

		bot.send_message(message.chat.id, "Уровень: Средний.\nСтавка: 15 монет.")
		keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.row(a,b,c,d,e)
		keyboard.row("Отмена")
		bot.send_message(message.chat.id, "Вот тебе последовательность:\n<b>{}</b> ► <b>{}</b> ► <b>{}</b> ► <b>{}</b> ► <b>???</b>".format(one, two, three, four), parse_mode="html", reply_markup=keyboard)
		five= str(five)
		bot.register_next_step_handler(message, task_midle)

	elif message.text == "Сложный":
		if str(message.chat.id)[0] != "-":
			bot.send_message(message.chat.id, "Заранее списано 100 монет.")
			requests.post(link+"minus.php", data={"tgid":message.chat.id, "balance":"100"})
		one = 0.1
		two = 0.1
		three = 0.1
		four = 0.1
		five = 0.1
		fakeone = 0.1
		faketwo = 0.1
		fakethree = 0.1
		fakefour = 0.1
		while '.' in str(one) or '.' in str(two) or '.' in str(three) or '.' in str(four) or '.' in str(five) or '.' in str(fakeone) or '.' in str(faketwo) or '.' in str(fakethree) or '.' in str(fakefour):
			arithmetic = {
				"*": lambda x, y: x * y,
				"/": lambda x, y: x / y,
				"+": lambda x, y: x + y,
				"-": lambda x, y: x - y,
			}
			one=randint(100, 1000)
			number1 = random.randint(100, 1000)
			number2 = random.randint(100, 1000)
			arithm1 = random.choice(list(arithmetic.keys()))
			arithm2 = random.choice(list(arithmetic.keys()))
			two = arithmetic[arithm1](one, number1)
			three = arithmetic[arithm2](two, number2)
			four = arithmetic[arithm1](three, number1)
			five = arithmetic[arithm2](four, number2)

			fakeone = arithmetic[random.choice(list(arithmetic.keys()))](one, random.randint(100, 1000))
			faketwo = arithmetic[random.choice(list(arithmetic.keys()))](two, random.randint(100, 1000))
			fakethree = arithmetic[random.choice(list(arithmetic.keys()))](three, random.randint(100, 1000))
			fakefour = arithmetic[random.choice(list(arithmetic.keys()))](three, random.randint(100, 1000))
		print("{}, {}, {}, {}, {}".format(one, two, three, four, five)) 
		

		array = [str(fakeone), str(faketwo), str(fakethree), str(fakefour), str(five)]
		a = random.choice(array)
		array.remove(str(a))
		b = random.choice(array)
		array.remove(str(b))
		c = random.choice(array)
		array.remove(str(c))
		d = random.choice(array)
		array.remove(str(d))
		e = random.choice(array)
		array.remove(str(e))

		bot.send_message(message.chat.id, "Уровень: Сложный.\nСтавка: 100 монет.")
		keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.row(a,b,c,d,e)
		keyboard.row("Отмена")
		bot.send_message(message.chat.id, "Вот тебе последовательность:\n<b>{}</b> ► <b>{}</b> ► <b>{}</b> ► <b>{}</b> ► <b>???</b>".format(one, two, three, four), parse_mode="html", reply_markup=keyboard)
		five= str(five)
		bot.register_next_step_handler(message, task_hard)

	elif message.text == "Рулетка":
		a = 0
		arithmetic = {
				"+": lambda x, y: x + y,
				"-": lambda x, y: x - y,
			}
		b = randint(1, 100)
		arithm = random.choice(list(arithmetic.keys()))
		c = arithmetic[arithm](a, b)
		bot.send_message(message.chat.id, "<i>Генерируем</i>", parse_mode="html")
		time.sleep(1)
		bot.send_message(message.chat.id, "<i>Еще пару секунд</i>", parse_mode="html")
		time.sleep(1)
		bot.send_message(message.chat.id, "<i>Иииии.....</i>", parse_mode="html")
		time.sleep(1)
		if str(message.chat.id)[0] == "-":
			bot.send_message(message.chat.id, "{}: {}".format(message.from_user.first_name, c))
			chatid = str(message.chat.id)[1:]
			requests.post(link+"secretC.php", data={'chatid':chatid, 'tgid':message.from_user.id, 'balance':c})
			print("{} получил {}".format(message.from_user.first_name, c))
		else:
			bot.send_message(message.chat.id, "Итого: {}".format(c))
			requests.post(link+"secretC.php", data={'tgid':message.chat.id, 'balance':c})
			print("{} получил {}".format(message.chat.first_name, c))

	
	elif message.text == "Отмена":
		cancel(message)

	else:
		bot.send_message(message.chat.id, "Неизвестное значение")
		homebuttons(message)

def changename(message):
	keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.row('Выгрузить имя из телеграма')
	keyboard.row('Отмена')
	bot.send_message(message.chat.id, "Отправь мне своё новое имя", reply_markup=keyboard)
	bot.register_next_step_handler(message, newname)

def newname(message):
	text = message.text
	if text == "Отмена":
		cancel(message)
	elif text == "Выгрузить имя из телеграма":
		if str(message.chat.id)[0] == "-":
			requests.post(link+"newnameC.php", data={"chatid":message.chat.id, "tgid":message.from_user.id, "name":message.from_user.first_name})
			bot.send_message(message.chat.id, "Имя изменено:\n{}".format(message.from_user.first_name))
			homebuttons(message)
		else:
			requests.post(link+"newname.php", data={"tgid":message.chat.id, "name":message.chat.first_name})
			bot.send_message(message.chat.id, "Имя изменено:\n{}".format(message.chat.first_name))
			homebuttons(message)
	else:
		text = text.replace("\n", " ")
		if str(message.chat.id)[0] == "-":
			requests.post(link+"newnameC.php", data={"chatid":message.chat.id, "tgid":message.from_user.id, "name":text})
			bot.send_message(message.chat.id, "Имя изменено:\n{}".format(text))
			homebuttons(message)
		else:
			requests.post(link+"newname.php", data={"tgid":message.chat.id, "name":text})
			bot.send_message(message.chat.id, "Имя изменено:\n{}".format(text))
			homebuttons(message)

def rating(message):
	if str(message.chat.id)[0] == "-":
		chatid = str(message.chat.id)[1:]
		post = requests.post(link+"chatstat.php", data={'chatid':chatid})
	else:
		post = requests.post(link+"stat.php")
	maxi = len(post.json())
	i=0
	text="Лучшие:\n"
	if maxi == 0:
		text = "А лучших то и нету..."
	else:
		while i < maxi:
			text=text+"{}) {}, баланс {}\n".format(i+1, post.json()[i][2], post.json()[i][4])
			i+=1
		if str(message.chat.id)[0] == "-":
			pass
		else: 
			post = requests.post(link+"rating.php", data={'tgid':message.chat.id})
			rating = post.json()['rating']
			if int(rating) > 10:
				name = post.json()['name']
				balance = post.json()['balance']
				text=text+"...\n{}) {}, баланс {}\n".format(rating, name, balance)
	bot.send_message(message.chat.id, text)

def reborn(message):
	if str(message.chat.id)[0] == "-":
		pass
	else:
		requests.post(link+"reborn.php", data={"tgid":message.chat.id,"name":message.chat.first_name,"username":message.chat.username})
		bot.send_message(owner, '''Возрождение пользователя: <a href='tg://user?id={}'>{}</a>\nUsername: @{}\niD: <code>{}</code>\n'''.format(message.chat.id, message.chat.first_name, message.chat.username, message.chat.id), parse_mode="HTML")
		hello(message)
		homebuttons(message)

def rules(message):
	bot.send_message(message.chat.id, "Всё легко и просто.\nВыбираешь уровень. Тебе даётся ряд чисел. Надо понять последовательность БЕЗ КАЛЬКУЛЯТОРА и найти недостающее число!\nМонеты (баллы) списываются сразу, как только выбрали уровнь игры. За отмену задание монеты (баллы) тоже снимаются. \n\nСтоимость уровней:\nЛегкий - 5\nСредний - 15\nСложный - 100")

def donate(message):
	bot.send_message(message.chat.id, "Привет. Был бы рад копеечки на пивко ♥\n\nЧерез бота:\nhttps://t.me/FS88ch/72\n\n1. PAYPAL: https://paypal.me/FSystem88\n2. QIWI: https://qiwi.com/n/FSYSTEM88\n3. YANDEX MONEY: https://money.yandex.ru/to/410015440700904\n\nКарты:\nСбербанк - 2202200768133611\nТинькофф - 5213243890970674\nЯндекс - 5599005048615145\nКиви - 4693957557583098\n\n♥♥♥")

def balance(message):
	if str(message.chat.id)[0] == "-":
		chatid = str(message.chat.id)[1:]
		post = requests.post(link+"balanceC.php", data={'chatid':chatid, 'tgid':message.from_user.id})
		bot.send_message(message.chat.id, "Баланс <b><a href='tg://user?id={}'>{}</a></b> в этом чате: {}".format(message.from_user.id, message.from_user.first_name, post.json()["balance"]), parse_mode="html")
	else:
		post = requests.post(link+"balance.php", data={'tgid':message.from_user.id})
		bot.send_message(message.chat.id, "Твой баланс: {}".format(post.json()["balance"]))


# В РАЗРАБОТКЕ
def tourney(message):
	keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.row('Старт')
	keyboard.row('Записаться на турнир')
	keyboard.row('Правила турнира')
	#keyboard.row('Призы')
	keyboard.row('Отмена')
	bot.send_message(message.chat.id, '''Меню турнира:''', reply_markup=keyboard)
	bot.register_next_step_handler(message, tourney_next)

# В РАЗРАБОТКЕ
def tourney_next(message):
	if message.text == "Старт":
		if dt.now().weekday() == 6:
			now = dt.now().strftime("%H:%M:%S")
			t1 = "12:00:00"
			f = "%H:%M:%S"
			dtf = dt.strptime(now, f) - dt.strptime(t1, f)
			if 0 < dtf.seconds < 3600:
				startT(message)
			else:
				bot.send_message(message.chat.id, "Турнир проходит по воскресеньям с 12:00 до 13:00.")

		else:
			bot.send_message(message.chat.id, "Приходите в воскресенье...")
		bot.register_next_step_handler(message, tourney_next)
	elif message.text == "Записаться на турнир":
		req = requests.post(link+"regtour.php", data={"tgid":message.chat.id, "name":message.chat.first_name, "username":message.chat.username, "balance":"0"})
		if req.json()['result'] == "1":
			bot.send_message(message.chat.id, "Вы успешно зарегистрированы.")
		elif req.json()['result'] == "2":
			bot.send_message(message.chat.id, "Вы уже зарегистрированы.")
		bot.register_next_step_handler(message, tourney_next)
	elif message.text == "Правила турнира":
		bot.send_message(message.chat.id, '''
			• Для участия в турнире необходимо нажать на кнопку <b>"Записаться на турнир"</b> и подтвердить своё согласие.
			• Турнир будет проводиться каждую неделю по воскресеньям в 12:00 по Мск.
			• После регистрации надо будет дождаться подходящего времени и нажать на кнопку <b>"Старт"</b>.
			• Даётся 15 задач (по 5 задач из каждого уровня) и будет предложено 1 раз крутануть рулетку, а вдруг повезёт...
			• По окончанию прохождения всех задач надо нажать на на кнопку <b>"Завершить"</b>.
			• Так же бот будет считать за какое время вы решили все задания.
			• По окнчанию турнира алгоритм высчитает 3х победителей''', parse_mode="html")
		bot.register_next_step_handler(message, tourney_next)
	#elif message.text == "Призы":
	elif message.text == "Отмена":
		cancel(message)

# В РАЗРАБОТКЕ
def startT(message):
	bot.send_message(message.chat.id, "let's go")
	bot.register_next_step_handler(message, tourney_next)

@bot.message_handler(commands=['start'])
def handle_start(message):
	try:
		id=requests.post(link+"checknewid.php", data={'tgid':message.chat.id})
		if id.json()['tgid'] == "0":
			newuser(message)	
		else:
			if str(message.chat.id)[0] == "-":
				hello(message)
				homebuttons(message)
			else:
				olduser(message)
	except:
		pass


@bot.message_handler(commands=['game'])
def handle_game(message):
	try:
		homebuttons(message)
	except:
		pass


@bot.message_handler(func=lambda message: True, content_types=['text'])
def Main(message):
		if message.text == 'Отмена':
			cancel(message)
		elif message.text == 'Играть':
			level(message)
		elif message.text == 'Изменить имя':
			changename(message)
		elif message.text == 'Рейтинг':
			rating(message)
		elif message.text == 'Возобновить':
			hello(message)
			homebuttons(message)
		elif message.text == 'Сбросить':
			reborn(message)
		elif message.text == 'Инструкция':
			rules(message)
		elif message.text in ['Легкий','Средний','Сложный','Рулетка']:
			game(message)
		elif message.text == "Донатерная":
			donate(message)
		elif message.text == "Узнать баланс":
			balance(message)
		elif message.text == "Турнир":
			tourney(message)
		elif message.text == "Скрыть кнопки":
			deletekeyboard(message)
		

while True:
	try:
		bot.polling()
	except Exception as E:
		time.sleep(1)
