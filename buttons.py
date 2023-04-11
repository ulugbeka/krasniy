from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#Knopka dlya otpravki nomera telefona
def phone_number_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Podelitsya kontaktom', request_contact=True)
    kb.add(button)
    return kb

#Knopka dlya otpravki nomera locatsii
def location_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Podelitsya locatsiey', request_location=True)
    kb.add(button)
    return kb
#Knopka dlya vibora pola
def gender_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Mujchina')
    button2 = KeyboardButton('Jenshina')
    kb.add(button, button2)
    return kb
#Knopki dlya vibora kolichestva
def product_count():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    buttons = [KeyboardButton(str(i)) for i in range(1, 10)]
    back = KeyboardButton('Nazad')
    kb.add(*buttons, back)
    return kb
#Knopki dlya korzini
def cart_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Ochistit')
    button2 = KeyboardButton('Oformit zakaz')
    button3 = KeyboardButton('Redaktirovat')
    button4 = KeyboardButton('Nazad')
    kb.add(button, button2, button3, button4)
    return kb
#Knopki pri vibore sposoba oplati
def pay_type_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Nalichnie')
    button2 = KeyboardButton('Kartoy')
    button3 = KeyboardButton('Nazad')
    kb.add(button, button2, button3)
    return kb
#Knopki dlya potverjdeniya zakaza
def confirmation_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Podtverdit')
    button2 = KeyboardButton('Otmenit')
    button3 = KeyboardButton('Nazad')
    kb.add(button, button2, button3)
    return kb


#Knopki s nazvaniyami tovarov
def products_kb():
    pass