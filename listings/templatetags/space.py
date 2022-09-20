from django import template
from django.utils import numberformat
register = template.Library()



def spaced_format(value):
    deleni = value / 1000
    zbytek = value % 1000
    str_deleni = str(deleni)
    str_zbytek = str(zbytek)
    if zbytek == 0:
        
        if value > 10000:
            res = str_deleni.replace("."," ") + "00"
            return res
        if value < 10000:
            res = str_deleni.replace("."," ") + "00"
            return res
    else:
        if value > 9999:
            str_deleni_1 = (str_deleni[:-1])
            hodnota = str_deleni_1.replace("."," ") + str_zbytek
            hodnota_without_dot = (hodnota[:-2])
            return hodnota_without_dot
        if value < 10000:
            str_deleni_1 = (str_deleni[:-2])
            hodnota = str_deleni_1+ " " + str_zbytek
            hodnota_bez_dot = hodnota.replace(".", " ")
            hodnota_without_dot = (hodnota_bez_dot[:-2])
            return hodnota_without_dot

register.filter("spaced_format",spaced_format)

