#binary = input("Въведи двоично число: ")
#decimal = int(binary, 2)
#print("Десетичното число е:", decimal)

def convert(number, from_base, to_base):
    decimal = int(number, from_base)

    if to_base == 2:
        return bin(decimal)[2:]
    elif to_base == 8:
        return oct(decimal)[2:]
    elif to_base == 10:
        return str(decimal)
    elif to_base == 16:
        return hex(decimal)[2:].upper()


number = input("Число: ")
from_base = int(input("От : "))
to_base = int(input("Към : "))

print("Резултат:", convert(number, from_base, to_base))