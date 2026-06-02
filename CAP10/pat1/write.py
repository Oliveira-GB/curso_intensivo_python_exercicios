from pathlib import Path

path = Path("programming.txt")
path.write_text("EITA LELE VAMOS VER")
path.write_text("EITA LELE VAMOS VER222")

print(path.read_text())
