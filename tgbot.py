import json
import telebot
from datetime import datetime
from database import add_task, get_tasks, delete_task, init_db, renumber_tasks, mark_task_as_completed, set_due_time

bot = telebot.TeleBot("7054429485:AAEZSAk1_vN_3zrBZBHwza0TaDDmKbJHkLU")


# ТУДУ ЛИСТ БОТ

@bot.message_handler(commands=['start'])
def greet_user(message):
    mess = '''Добро пожаловать в бот To-Do List!

Тут вы можете написать ваши планы на день.

Комманды:

    /add - добавить задачу 
    /list - вывести список задач
    /delete - удалить
    /mark - отметить задачу выполненной
    /timer - добавить время до выполнения задачи
    /notes - заметки
    '''
    bot.send_message(message.chat.id, mess)


# Функция для загрузки задач из файла
def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


# Функция для сохранения задач в файл
def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=4)


tasks = load_tasks()


# ФУНКЦИЯ ДОБАВЛЕНИЯ ЗАДАЧИ

@bot.message_handler(commands=['add'])
def ask(message):
    msg = bot.reply_to(message, 'Введите задачу: ')
    bot.register_next_step_handler(msg, save)


def save(message):
    task = message.text
    add_task(task)  # Добавляем задачу в базу данных
    save_tasks(get_tasks())  # Сохраняем все задачи в файл
    bot.reply_to(message, f'Задача "{task}" добавлена!')


# ФУНКЦИЯ ПОКАЗА ВСЕХ ЗАДАЧ

@bot.message_handler(commands=['list'])
def show_everything(message):
    tasks = get_tasks()
    if tasks:
        response = 'Ваши задачи:\n'
        for task in tasks:
            status = '✅' if task[2] else ''
            due_time = f" (Время: {task[3]})" if task[3] else ''
            response += f'\n{task[0]}. {task[1]} {status}{due_time}'
    else:
        response = 'У вас пока нет записанных задач.'
    bot.reply_to(message, response)


# ФУНКЦИЯ УДАЛЕНИЯ ЗАДАЧИ

@bot.message_handler(commands=['delete'])
def get_task_id(message):
    tasks = get_tasks()
    if tasks:
        response = 'Выберите задачу для удаления:\n'
        for task in tasks:
            response += f'\n{task[0]}. {task[1]}'
        msg = bot.reply_to(message, response)
        bot.register_next_step_handler(msg, remove_task)
    else:
        response = 'У вас нет задач для удаления.'
        bot.reply_to(message, response)


def remove_task(message):
    try:
        task_id = int(message.text)
        delete_task(task_id)
        renumber_tasks()
        bot.reply_to(message, f"Задача номер {task_id} удалена.")
    except ValueError:
        bot.reply_to(message, "Пожалуйста, введите корректный номер задачи.")


# ФУНКЦИЯ ДЛЯ ОТМЕТКИ ЗАДАЧУ ВЫПОЛНЕННОЙ

@bot.message_handler(commands=['mark'])
def get_id(message):
    tasks = get_tasks()
    if tasks:
        response = 'Выберите выполненную задачу:\n'
        for task in tasks:
            status = '✅' if task[2] else ''
            response += f'\n{task[0]}. {task[1]} {status}'
        msg = bot.reply_to(message, response)
        bot.register_next_step_handler(msg, mark_task)
    else:
        response = 'У вас нет задач для удаления.'
        bot.reply_to(message, response)


def mark_task(message):
    try:
        task_id = int(message.text)
        mark_task_as_completed(task_id)
        tasks = get_tasks()
        response = ''
        for task in tasks:
            status = "✅" if task[2] else ""
            response += f'\n{task[0]}. {task[1]} {status}'
        bot.edit_message_text(chat_id=message.chat.id,
                              message_id=message.message_id - 1,
                              text=response)
        bot.send_message(message.chat.id, 'Так держать!')
    except ValueError:
        bot.reply_to(message, "Пожалуйста, введите корректный номер задачи.")


# ВРЕМЯ НА ВЫПОЛНЕНИЕ ЗАДАЧИ

@bot.message_handler(commands=['timer'])
def ask_for_task(message):
    tasks = get_tasks()
    if tasks:
        response = 'Выберите задачу чтобы поставить таймер:\n'
        for task in tasks:
            status = "✅" if task[2] else ""
            due_time = task[3] if task[3] else ''
            response += f'\n{task[0]}. {task[1]} {status} (Время: {due_time})'
        msg = bot.reply_to(message, response)
        bot.register_next_step_handler(msg, ask_for_time)
    else:
        bot.reply_to(message, "У вас нет задач для установки времени.")


def ask_for_time(message):
    try:
        task_id = int(message.text)
        msg = bot.reply_to(message, 'Введите время выполнения задачи (в формате ЧЧ:ММ): ')
        bot.register_next_step_handler(msg, lambda m: save_due_time(m, task_id))
    except ValueError:
        bot.reply_to(message, "Пожалуйста, введите корректный номер задачи.")


def save_due_time(message, task_id):
    try:
        due_time = datetime.strptime(message.text, "%H:%M").strftime("%H:%M")
        set_due_time(task_id, due_time)
        bot.reply_to(message, f'Время для задачи {task_id} установлено на {due_time}')
    except ValueError:
        bot.reply_to(message, "Пожалуйста, введите время в правильном формате (ЧЧ:ММ).")


# Инициализация базы данных
if __name__ == "__main__":
    init_db()

# Запуск бота
bot.polling(none_stop=True)
