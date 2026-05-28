convidados = ["Bob Marley", "Pessoa numero 2", "Pessoa numero 3"]

convidado_new_one = convidados.insert(0, "Larissa oliveira")
convidado_new_two = convidados.insert(1, "Vaneli")
convidado_new_three = convidados.append("Sei quem mais não")

message = f"Rapido e ligeiro nem precisa pensar para esses exercicios {convidados[0]}"
print(message)
message = f"Rapido e ligeiro nem precisa pensar para esses exercicios {convidados[1]}"
print(message)
message = f"Rapido e ligeiro nem precisa pensar para esses exercicios {convidados[-1]}"
print(message)


