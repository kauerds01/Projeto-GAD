# Bloco de Dados da empresa
empresa = {
    "nome": "GAD Tecnologia Agrícola",
    "proprietarios": "Donos: Bruno, Kauê, Gabi.",
    "cnpj": "12.345.678/0001-90",
    "setor": "Tecnologia e Agricultura",
    "atividade": "Gestão agrícola com drones",
    "cidade": "São Paulo",
    "estado": "SP",
    "ano_fundacao": 2026,
}

# bloco de matriz 2d - Aluno 2
plantacao = [
    ["saudável", "saudável", "seco", "seco"],
    ["saudável", "saudável", "seco", "saudável"],
    ["saudável", "seco", "saudável", "seco"],
    ["saudável", "saudável", "seco", "seco"],
]


def iniciar():
    print("programa GAD iniciado")


def ver_plantacao():
    print("plantacao verificada")


def ver_insumos():
    print("insumos verificados")


def ver_drones():
    print("drones verificados")


def encerrar():
    print("saindo do programa")


# --tela inicial--
def menu():
    print("===GAD===")
    print("[1] iniciar")
    print("[2] ver plantaçao")
    print("[3] ver insumos")
    print("[4] ver drones")
    print("[5] encerrar")


while True:
    menu()

    opcao = input("selecione uma opcao: ").strip()

    if opcao == "1":
        iniciar()
    elif opcao == "2":
        ver_plantacao()
    elif opcao == "3":
        ver_insumos()
    elif opcao == "4":
        ver_drones()
    elif opcao == "5":
        encerrar()
        break
    else:
        print("Opção inválida")
with open("arquivo.csv", "r", encoding="utf-8") as arquivo:
    linha = arquivo.readline()

    while linha:
        print(linha, end="")
        linha = arquivo.readline()