rios = {"Brasil":"Rio 1", "China":"RIO 2", "Tailandia":"Rio 3"}

for key, value in rios.items():
    print(f"Local {key} - nome {value}")

for key in rios:
    print(f"Local {key}")

for value in rios.values():
    print(f"nome {value}")
