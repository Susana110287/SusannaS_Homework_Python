from address import Address
from mailing import Mailing

# создала адреса отправителя и получателя
from_addr = Address("658060", "Новоалтайск", "Майская", "8", "2")
to_addr = Address("690001", "Владивосток", "Абрикосовая", "11", "10")

# создала экземпляр почтового отправления
mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=10000,
    track="RU81123654025"
)

# печать информацию об отправлении
print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, "
    f"{mailing.from_address.city}, {mailing.from_address.street}, "
    f"{mailing.from_address.house} - {mailing.from_address.flat} "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.flat}. Стоимость {mailing.cost} рублей."
)
