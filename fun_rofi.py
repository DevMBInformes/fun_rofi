#!/bin/python

import os


#datos = os.system("ls /mnt/alter/code/")
#print(datos)

#os.system(f"{datos} | rofi -show -dmenu")
import subprocess


def conver_list(data:list)->bytes:
    options_str_list = [str(dat) for dat in data]
    options_str = "\n".join(options_str_list)
    output = options_str.encode('utf-8')
    return output


def get_value_string(output:bytes)->str:
    result = subprocess.run(['rofi', '-dmenu'], input=output, stdout=subprocess.PIPE)
    result = result.stdout.decode('utf-8')
    return result[:-1]



output = conver_list([1,2,3,4,5,6,7])
result = get_value_string(output)
print(f"el resultado es {result}")


