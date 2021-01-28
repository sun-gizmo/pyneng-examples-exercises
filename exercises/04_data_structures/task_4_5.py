# -*- coding: utf-8 -*-
"""
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2 (пересечение).

Результатом должен быть такой список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

###Решение
                                   
In [17]: command1 = command1.split()[-1].split(',')                                                  

In [18]: command2 = command2.split()[-1].split(',')                                                  

In [19]: set1 = set(command1)                                                                        

In [20]: set2 = set(command2)                                                                        

In [21]: setall = set1.intersection(set2)                                                            

In [22]: vlans = list(setall)                                                                        

In [23]: print(vlans)                                                                                
['1', '3', '8']

