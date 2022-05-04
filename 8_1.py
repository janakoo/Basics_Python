class MyData:
    def __init__(self, mycalendar):
        self.mycalendar = mycalendar

    @classmethod
    def m_metod(cls, mycalendar):
        my_calendar = list(map(int, mycalendar.split('-')))

        return  (f'Date {my_calendar[0]}-{my_calendar[1]}-{my_calendar[2]}')

    @staticmethod
    def is_valid_date(year, month, day):
        day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            day_count_for_month[2] = 29
        return (1 <= month <= 12 and 1 <= day <= day_count_for_month[month])

while True:
    input_data = input("введите дату дд-мм-гггг :")
    try:
        mycalendar = list(map(int, input_data.split('-')))

    except ValueError:
        print("Введите дату")
    else:
        print(mycalendar)
        break

my_str = '22-04-2022'
today = MyData.m_metod(my_str)
print(today)
print(mycalendar)

today = MyData.m_metod(input_data)
print(today)
