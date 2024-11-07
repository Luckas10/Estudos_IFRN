from models.cpf import Cpf
from models.identidade import Identidade

if __name__ == '__main__':
    cpf = Cpf('José', 50982436721)
    rg = Identidade('Maria', 883774551)


    print('-' * 15)
    print(cpf)
    print(cpf.__dict__)
    print('-' * 15)
    print(cpf)
    print(cpf.__dict__)