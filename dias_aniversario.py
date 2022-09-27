# recebe input de dia, mês e ano, checa com a data atual e diz quantos dias faltam
import datetime
from idade import mostrar_idade

obj_data = datetime.datetime.now()
data_atual: tuple[int] = (obj_data.day, obj_data.month)

def entrada_dados_dia() -> int:
    entrada_certa: bool = False
    while not entrada_certa:
        entrada_dia = input("Em que dia você nasceu: ")
        try:
            dia = int(entrada_dia)
            if dia > 30:
                print("Data inválida, não existe mês com mais de 30 dias")
            elif dia < 1:
                print("Data inválida, não existe dia zero ou negativo")
            else:
                entrada_certa = True
                return dia
        except ValueError:
            print("Entrada errada, digite apenas números inteiros e positivos")


def entrada_dados_mes() -> int:
    entrada_certa: bool = False
    while not entrada_certa:
        entrada_mes = input("Em que mês você nasceu: ")
        try:
            mes = int(entrada_mes)
            if mes > 12:
                print("Data inválida, existem apenas 12 meses")
            elif mes < 1:
                print("Data inválida, não existe mês zero ou negativo")
            else:
                entrada_certa = True
                return mes
        except ValueError:
            print("Entrada errada, digite apenas números inteiros e positivos")
            

def mostrar_data_aniversario():
    texto: str = ""
    dia_digitado = entrada_dados_dia()
    mes_digitado = entrada_dados_mes()
    if dia_digitado == data_atual[0] and mes_digitado == data_atual[1]:
        texto = "Parabéns, hoje é seu aniversário."
    else:
       meses_faltando = 0
       dias_faltando = 0
       if mes_digitado > data_atual[1]:
            meses_faltando += mes_digitado - data_atual[1]
       if mes_digitado < data_atual[1]:
            meses_faltando = data_atual[1] - mes_digitado
       if dia_digitado < data_atual[0]:
           dias_faltando += data_atual[0] - dia_digitado
       if dia_digitado > data_atual[0]:
           dias_faltando = dia_digitado - data_atual[0]
           meses_faltando += 1
       texto = f"faltam {dias_faltando} dias e {meses_faltando} meses para o seu aniversário."
    return texto

if __name__ == "__main__":
    print(f"Você tem {mostrar_idade()} anos de idade e {mostrar_data_aniversario()}")