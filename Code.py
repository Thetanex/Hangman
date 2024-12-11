# Библиотеки
import sqlite3 as l3
import random as rnd
import os
# Прочие файлы: графика и тп
import add


# Получение случайного значения из БД
def get_rand_word(lst):
    return lst[rnd.randint(1, 65499)][1]


def main():
    os.system('cls' if os.name == 'nt' else 'clear')  # Очистка консоли
    print("\u001b[1m" + '=' * 45 + "\u001b[0m")
    sqlite_connection = l3.connect('db/data.sqlite')  # Работа с БД
    cursor = sqlite_connection.cursor()
    cursor.execute("SELECT * from nouns")
    word_lst = cursor.fetchall()  # WordList
    cursor.close()

    wl =[]
    # Основной цикл игры
    while True:
        cnt = 0
        wlst = get_rand_word(word_lst)
        out_lst = ['_' for _ in range(len(wlst))]
        w = []
        wl.append(wlst)

        # Цикл угадывания слова
        while cnt != len(add.pic):
            if cnt != 0:
                print(add.pic[(cnt - 1) % len(add.pic)])
            if w:
                print('Данное значения:', *w)
            print("  \u001b[1mПрогресс отгадывания:\u001b[0m ", *out_lst, sep='')
            inp = input('  \u001b[1mВведите предполагаемую букву: \u001b[0m')
            os.system('cls' if os.name == 'nt' else 'clear')  # Очистка консоли
            print("\u001b[1m" + '=' * 45 + "\u001b[0m")
            print("\u001b[1mВведеная буква:\u001b[0m", inp + '\n')
            if add.cmd(inp, w).Errors():
                inp = inp.lower()
                w.append(inp)
                if wlst.find(inp) == -1:
                    cnt += 1
                elif wlst.find(inp) != -1:
                    for i in range(len(out_lst)):
                        if wlst[i] == inp:
                            out_lst[i] = inp
                if '_' not in out_lst:
                    cnt = len(add.pic)
        if '_' not in out_lst:
            print('\u001b[1m\033[32m     Вы Выиграли\u001b[0m\033[29m\n')
        else:
            print('\u001b[1m\033[33m     Вы Проиграли\u001b[0m\033[29m\n')
        print('   \u001b[1mНачать новую игру?\u001b[0m')
        inp = input('  \u001b[1mВведите команду: \u001b[0m')
        while add.cmd(inp, w, wl).Commands():
            inp = input('  \u001b[1mВведите команду: \u001b[0m')
        os.system('cls' if os.name == 'nt' else 'clear')  # Очистка консоли
        print("\u001b[1m" + '=' * 45 + "\u001b[0m")


if __name__ == "__main__":
    main()
