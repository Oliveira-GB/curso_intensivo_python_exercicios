def make_album(nome_album, nome_artista):
    dic_musica = {f"Album":nome_album, "artista":nome_artista}
    return dic_musica

print(f"Aqui {make_album("album1", "artista1")}")
print(f"Aqui {make_album("album2", "artista2")}")
print(f"Aqui {make_album("album3", "artista3")}")