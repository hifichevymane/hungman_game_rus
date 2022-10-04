from random import *

word_list = ['КЛЮЧ', 'КНИГА', 'ЕНОТ', 'МАШИНКА', 'КОРОВА', 'ТЕЛЕЖКА', 'ШЛЕМ', 'КНОПКА', 'ШНУР', 'ЧЕРНЫЙ',
             'ВЛАСТЕЛИН', 'СКАЙП', 'ДУБ', 'ЧАСЫ', 'ТРУБА', 'ЕЛКА', 'ИНСТИТУТ', 'КОРОБКА', 'ТАБЛИЧКА', 'ВОДА',
             'СКОВОРОДА',
             'МНОГОНОЖКА', 'ЕВРЕЙ', 'ТЕРМИТ', 'КАЧЕК', 'РУЛОН', 'МАГНИТОФОН', 'НОГА', 'СЛОН', 'МИКРОВОЛНОВКА', 'ТОРТ',
             'МАК',
             'ДЫМ', 'ЧАЙКА', 'ВАЛЕТ', 'ПЛИНТУС', 'ШАПКА', 'ДИНОЗАВР', 'ТОРШЕР', 'БАЛАЛАЙКА', 'БАНКА', 'ЯХТА', 'ОВЦА',
             'БАНАН',
             'ДУБ', 'АНИМЕ', 'РАДУГА', 'БУКВА', 'ВЕЛОСИПЕД', 'БАНДЖО', 'ГОЛУБЬ', 'ВИНТОВКА', 'КУБОК', 'ЖАСМИН',
             'ТЕЛЕФОН',
             'АНДРОИД', 'ГОРА', 'ХАЛАТ', 'ЖЕТОН', 'ОБОД', 'МЫЛО', 'ЙОГ', 'ШИШКА', 'ДОЛЛАР', 'КОЛОНКА', 'КУБИК', 'ОМАР',
             'РАКЕТА', 'МОРКОВКА', 'ЗЕРКАЛО', 'МОЛОТ', 'ВОЗДУХ', 'ЗМЕЙ', 'ЁЖ', 'ПАЛЬМА', 'МАСЛО', 'ДИДЖЕЙ', 'МЕШОК',
             'ТЮБИК',
             'МОЗГ', 'ПОЕЗД', 'РОЗЕТКА', 'ПАРАШЮТИСТ', 'БЕЛКА', 'ШПРОТЫ', 'САМОСВАЛ', 'ПАЗЛ', 'БУТЫЛКА', 'КРЕМЛЬ',
             'ПИЦЦА',
             'МАКАРОНЫ', 'КОВЕР', 'ЗУБЫ', 'ЯРЛЫК', 'КАШАЛОТ', 'МАРС', 'ШАКАЛ', 'ПОМАДА', 'ДЖИП', 'ЛЕЩ', 'КАМЕНЬ',
             'ДИСК']


def get_word():
    chosen_word = choice(word_list)
    return chosen_word


def display_hungman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     /|\\
           |      |
           |      |         
           |     / \\   
           -    
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/              
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/           
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|            
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O         
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |                
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |                
           |     
           -
        '''
    ]

    return stages[tries]


def play(chosen_word):
    word_completion = '_' * len(chosen_word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    arr = list(word_completion)
    tries = 6

    print('Давайте играть в угадайку слов!')
    print(display_hungman(tries))
    print(word_completion)

    while True:
        ans = str(input('Введите букву: ')).upper()

        if len(ans) > 1 or ans.isalpha() == False:
            print('Вы ввели неправильные данные! Попробуйте ещё раз')
            continue

        else:
            if ans in chosen_word:

                if ans not in guessed_letters:
                    guessed_letters.append(ans)
                    print('Вы отгадали букву !')

                    for i in range(len(word_completion)):
                        if chosen_word[i] == ans:
                            arr[i] = ans
                    if ''.join(arr) == chosen_word:
                        guessed = True

                else:
                    print('Буква уже вводилась')
                    continue

            else:
                tries -= 1
                print(f'Вы не отгадали букву. У вас осталось {tries} попыток')

        if guessed:
            print('Вы выиграли!')
            print(f"Это было слово - {chosen_word}")
            break

        if tries == 0:
            print('Вы проиграли!')
            print(f"Правильное слово - {chosen_word}")
            break

        print(display_hungman(tries))
        print(''.join(arr))


while True:
    play(get_word())
    ans2 = str(input('Хотите ли вы ещё сыграть?(да/нет): ')).lower()
    if ans2 == 'да':
        continue
    else:
        break