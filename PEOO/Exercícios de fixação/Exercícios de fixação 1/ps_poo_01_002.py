import os
from eletrodomesticos_v2 import Televisao

def main():
    tv_interativa = Televisao()
    while True:
        estado = tv_interativa.estado()
        print(f'TV Interativa | Canal: {tv_interativa.canal} | {estado}')
        tv_interativa.menu()
        tv_interativa.opcao(int(input()))
        os.system('clear')

if __name__ == '__main__':
    main()
    