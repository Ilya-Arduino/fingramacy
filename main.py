import random
import telebot
from telebot import types #
API_TOKEN = '7619267652:AAFln8hLqlUK8THIJX1rJI8HDuzaDvyqNyM'

bot = telebot.TeleBot(API_TOKEN)
level = 0
users_id_complexity = {}
users_id_count = {}
users_id_actions_cein = {}
users_id_actions_hms = {}
users_id_actions_cein_summ = {}
users_id_actions_cein_summ_minus = {}
bySum = {}
bySumHms = {}
soldSum = {}
soldSumHms = {}
dayCounter = {}
sum_proc_counter = {}
def regUser(ident, i):
    if ident in users_id_complexity:
        print("User ", ident, " is registred!")
        return 'fatal'
    else:
        users_id_complexity[ident] = i
        if i == 1:
            users_id_count[ident] = 10000
        if i == 2:
            users_id_count[ident] = 6000
        if i == 3:
            users_id_count[ident] = 3000
        users_id_actions_cein[ident] = 0
        sum_proc_counter[ident] = 0
        users_id_actions_cein_summ[ident] = 0
        users_id_actions_hms[ident] = 0
        users_id_actions_cein_summ_minus[ident] = 0
        dayCounter[ident] = 0
        print(users_id_complexity)
# Обработка '/start' и '/help'


@bot.message_handler(commands=['help', 'start'])
def start(message):
    markup_start = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Easy", callback_data = '1')
    button2 = types.InlineKeyboardButton("Normal", callback_data = '2')
    button3 = types.InlineKeyboardButton("Hard", callback_data = '3')
    markup_start.add(button1)
    markup_start.add(button2)
    markup_start.add(button3)
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Добро пожаловать в интерактивную игру, в которой ты будешь инвестором! \
В твоём распоряжении будут некоторые финансы, выбери уровень сложности:".format(message.from_user), reply_markup=markup_start)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    markup_callback = types.InlineKeyboardMarkup()
    bt_1 = types.InlineKeyboardButton("Назад", callback_data = 'return')
    markup_callback.row(bt_1)
    if callback.data == '1':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        if regUser(callback.message.chat.id, 1) == "fatal":
            bot.send_message(callback.message.chat.id, "Ой! Пользователь уже зарегестрирован!", reply_markup=markup_callback)
        else:
            
            bot.send_message(callback.message.chat.id, "Отлично! Добро пожаловать в игру!\n\
С этого момента тебе необходимо правильно распределять свой капитал\n\
Ты можешь купить или продать акции, подписывать договоры, и многое другое. Твой стартовый капитал: " + str(users_id_count[callback.message.chat.id]), reply_markup=markup_callback)
    if callback.data == '2':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        if regUser(callback.message.chat.id, 2) == "fatal":
            bot.send_message(callback.message.chat.id, "Ой! Пользователь уже зарегестрирован!", reply_markup=markup_callback)
        else:

            bot.send_message(callback.message.chat.id, "Отлично! Добро пожаловать в игру!\n\
С этого момента тебе необходимо правильно распределять свой капитал\n\
Ты можешь купить или продать акции, подписывать договоры, и многое другое. Твой стартовый капитал: " + str(users_id_count[callback.message.chat.id]), reply_markup=markup_callback)
    if callback.data == '3':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        if regUser(callback.message.chat.id, 3) == "fatal":
            bot.send_message(callback.message.chat.id, "Ой! Пользователь уже зарегестрирован!", reply_markup=markup_callback)
        else:
            
            bot.send_message(callback.message.chat.id, "Отлично! Добро пожаловать в игру!\n\
С этого момента тебе необходимо правильно распределять свой капитал\n\
Ты можешь купить или продать акции, подписывать договоры, и многое другое. Твой стартовый капитал: " + str(users_id_count[callback.message.chat.id]), reply_markup=markup_callback)
    if callback.data == 'check':
        markup = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton("Назад", callback_data="return")
        markup.row(bt_1)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, "Уровень сложности : " + str(users_id_complexity[callback.message.chat.id]) + " \nБаланс: " + str(users_id_count[callback.message.chat.id]) + " ₽", reply_markup=markup)
# Обработка всех остальных сообщений с типом контента 'текст' (по умолчанию для content_types используется ['текст'])
    if callback.data == "return":
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        markup_2 = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton("Проверить баланс", callback_data = 'check')
        bt_2 = types.InlineKeyboardButton("Купить акции", callback_data = 'stocks')
        bt_5 = types.InlineKeyboardButton("Продать акции", callback_data = 'sold_stocks')
        bt_3 = types.InlineKeyboardButton("Список моих акций", callback_data = 'spis_act')
        bt_4 = types.InlineKeyboardButton("Следующий день торгов", callback_data = 'next_day')
        bt_6 = types.InlineKeyboardButton("Как играть?", callback_data = 'how_to_play')
        markup_2.row(bt_1, bt_3)
        markup_2.row(bt_2, bt_5)
        markup_2.row(bt_4, bt_6)
        if callback.message.chat.id in users_id_complexity:
                bot.send_message(callback.message.chat.id, "Босс, что вы хотите предпринять сегодня?\
                ", reply_markup=markup_2)
        else:
                bot.send_message(callback.message.chat.id, "Для начала пройдите регистрацию.\
                 ")
    if callback.data == "stocks":
        markup_actions = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton("Центр-Инвест", callback_data = 'center_invest')
        bt_3 = types.InlineKeyboardButton("HMSTR", callback_data = 'hmstr')
        bt_4 = types.InlineKeyboardButton("Назад", callback_data = 'return')
        markup_actions.row(bt_1)
        markup_actions.row(bt_3, bt_4)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, "Вот список актуальных акций:  \n", reply_markup=markup_actions)

    if callback.data == "how_to_play":
        markup = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton("Назад", callback_data="return")
        markup.row(bt_1)
        bot.send_message(callback.message.chat.id, "Дорогой игрок! Ты попал в место, где ты можешь как заработать, так и потерять ВСЁ! Вот основные принципы игры:\n\
✔Покупка акций : Для начала вам необходимо ознакомится с акциями по их описанию. Рекомендуем вкладываться в акции проверенных компаний.\n\
✔Следующий день торгов: Нажав на данный пункт ваши активы возрастут или упадут в соответствии с курсом. За ограниченоое количество дней вам необходимо приумножить свой доход.\n\
✔Продажа акций: Если вы видите, что акции летят вниз, и не приносят доход, вы можете продать их, сохранив свои деньги.\n\
Доходность завивит от акции, а так же от уровня сложности. Изначальная сумма так же зависит от уровня сложности.\n\
В конце игры, когда закончатся сроки ваших инвестиций, вы узнаете, заработали ли вы на своих активах или нет.", reply_markup=markup)
    if callback.data == "sold_stocks":
        markup_actions_sold = types.InlineKeyboardMarkup()
        try:
         if users_id_actions_cein[callback.message.chat.id] > 0:
            bt_1 = types.InlineKeyboardButton("Центр-Инвест", callback_data = 'sold_cein')
         else:
            bt_1 = types.InlineKeyboardButton("Нет акций", callback_data = 'return')
        except:
            bt_1 = types.InlineKeyboardButton("Нет акций", callback_data = 'return')
        try:
         if users_id_actions_hms[callback.message.chat.id] > 0:
            bt_3 = types.InlineKeyboardButton("HMSTR", callback_data = 'sold_hmstr')
         else:
            bt_3 = types.InlineKeyboardButton("Нет акций", callback_data = 'return')
        except:
            bt_3 = types.InlineKeyboardButton("Нет акций", callback_data = 'return')
        bt_4 = types.InlineKeyboardButton("Назад", callback_data = 'return')
        markup_actions_sold.row(bt_1)
        markup_actions_sold.row(bt_3, bt_4)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, "Вот список ваших акций:  \n", reply_markup=markup_actions_sold)
    if callback.data == 'sold_cein':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, "Введите сумму на которую хотите вывести акций. Минимальная сумма: 1200 Ваши акции = " + str(users_id_actions_cein[callback.message.chat.id]))
        bot.register_next_step_handler(callback.message, onSold)
    if callback.data == 'sold_hmstr':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, "Введите сумму на которую хотите вывести акций. Минимальная сумма: 1200 Ваши акции = " + str(users_id_actions_hms[callback.message.chat.id]))
        bot.register_next_step_handler(callback.message, onSoldHms)
    if callback.data == 'center_invest':
        markup_center_invest = types.InlineKeyboardMarkup()
        bt_2 = types.InlineKeyboardButton("Назад", callback_data="return")
        bt_1 = types.InlineKeyboardButton("Купить", callback_data = 'buy_cein')
        markup_center_invest.row(bt_1, bt_2)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, "ПАО КБ Центр-инвест создан в 1992 году. Банк Центр-инвест входит в ТОП-50 надежных банков России по версии издания Forbes.\n", reply_markup=markup_center_invest)
    if callback.data == 'hmstr':
        markup_center_invest = types.InlineKeyboardMarkup()
        bt_2 = types.InlineKeyboardButton("Назад", callback_data="return")
        bt_1 = types.InlineKeyboardButton("Купить", callback_data = 'buy_hmstr')
        markup_center_invest.row(bt_1, bt_2)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, "Недавно появились на рынке. Доходность осуществляется за счёт юных тапальщиков. Стабильность не изучена.\n", reply_markup=markup_center_invest)
    if callback.data == 'buy_cein':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, "Введите сумму на которую хотите купить акций. Минимальная сумма: 1200 Ваш баланс = " + str(users_id_count[callback.message.chat.id]))
        bot.register_next_step_handler(callback.message, onBuy)
    if callback.data == 'buy_hmstr':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, "Введите сумму на которую хотите купить хомяков. Минимальная сумма: 1200 Ваш баланс = " + str(users_id_count[callback.message.chat.id]))
        bot.register_next_step_handler(callback.message, onBuyHms)
    if callback.data == 'buy_done':
        markup_actions = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton("Назад", callback_data = 'return')
        markup_actions.row(bt_1)
        users_id_count[callback.message.chat.id] = int(users_id_count[callback.message.chat.id] - bySum[callback.message.chat.id])
        try:
          users_id_actions_cein[callback.message.chat.id] = users_id_actions_cein[callback.message.chat.id] + bySum[callback.message.chat.id]
        except:
          users_id_actions_cein[callback.message.chat.id] = 0 + bySum[callback.message.chat.id]
         
        print("ok " + str(users_id_count[callback.message.chat.id]))
        bot.send_message(callback.message.chat.id, "Поздравляем с покупкой! Уверены, что это решение было правильным. Ваш баланс: " + str(users_id_count[callback.message.chat.id]), reply_markup=markup_actions)
    if callback.data == 'buy_done_hmstr':
        markup_actions = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton("Назад", callback_data = 'return')
        markup_actions.row(bt_1)
        users_id_count[callback.message.chat.id] = int(users_id_count[callback.message.chat.id] - bySumHms[callback.message.chat.id])
        try:
          users_id_actions_hms[callback.message.chat.id] = users_id_actions_hms[callback.message.chat.id] + bySumHms[callback.message.chat.id]
        except:
          users_id_actions_hms[callback.message.chat.id] = 0 + bySumHms[callback.message.chat.id]
         
        print("ok " + str(users_id_count[callback.message.chat.id]))
        bot.send_message(callback.message.chat.id, "Поздравляем с покупкой! Уверены, что это решение было правильным. Ваш баланс: " + str(users_id_count[callback.message.chat.id]), reply_markup=markup_actions)

    if callback.data == 'sold_done':
        markup_actions = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton("Назад", callback_data = 'return')
        markup_actions.row(bt_1)
        users_id_count[callback.message.chat.id] = (int(users_id_count[callback.message.chat.id] + int(soldSum[callback.message.chat.id])))
        try:
          users_id_actions_cein[callback.message.chat.id] = users_id_actions_cein[callback.message.chat.id] - soldSum[callback.message.chat.id]
        except:
          print("fatal sold error")
         
        print("ok " + str(users_id_count[callback.message.chat.id]))
        bot.send_message(callback.message.chat.id, "Поздравляем с покупкой! Уверены, что это решение было правильным. Ваш баланс: " + str(users_id_count[callback.message.chat.id]), reply_markup=markup_actions)
    
    if callback.data == 'sold_hms_done':
        markup_actions = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton("Назад", callback_data = 'return')
        markup_actions.row(bt_1)
        users_id_count[callback.message.chat.id] = (int(users_id_count[callback.message.chat.id] + int(soldSumHms[callback.message.chat.id])))
        try:
          users_id_actions_hms[callback.message.chat.id] = users_id_actions_hms[callback.message.chat.id] - soldSumHms[callback.message.chat.id]
        except:
          print("fatal sold error")
         
        print("ok " + str(users_id_count[callback.message.chat.id]))
        bot.send_message(callback.message.chat.id, "Поздравляем с покупкой! Уверены, что это решение было правильным. Ваш баланс: " + str(users_id_count[callback.message.chat.id]), reply_markup=markup_actions)

    if callback.data == 'spis_act':
        global cein
        markup_actions = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton("Назад", callback_data = 'return')
        markup_actions.row(bt_1)
        try:
         if users_id_actions_cein[callback.message.chat.id]:
          cein = str(users_id_actions_cein[callback.message.chat.id]) + "Р"
         else:
          cein = "Нет данных"
        except:
         cein = "Нет данных"
        try:
         if users_id_actions_hms[callback.message.chat.id]:
          cein_hms = str(users_id_actions_hms[callback.message.chat.id]) + "Р"
         else:
          cein_hms = "Нет данных"
        except:
         cein_hms = "Нет данных"
        bot.send_message(callback.message.chat.id, "Ваши акции: \n" + "Центр-Инвест:  " + cein +"\n\
HMSTR: " + cein_hms, reply_markup=markup_actions)
    if callback.data == 'next_day':
        il = 0
        markup_actions = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton("Назад", callback_data = 'return')
        markup_actions.row(bt_1)
        choice_list_1 = [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
        choice_list_2 = [1, 0, 1, 0, 1, 0, 1]
        choice_list_3 = [1, 0, 1, 0, 1, 0, 1, 0, 0]
        choice_list_1_hms = [1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0]
        choice_list_2_hms = [1, 0, 1, 0, 1, 0]
        choice_list_3_hms = [1, 0, 1, 0, 1, 0, 1, 0, 0]
        if users_id_complexity[callback.message.chat.id] == 1:
         il = random.choice(choice_list_1)
         if il == 0:
          proc_cein = random.randint(3, 12)
         else:
          proc_cein = random.randint(3, 14)
        if users_id_complexity[callback.message.chat.id] == 2:
         il = random.choice(choice_list_2)
         if il == 0:
          proc_cein = random.randint(4, 14)
         else:
          proc_cein = random.randint(4, 18)
        if users_id_complexity[callback.message.chat.id] == 3:
         proc_cein = random.randint(12, 28)
         il = random.choice(choice_list_3)
        if users_id_complexity[callback.message.chat.id] == 1:
         il_hms = random.choice(choice_list_1_hms)
         if il_hms == 0:
          proc_hms = random.randint(6, 18)
         else:
          proc_hms = random.randint(6, 18)
        if users_id_complexity[callback.message.chat.id] == 2:
         il_hms = random.choice(choice_list_2_hms)
         if il_hms == 0:
          proc_hms = random.randint(6, 20)
         else:
          proc_hms = random.randint(6, 20)
        if users_id_complexity[callback.message.chat.id] == 3:
         proc_hms = random.randint(12, 70)
         il_hms = random.choice(choice_list_3_hms)
        if(il == 0):
            znak = "-"
        else:
            znak = "+"
        if(il_hms == 0):
            znak_hms = "-"
        else:
            znak_hms = "+"
    #try:
        if il == 0:
            if users_id_actions_cein[callback.message.chat.id] != 0 or users_id_actions_hms[callback.message.chat.id] != 0:
             i = counter_minus(int(users_id_actions_cein[callback.message.chat.id]), proc_cein)
             sum_proc_counter[callback.message.chat.id] = sum_proc_counter[callback.message.chat.id] - proc_cein
            else:
             bot.send_message(callback.message.chat.id, "Пока что у вас нет акций", reply_markup=markup_actions)

        else:
            if users_id_actions_cein[callback.message.chat.id] != 0 or users_id_actions_hms[callback.message.chat.id] != 0:
             i = counter_plus(int(users_id_actions_cein[callback.message.chat.id]), proc_cein)
             sum_proc_counter[callback.message.chat.id] = sum_proc_counter[callback.message.chat.id] + proc_cein
            else:
                return
        if il_hms == 0:
            if users_id_actions_cein[callback.message.chat.id] != 0 or users_id_actions_hms[callback.message.chat.id] != 0:
             i_hms = counter_minus(int(users_id_actions_hms[callback.message.chat.id]), proc_cein)
             sum_proc_counter[callback.message.chat.id] = sum_proc_counter[callback.message.chat.id] - proc_hms
            else:
             bot.send_message("Пока что у вас нет акций", reply_markup=markup_actions)

        else:
            if users_id_actions_cein[callback.message.chat.id] != 0 or users_id_actions_hms[callback.message.chat.id] != 0:
             i_hms = counter_plus(int(users_id_actions_hms[callback.message.chat.id]), proc_cein)
             sum_proc_counter[callback.message.chat.id] = sum_proc_counter[callback.message.chat.id] + proc_hms
            else:
                return
        users_id_actions_cein[callback.message.chat.id] = int(i)
        users_id_actions_hms[callback.message.chat.id] = int(i_hms)
        print(users_id_actions_cein[callback.message.chat.id])
        print(users_id_actions_hms[callback.message.chat.id])
        try:
         dayCounter[callback.message.chat.id] = dayCounter[callback.message.chat.id] + 1
        except:
         dayCounter[callback.message.chat.id] = 0 + 1
        if str(int((users_id_complexity[callback.message.chat.id]) * 3) - int(dayCounter[callback.message.chat.id])) == "0":
            itog(callback.message.chat.id)
        else:
         bot.send_message(callback.message.chat.id, "Итог дня: \n" + "Центр-Инвест:  " + str(users_id_actions_cein[callback.message.chat.id]) + " ( " + znak + str(proc_cein) + " % )\n\
" + "HMSTR:  " + str(users_id_actions_hms[callback.message.chat.id]) + " ( " + znak_hms + str(proc_hms) + " % )" + " Общие показатели по акции за всё время: " + str(sum_proc_counter[callback.message.chat.id]) + " %" + "Дней осталось: " + str(int((users_id_complexity[callback.message.chat.id]) * 3) - int(dayCounter[callback.message.chat.id])), reply_markup=markup_actions)
    #except:
       # return
def itog(index_itog):
    if users_id_complexity[index_itog] == 1:
        if (10000 - (int(users_id_count[index_itog]) + int(users_id_actions_cein[index_itog]) + int(users_id_actions_hms[index_itog]))) > 0:
            bot.send_message(index_itog, "Вы БАНКРОТ! Сумма на вашем счету за время инвестиций стала меньше изначальной.")
        elif (10000 - (int(users_id_count[index_itog]) + int(users_id_actions_cein[index_itog]) + int(users_id_actions_hms[index_itog]))) < 0:
            bot.send_message(index_itog, "Ваш бизнес вырос! Вы прошли миссию! Ваш доход составил: " + str(int((int(users_id_count[index_itog]) + int(users_id_actions_cein[index_itog]) + int(users_id_actions_hms[index_itog]))) - 10000))
        else: 
            bot.send_message(index_itog, "Ваш бизнес не принёс прибыли. Однако у вас нет убытка, поздравляем!")
    if users_id_complexity[index_itog] == 2:
        if (6000 - (int(users_id_count[index_itog]) + int(users_id_actions_cein[index_itog]) + int(users_id_actions_hms[index_itog]))) > 0:   
            bot.send_message(index_itog, "Вы БАНКРОТ! Сумма на вашем счету за время инвестиций стала меньше изначальной.")
        elif (6000 - (int(users_id_count[index_itog]) + int(users_id_actions_cein[index_itog]) + int(users_id_actions_hms[index_itog]))) < 0:
            bot.send_message(index_itog, "Ваш бизнес вырос! Вы прошли миссию! Ваш доход составил: " + str(int((int(users_id_count[index_itog]) + int(users_id_actions_cein[index_itog]) + int(users_id_actions_hms[index_itog]))) - 6000))
        else: 
            bot.send_message(index_itog, "Ваш бизнес не принёс прибыли. Однако у вас нет убытка, поздравляем!")
    if users_id_complexity[index_itog] == 3:
        if (3000 - (int(users_id_count[index_itog]) + int(users_id_actions_cein[index_itog]) + int(users_id_actions_hms[index_itog]))) > 0:   
            bot.send_message(index_itog, "Вы БАНКРОТ! Сумма на вашем счету за время инвестиций стала меньше изначальной.")
        elif (3000 - (int(users_id_count[index_itog]) + int(users_id_actions_cein[index_itog]) + int(users_id_actions_hms[index_itog]))) < 0:
            bot.send_message(index_itog, "Ваш бизнес вырос! Вы прошли миссию! Ваш доход составил: " + str(int((int(users_id_count[index_itog]) + int(users_id_actions_cein[index_itog]) + int(users_id_actions_hms[index_itog]))) - 3000))
        else: 
            bot.send_message(index_itog, "Ваш бизнес не принёс прибыли. Однако у вас нет убытка, поздравляем!")

def counter_plus(p, r):      
 si = (p*r)/100+p
 return round(si + 1)
def counter_minus(p, r):      
 si = p-(p*r)/100
 return round(si)


def onBuy(message):
    markup_center_invest = types.InlineKeyboardMarkup()
    markup_center_invest_notpay = types.InlineKeyboardMarkup()
    bt_2 = types.InlineKeyboardButton("Назад", callback_data="return")
    bt_1 = types.InlineKeyboardButton("Купить", callback_data = 'buy_done')
    markup_center_invest.row(bt_1, bt_2)
    markup_center_invest_notpay.row(bt_2)
    if message.text.isdigit():
        if int(message.text) >= 1200:
            if int(message.text) <= users_id_count[message.chat.id]:
                 buythis(int(message.text), message.chat.id)
                 bot.delete_message(message.chat.id, message.message_id)
                 bot.send_message(message.chat.id, "Ваше решение окончательно? \nВаш баланс: " + str(users_id_count[message.chat.id]) + " Р Спишется: " + message.text + " Р.", reply_markup=markup_center_invest)
            else:
                 bot.send_message(message.chat.id, "Вы пытаетесь потратить больше денег, чем у вас есть на счету!", reply_markup=markup_center_invest_notpay)
        else:
            bot.send_message(message.chat.id, "Минимальная сумма для покупки акции - 1200", reply_markup=markup_center_invest_notpay)
    else:
        bot.send_message(message.chat.id, "Ошибка формата, Введённые данные недопустимы. Введите целое число без иных символов.", reply_markup=markup_center_invest_notpay)
def buythis(i, message):
    bySum[message] = i 

def onBuyHms(message):
    markup_center_invest = types.InlineKeyboardMarkup()
    markup_center_invest_notpay = types.InlineKeyboardMarkup()
    bt_2 = types.InlineKeyboardButton("Назад", callback_data="return")
    bt_1 = types.InlineKeyboardButton("Купить", callback_data = 'buy_done_hmstr')
    markup_center_invest.row(bt_1, bt_2)
    markup_center_invest_notpay.row(bt_2)
    if message.text.isdigit():
        if int(message.text) >= 1200:
            if int(message.text) <= users_id_count[message.chat.id]:
                 buyhms(int(message.text), message.chat.id)
                 bot.delete_message(message.chat.id, message.message_id)
                 bot.send_message(message.chat.id, "Ваше решение окончательно? \nВаш баланс: " + str(users_id_count[message.chat.id]) + " Р Спишется: " + message.text + " Р.", reply_markup=markup_center_invest)
            else:
                 bot.send_message(message.chat.id, "Вы пытаетесь потратить больше денег, чем у вас есть на счету!", reply_markup=markup_center_invest_notpay)
        else:
            bot.send_message(message.chat.id, "Минимальная сумма для покупки акции - 1200", reply_markup=markup_center_invest_notpay)
    else:
        bot.send_message(message.chat.id, "Ошибка формата, Введённые данные недопустимы. Введите целое число без иных символов.", reply_markup=markup_center_invest_notpay)
def buyhms(i, message):
    bySumHms[message] = i     

def onSoldHms(message):
    markup_center_invest = types.InlineKeyboardMarkup()
    markup_center_invest_notpay = types.InlineKeyboardMarkup()
    bt_2 = types.InlineKeyboardButton("Назад", callback_data="return")
    bt_1 = types.InlineKeyboardButton("Продать", callback_data = 'sold_hms_done')
    markup_center_invest.row(bt_1, bt_2)
    markup_center_invest_notpay.row(bt_2)
    if message.text.isdigit():
        if int(message.text) >= 1200:
            if int(message.text) <= users_id_actions_hms[message.chat.id]:
                 soldhms(int(message.text), message.chat.id)
                 bot.delete_message(message.chat.id, message.message_id)
                 bot.send_message(message.chat.id, "Ваше решение окончательно? \nВаш баланс: " + str(users_id_count[message.chat.id]) + " Р Спишется: " + message.text + " Р.", reply_markup=markup_center_invest)
            else:
                 bot.send_message(message.chat.id, "Вы пытаетесь потратить больше денег, чем у вас есть на счету!", reply_markup=markup_center_invest_notpay)
        else:
            bot.send_message(message.chat.id, "Минимальная сумма для продажи акции - 1200", reply_markup=markup_center_invest_notpay)
    else:
        bot.send_message(message.chat.id, "Ошибка формата, Введённые данные недопустимы. Введите целое число без иных символов.", reply_markup=markup_center_invest_notpay)
def soldhms(i, message):
    soldSumHms[message] = i    

def onSold(message):
    markup_center_invest = types.InlineKeyboardMarkup()
    markup_center_invest_notpay = types.InlineKeyboardMarkup()
    bt_2 = types.InlineKeyboardButton("Назад", callback_data="return")
    bt_1 = types.InlineKeyboardButton("Продать", callback_data = 'sold_done')
    markup_center_invest.row(bt_1, bt_2)
    markup_center_invest_notpay.row(bt_2)
    if message.text.isdigit():
        if int(message.text) >= 1200:
            if int(message.text) <= users_id_actions_cein[message.chat.id]:
                 soldcein(int(message.text), message.chat.id)
                 bot.delete_message(message.chat.id, message.message_id)
                 bot.send_message(message.chat.id, "Ваше решение окончательно? \nВаш баланс: " + str(users_id_count[message.chat.id]) + " Р Спишется: " + message.text + " Р.", reply_markup=markup_center_invest)
            else:
                 bot.send_message(message.chat.id, "Вы пытаетесь потратить больше денег, чем у вас есть на счету!", reply_markup=markup_center_invest_notpay)
        else:
            bot.send_message(message.chat.id, "Минимальная сумма для продажи акции - 1200", reply_markup=markup_center_invest_notpay)
    else:
        bot.send_message(message.chat.id, "Ошибка формата, Введённые данные недопустимы. Введите целое число без иных символов.", reply_markup=markup_center_invest_notpay)
def soldcein(i, message):
    soldSum[message] = i   
        
        
@bot.message_handler(func=lambda message: True)
def onClick(message):
        bot.delete_message(message.chat.id, message.message_id)
        markup_2 = types.InlineKeyboardMarkup()
        bt_1 = types.InlineKeyboardButton("Проверить баланс", callback_data = 'check')
        bt_2 = types.InlineKeyboardButton("Купить акции", callback_data = 'stocks')
        bt_5 = types.InlineKeyboardButton("Продать акции", callback_data = 'sold_stocks')
        bt_3 = types.InlineKeyboardButton("Список моих акций", callback_data = 'spis_act')
        bt_4 = types.InlineKeyboardButton("Следующий день торгов", callback_data = 'next_day')
        bt_6 = types.InlineKeyboardButton("Как играть?", callback_data = 'how_to_play')
        markup_2.row(bt_1, bt_3)
        markup_2.row(bt_2, bt_5)
        markup_2.row(bt_4, bt_6)
        if message.chat.id in users_id_complexity:
                bot.send_message(message.chat.id, "Босс, что вы хотите предпринять сегодня?\
                ", reply_markup=markup_2)
        else:
                bot.send_message(message.chat.id, "Для начала пройдите регистрацию.\
                 ")
        


bot.infinity_polling()
