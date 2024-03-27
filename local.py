radianes = False
def fac(n): 
    if n >= 1000000000000:
        return "El número es demasiado grande"
    try:
        text = str(n) + ' = '
        for i in range(2, int(n**0.5) + 1):
            while n % i == 0:
                n //= i
                counter = 1
                while n % i == 0:
                    n //= i
                    counter += 1
                text += str(i)
                if counter > 1:
                    text += '^' + str(counter)
                text += ' × '
        if n > 1:
            text += str(n)
        else:
            text = text[:-3]  # Elimina el último ' × '
        return text
    except Exception as e:
        print(e)
        return str(e)
