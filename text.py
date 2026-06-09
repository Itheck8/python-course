try:
    number = int(input('введи хуйню'))
    print(100/number)
except ValueError:
    print('хуйня')
except ZeroDivisionError:
    print('еблан на ноль делишь')