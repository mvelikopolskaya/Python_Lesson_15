# Напишите функцию, которая принимает количество дней от текущей даты и
# возвращает дату, которая наступит через указанное количество дней. Дополнительно,
# выведите эту дату в формате YYYY-MM-DD.

from datetime import datetime, timedelta


def day_after(days):
    current_date = datetime.now()
    delta = timedelta(days)
    new_date = current_date + delta
    formatted_new_date = new_date.strftime('%Y-%m-%d')
    return formatted_new_date


if __name__ == '__main__':
    print(day_after(2))