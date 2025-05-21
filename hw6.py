def ComputePowerOfTen(n):
    if n == 0:
        return 1
    elif n == 1:
        return 10
    else:
        half_power = ComputePowerOfTen(n // 2)
        if n % 2 == 0:
            return half_power * half_power
        else:
            return 10 * half_power * half_power


def DecimalToBinary(decimal):
    if decimal == 0:
        return "0"
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary