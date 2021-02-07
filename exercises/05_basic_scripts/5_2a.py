#! usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28  в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
network = input('Введите IP-сети в формате 10.1.1.0/24: ')
ip = network[:network.find('/')]
ip = ip.split('.')
oktet1 = bin(int(ip[0]))
oktet2 = bin(int(ip[1]))
oktet3 = bin(int(ip[2]))
oktet4 = bin(int(ip[3]))


oktet1 = oktet1[2::]
oktet2 = oktet2[2::]
oktet3 = oktet3[2::]
oktet4 = oktet4[2::]

bin_oktet1 = "{:>08}".format(oktet1)
bin_oktet2 = "{:>08}".format(oktet2)
bin_oktet3 = "{:>08}".format(oktet3)
bin_oktet4 = "{:>08}".format(oktet4)

bin_ip = (bin_oktet1+bin_oktet2+bin_oktet3+bin_oktet4)

mask = network[network.find('/')::]
mask = int(mask.lstrip('/'))
maskbin = "1" * mask
maskbin = "{:<032}".format(maskbin)

net = bin_ip[:mask]
Network = "{:<032}".format(net)

noktet1 = int(Network[0:8], 2)
noktet2 = int(Network[8:16], 2)
noktet3 = int(Network[16:24], 2)
noktet4 = int(Network[24:32], 2)

ip_template = """
Network
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
"""

print(ip_template.format(noktet1,noktet2,noktet3,noktet4))

moktet1 = int(maskbin[0:8], 2)
moktet2 = int(maskbin[8:16], 2)
moktet3 = int(maskbin[16:24], 2)
moktet4 = int(maskbin[24:32], 2)


mask_template = '''
/{4:<}
{0:<8} {1:<8} {2:<8} {3:<8}
{0:<08b} {1:<08b} {2:<08b} {3:<08b}
'''

print(mask_template.format(moktet1,moktet2,moktet3,moktet4,mask))
