import os


class cmd:
    def __init__(self, str='', w=[], wl=['-']):
        self.str = str
        self.w = w
        self.wl = wl

    def Errors(self):
        if len(self.str) != 1:
            print('\u001b[1m\033[31mSize Error:\u001b[0m\033[29m  Длинна передаваемого значения должна быть =1\n',)
            return False
        if not self.str.isalpha():
            print('\u001b[1m\033[31mType Error:\u001b[0m\033[29m  Передаваемое значение должно буквой\n')
            return False
        if not ('А' <= self.str <= 'Я') and not ('а' <= self.str <= 'я') and self.str != 'Ё' and self.str != 'ё':
            print('\u001b[1m\033[31mLanguage Error:\u001b[0m\033[29m  Передаваемое значение должно быть буквой из кириллицы\n')
            return False
        if self.str in self.w:
            print('\u001b[1m\033[31mRetry Error:\u001b[0m\033[29m  Передаваемое значение уже было передано\n')
            return False
        return True

    def Commands(self):
        if self.str == '/rs':
            return False
        elif self.str == '/wl':
            print(*self.wl)
            return True
        elif self.str == '/lsw':
            print(self.wl[-1])
            return True
        elif self.str == '/ex':
            os.abort()
        else:
            print('\u001b[1m\033[31mCommand Error:\u001b[0m\033[29m  Команда не существует\n')
            return True


pic = [
    """





 ━━━━━━━━━━━━━
""",
    """
   ┃
   ┃
   ┃
   ┃
   ┃
 ━━┻━━━━━━━━━━
""",
    """
   ┏━━━━━━━
   ┃
   ┃
   ┃
   ┃
 ━━┻━━━━━━━━━━
""",
    """
   ┏━━━━━━┓
   ┃
   ┃
   ┃
   ┃
 ━━┻━━━━━━━━━━
""",
    """
   ┏━━━━━━┓
   ┃      ⬤
   ┃
   ┃
   ┃
 ━━┻━━━━━━━━━━
""",
    """
   ┏━━━━━━┓
   ┃      ⬤
   ┃      ┃
   ┃
   ┃
 ━━┻━━━━━━━━━━
""",
    """
   ┏━━━━━━┓
   ┃      ⬤
   ┃     ┏┫
   ┃
   ┃
 ━━┻━━━━━━━━━━
""",
    """
   ┏━━━━━━┓
   ┃      ⬤
   ┃     ┏╋┓
   ┃
   ┃
 ━━┻━━━━━━━━━━
""",
    """
   ┏━━━━━━┓
   ┃      ⬤
   ┃     ┏╋┓
   ┃     ┏┛
   ┃
 ━━┻━━━━━━━━━━
""",
    """
   ┏━━━━━━┓
   ┃      ⬤
   ┃     ┏╋┓
   ┃     ┏┻┓
   ┃
 ━━┻━━━━━━━━━━
"""]