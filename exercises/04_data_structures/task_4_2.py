# -*- coding: utf-8 -*-
"""
Задание 4.2

Преобразовать строку mac из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

mac = "AAAA:BBBB:CCCC"

### первый вариант решения
print(mac.replace(":","."))                                                                 
AAAA.BBBB.CCCC

### второй вариант решения
mac1 = mac.split(":")                                                                       

print(".".join(mac1))                                                                       
AAAA.BBBB.CCCC

### второй вариант в одну строку
print(".".join(mac.split(":")))                                                             
AAAA.BBBB.CCCC

