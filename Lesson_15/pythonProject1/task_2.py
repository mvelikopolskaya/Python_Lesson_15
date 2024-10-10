# Напишите скрипт, который получает текущее время и дату, а затем выводит их в
# формате YYYY-MM-DD HH:MM:SS. Дополнительно, выведите день недели и номер
# недели в году.

from datetime import datetime

current_date = datetime.now()
formatted_date = current_date.strftime('%Y-%m-%d %H:%M:%S')
current_day = current_date.strftime('%A')
week_number = current_date.isocalendar()[1]
print(f'Current date is {formatted_date}')
print(f'Current day is {current_day}')
print(f'Current week number is {week_number}')
