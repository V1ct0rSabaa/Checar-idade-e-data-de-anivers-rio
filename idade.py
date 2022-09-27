import datetime

ano_atual = datetime.datetime.now().year

def input_do_ano() -> int:
    entrada_certa: bool = False
    while not entrada_certa:
        texto_digitado = input("Em que ano você nasceu: ")
        try:
            ano_digitado = int(texto_digitado)
            if ano_digitado > ano_atual:
                print("Data inválida, você não deve digitar uma data no futuro")
            elif ano_digitado < 1:
                print("Data inválida, não existe ano zero ou negativo")
            else:
                entrada_certa = True
                return ano_digitado
        except ValueError:
            print("Entrada errada")



def mostrar_idade() -> str:
    ano_digitado = input_do_ano()
    global ano_atual
    anos_idade = f"Você tem {ano_atual - ano_digitado} anos"
    return anos_idade


