def convert10tobase(num, base):
    newNum = ''
    while num > 0:
        newNum = str(num % base) + newNum
        num //= base
    return int(newNum)