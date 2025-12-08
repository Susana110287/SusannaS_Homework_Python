from smartphone import Smartphone

#создала список смартофонов
catalog = [
    Smartphone("Samsung Galaxy", "A25", "+79131111110"),
    Smartphone("Motorola Moto", "G34", "+79131111111"),
    Smartphone("Xiaomi Redmi", "Note 14", "+79131111112"),
    Smartphone("Realme", "C75", "+79131111113"),
    Smartphone("Xiaomi Poco", "M6 Pro", "+79131111114")
]

#печать списка смартфонов
for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model} - {smartphone.number}") 