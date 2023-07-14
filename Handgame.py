import random

words_list = ["автомобиль","карта","ключ","дед","газета","молоко","колбаса","шкаф","самолёт","огурец"]
alphabet = "А Б В Г Д Е Ё Ж З И Й К \n Л М Н О П Р С Т У Ф Х \n  Ц Ч Ш Щ Ъ Ы Ь Э Ю Я"

def give_word():
    current_word = random.choice(words_list).upper()
    return current_word

def start_game(word, alphabet):

    word_letters = []

    line = list("_"*len(word))
    print('  '.join(line))
    print(alphabet)
    
    tries = 6

    while True:
        letter = input().upper()
        if letter in word and len(letter) == 1:
            print(display_hangman(tries))

            if  word_letters.count(letter) > 1:
                for item in range(len(word_letters)):
                    if word_letters[item] == letter:
                        line[item] = letter
            else:
                line[word_letters.index(letter)] = letter
            alphabet = alphabet.replace(letter, "")
            print(alphabet)
            print(' '.join(line))

            if "_" not in line:
                print("Вы выиграли!")
                print("Хотите сыграть ещё? ДА/НЕТ (любой другой ввод будет считаться за 'НЕТ')")
                answer = input().upper()
                if answer == 'ДА':
                    return True     #start_game(give_word()) не хочу приходить к рекурсии поэтому такой костыль
                else:
                    return False
        else:
            tries -= 1
            if tries < 0:
                print("Вы проиграли! Слово -", word)
                print("Хотите сыграть ещё? ДА/НЕТ (любой другой ввод будет считаться за 'НЕТ')")
                answer = input().upper()
                if answer == 'ДА':
                    return True
                    
                else:
                    return False   
            print(display_hangman(tries))
            print(' '.join(line))
            print(alphabet)
                       
                    
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \\
                   -
                ''',
                
                '''
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                ''',
                
                '''
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                ''',
               
                '''
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                ''',
                
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                
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

print("Добро пожаловать, любители игр! Это - HandGame. Отгадайте слово и спасите человечка.")
while start_game(give_word(), alphabet):
    continue