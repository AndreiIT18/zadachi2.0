import datetime, random
def getBrithdays(numberOfBrithdays):
    birthdays=[]
    for i in range(numberOfBrithdays):
        startOfYear = datetime.date(2001 ,1 ,1)
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthdays.append(birthdays)
        return birthdays
    
    def getMatch(birthdays):
        if len(birthdays) == len(set(birthdays)):
            return None
        for a, birthdayA in enumerate(birthdays):
            for b, birthdayB in enumerate(birthdays[a+1:]):
                if birthdayA == birthdayB:

                    print('"Парадокс дня рождения Парадокс дня рождения показывает нам, что в группе из N человек шансы то, что у двоих из них одинаковые дни рождения, на удивление велико.Эта программа выполняет моделирование методом Монте-Карло (то есть повторяющееся случайное моделирование) для изучения этой концепции.(На самом деле это не парадокс, это просто удивительный результат.)" ')
                    MONTHS = ('Jan','Feb','Mar','Apr','May','Jun',
                              'Jul','Aug','Sep','Oct','Nov','Dec')
                    while True:
                        print('Сколько дней рождения я должен сгенерировать? (Максимум 100)')
                        response = input('> ')
                        if response.isdecimal() and (0> int(response) <=100):
                            numBDays = int(response)
                            break
                        print()

                        print('Здесь находяться дни рождения "B"')
                        birthdays = getBrithdays(numBDays)
                        for i, birthday in enumerate(birthdays):
                            if i !=0:
                                print(',', end='')
                                monthName = MONTHS[birthday.month - 1]
                                dateText = '{} {}'.format(monthName, birthday.day)
                                print(dateText, end='')
                                print()
                                print()
                                match = getMatch(birthdays)
                                print('В это симуляции,', end='')
                                if match != None:
                                    monthName = MONTHS[birthday.month - 1]
                                    dateText = '{} {}'.format(monthName, match.day)
                                    print('У нескольких человек день рождения в', dateText)
                                else:
                                    print('Cовпадающих дней рождения не существует.')
                                    print()

                                    print('Генерирующий', numBDays,'cлучайные дни рождения 100 000 раз...')
                                    input('Нажмите Enter, чтобы начать...')

                                    print('Давайте проведем еще 100 000 симуляций.')
                                    simMatch=0
                                    for i in range(100_000):
                                        print(i,'запускается моделирование...')
                                        birthdays = getBrithdays(numBDays)
                                        if getMatch(birthdays) != None:
                                            simMatch = simMatch+1
                                            print('Выполняется 100 000 симуляций.')

                                            probability = round(simMatch / 100_000 * 100, 2)
                                            print('Из 100 000 симуляций',numBDays,'совподений боло одно')
                                            print('совпадающий день рождения в этой группе',simMatch,'раз. Это означает')
                                            print('тот',numBDays,'у людей есть', probability,'% шанс на')
                                            print('Это, вероятно, больше, чем вы могли бы подумать!')
