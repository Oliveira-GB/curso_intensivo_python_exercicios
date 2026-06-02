from pathlib import Path

path = Path("book.txt")
conteudo = ""

print("Livro de convidados")
continuar = int(input("Digite 1 para colocar um nome novo ou 2 para criar o arquivo\n"))

while continuar == 1:
    nome = input("Digite um nome")
    conteudo += f"{nome}\n"
    continuar = int(input("Digite 1 para colocar um nome novo ou 2 para criar o arquivo\n"))

path.write_text(conteudo)

teste = path.read_text()
print(teste)