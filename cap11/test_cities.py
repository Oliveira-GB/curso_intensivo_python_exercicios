from cities import *

def test_cities_country():
    cities_formatted = cities_country("São Paulo", "Brasil")
    assert cities_formatted == "Cidadela São Paulo, paisete Brasil"