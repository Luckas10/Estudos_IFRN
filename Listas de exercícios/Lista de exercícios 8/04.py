# 4) Faça uma função que recebe como parâmetro uma data (no formato DD/MM) e informa a data por extenso. Em seguida 
# crie uma função principal que ao ser executada pelo programa solicita uma data ao usuário e informa o retorno da 
# função (ex: Usuário digita 15/06 e o programa informa: QUINZE DE JUNHO).

def data_por_extenso(data):
    meses = {
        '01': 'JANEIRO',
        '02': 'FEVEREIRO',
        '03': 'MARÇO',
        '04': 'ABRIL',
        '05': 'MAIO',
        '06': 'JUNHO',
        '07': 'JULHO',
        '08': 'AGOSTO',
        '09': 'SETEMBRO',
        '10': 'OUTUBRO',
        '11': 'NOVEMBRO',
        '12': 'DEZEMBRO'
    }

    numeros = [
        "UM", 
        "DOIS", 
        "TRÊS", 
        "QUATRO", 
        "CINCO", 
        "SEIS", 
        "SETE", 
        "OITO", 
        "NOVE"
    ]

    dia, mes = data.split('/')
    dia_por_extenso = ''

    if dia.startswith('0'):
        dia = dia[1:]

    if dia == '10':
        dia_por_extenso = 'DEZ'

    elif dia == '11':
        dia_por_extenso = 'ONZE'

    elif dia == '12':
        dia_por_extenso = 'DOZE'

    elif dia == '13':
        dia_por_extenso = 'TREZE'

    elif dia == '14':
        dia_por_extenso = 'QUATORZE'

    elif dia == '15':
        dia_por_extenso = 'QUINZE'

    elif dia == '16':
        dia_por_extenso = 'DEZESSEIS'

    elif dia == '17':
        dia_por_extenso = 'DEZESSETE'

    elif dia == '18':
        dia_por_extenso = 'DEZOITO'
        
    elif dia == '19':
        dia_por_extenso = 'DEZENOVE'

    elif dia.startswith('2'):
        if dia != '20':
            dia_por_extenso = 'VINTE E ' + numeros[int(dia[1]) - 1]
        else:
            dia_por_extenso = 'VINTE'

    elif dia.startswith('3'):
        if dia != '30':
            dia_por_extenso = 'TRINTA E ' + numeros[int(dia[1]) - 1]
        else:
            dia_por_extenso = 'TRINTA'

    else:
        dia_por_extenso = 'ZERO' if dia == '0' else 'NÃO IMPLEMENTADO'

    mes_por_extenso = meses[mes]

    return dia_por_extenso + ' DE ' + mes_por_extenso


def main():
    print("=== ESCRITOR DE DATA POR EXTENSO ===")
    data = input("Digite uma data (DD/MM): ")
    data_extenso = data_por_extenso(data)
    print("Data por extenso:", data_extenso)


if __name__ == '__main__':
    main()
