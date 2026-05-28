convidados = ["Bob Marley", "Pessoa numero 2", "Pessoa numero 3"]

convidado_out = convidados.pop()
message = f"Adeus vlws flws {convidado_out}"
print(message)

del convidados[-1]
print(convidados)