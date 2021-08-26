from teste import Conta

if __name__ == '__main__':

    banco = list()

    while True:
        conta = Conta(input('Titular'))
        banco.append(conta)

        resp = input("Deseja continuar? [S/N]")
        if resp == "N":
            break

    banco[1].depositar(50)
    banco[1].sacar(100)

    for o in banco:
        print(o)