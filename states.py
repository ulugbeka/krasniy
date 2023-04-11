from aiogram.dispatcher.filters.state import State, StatesGroup


#Processi dlya registraci
class Registration(StatesGroup):
    getting_name_state = State()
    getting_phone_number_state = State()
    getting_location = State()
    getting_gender = State()

#Processi dlya vibora opredelennogo tovara
class GetProduct(StatesGroup):
    getting_pr_name = State()
    getting_pr_count = State()

#Processi pri rabote s korzinoy
class Cart(StatesGroup):
    waiting_for_product = State()
    waiting_new_count = State()


#Processi pri oformlenii zakaza
class Order(StatesGroup):
    waiting_location = State()
    waiting_pay_type = State()
    waiting_accept = State()