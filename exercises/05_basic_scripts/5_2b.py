#! usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
import sys


network = sys.argv[1]
ip = network[:network.find('/')]
ip = ip.split('.')
oktet1 = int(ip[0])
oktet2 = int(ip[1])
oktet3 = int(ip[2])
oktet4 = int(ip[3])

ip_template = """
Network
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
"""
print(ip_template.format(oktet1,oktet2,oktet3,oktet4))


mask = network[network.find('/')::]
mask = int(mask.lstrip('/'))
maskbin = "1" * mask
maskbin = "{:<032}".format(maskbin)

moktet1 = int(maskbin[0:8], 2)
moktet2 = int(maskbin[9:16], 2)
moktet3 = int(maskbin[17:24], 2)
moktet4 = int(maskbin[25:32], 2)

mask_template = '''
/{4:<}
{0:<8} {1:<8} {2:<8} {3:<8}
{0:<08b} {1:<08b} {2:<08b} {3:<08b}
'''

moktet1 = int(maskbin[0:8], 2)
moktet2 = int(maskbin[8:16], 2)
moktet3 = int(maskbin[16:24], 2)
moktet4 = int(maskbin[24:32], 2)

print(mask_template.format(moktet1,moktet2,moktet3,moktet4,mask))
