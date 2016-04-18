def valida_entrada(palindrome):
    if not palindrome:
        return False
    palindrome = list(palindrome)
    algarismos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in palindrome:
        if not i in algarismos:
            return False
            break
    return True


def encontra_palindromo_mais_proximo(palindrome):
    palindrome = list(palindrome)
    size_list = len(palindrome)
    mid_llist = int(len(palindrome) / 2)
    for i in range(mid_llist):
        palindrome[size_list - i - 1] = palindrome[i]

    return (''.join(palindrome))


def proximo_palindrome_simples(palindrome):
    palindrome = list(palindrome)
    mid_list = int(len(palindrome) / 2)
    palindrome[mid_list] = str(int(palindrome[mid_list]) + 1)
    palindrome[len(palindrome) - mid_list - 1] = palindrome[mid_list]
    return (''.join(palindrome))


def proximo_palindrome_composto(palindrome):
    palindrome = list(palindrome)
    palindrome[0:0] = '1'
    palindrome[-1] = '1'
    return ''.join(palindrome)


def proximo_palindrome(palindrome):
    palindrome = list(palindrome)
    size_list = len(palindrome)
    flag = int((size_list - 1) / 2)
    while palindrome[flag] == '0':
        flag = flag - 1

    palindrome[flag] = str(int(palindrome[flag]) + 1)
    palindrome[size_list - flag - 1] = palindrome[flag]
    return (''.join(palindrome))


def zerar_palindrome(palindrome):
    palindrome = list(palindrome)
    size_list = len(palindrome)
    flag = int((len(palindrome) - 1) / 2)
    while (flag >= 0) & (palindrome[flag] == '9'):
        palindrome[flag] = '0'
        palindrome[size_list - flag - 1] = '0'
        flag = flag - 1

    return (''.join(palindrome))

if __name__ == "__main__":
    numeroTestes = int(input())
    for i in range(numeroTestes):
        palindrome = input()
        if not valida_entrada(palindrome):
            print('Entrada nao valida')
            continue

        palindrome = list(palindrome)
        size_list = len(palindrome)
        mid_list = int(len(palindrome) / 2)
        temp = palindrome
        palindrome = encontra_palindromo_mais_proximo(palindrome)
        if palindrome > (''.join(temp)):
            print(''.join(palindrome))

        elif temp[mid_list] != '9':
            palindrome = proximo_palindrome_simples(palindrome)
            print(palindrome)

        else:
            palindrome = zerar_palindrome(palindrome)
            flag = -1
            for j in palindrome:
                if j != '0':
                    flag = 0
                    break

            if flag >= 0:
                palindrome = proximo_palindrome(palindrome)
                print(palindrome)

            else:
                palindrome = proximo_palindrome_composto(palindrome)
                print(palindrome)
