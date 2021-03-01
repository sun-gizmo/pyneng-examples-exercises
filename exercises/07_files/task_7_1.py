!# /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
#Решение

with open('ospf.txt', 'r') as f:
    ospf = f.readlines()
    for lines in ospf:
        lines = lines.strip().split()
        protocol = lines[0].replace('O', 'OSPF')
        prefix = lines[1]
        metric = lines[2].strip('[]')
        hop = lines[4].rstrip(',')
        update = lines[5].rstrip(',')
        interface = lines[6]
        ospf_route = '''
        Protocol              {}
        Prefix                {}
        AD/Metric             {}
        Next-Hop              {}
        Last update           {}
        Outbound Interface    {}
        '''
        print(ospf_route.format(protocol,prefix,metric,hop,update,interface))
