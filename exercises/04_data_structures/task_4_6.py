# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0

###Решение
ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"                                                                                                                                           

ospf = ospf_route.split()                                                                                                                                                                                                  

prefix = ospf[1]                                                                                                                                                                                                           
ad = ospf[2]                                                                                                                                                                                                               
hop = ospf[3]                                                                                                                                                                                                              
prefix = ospf[0]                                                                                                                                                                                                           
ad = ospf[1]                                                                                                                                                                                                               
update = ospf[4]                                                                                                                                                                                                           
inter = ospf[5]                                                                                                                                                                                                            

ad = ad.strip('[]')                                                                                                                                                                                                        
hop = hop.rstrip(',')                                                                                                                                                                                                      
update = update.rstrip(',')                                                                                                                                                                                                

ospf_router = ''' 
    ...: Prefix                {0:18} 
    ...: AD/Metric             {1:18} 
    ...: Next-Hop              {2:18} 
    ...: Last update           {3:18} 
    ...: Outbound Interface    {4:18} 
    ...: '''                                                                                                                                                                                                                        
                                                                                                                                                                         
ospf_router.format(prefix,ad,hop,update,inter)                                                                                                                                                                             

print(ospf_router.format(prefix,ad,hop,update,inter))                                                                                                                                                                      

Prefix                10.0.24.0/24      
AD/Metric             110/41            
Next-Hop              10.0.13.3         
Last update           3d18h             
Outbound Interface    FastEthernet0/0
