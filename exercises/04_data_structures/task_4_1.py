# -*- coding: utf-8 -*-
"""
Задание 4.1

Используя подготовленную строку nat, получить новую строку, в которой
в имени интерфейса вместо FastEthernet написано GigabitEthernet.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"

nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"                    

print(nat.replace('Fast', 'Giga'))                                                         
ip nat inside source list ACL interface GigaEthernet0/1 overload 
