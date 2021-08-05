from Clients import clients


class Clients:
    def __init__(self, name=str, money=int, city="", status=str):
        self.name = name
        self.money = money
        self.city = city
        self.status = status

    def getName(self):
        return self.name

    def getMoney(self):
        return self.money

    def getCity(self):
        return self.city

    def getStatus(self):
        return self.status


for i in clients:
    clients_pet = Clients(name=i.get("name"),
                  money=i.get("money"),
                  city=i.get("city"),
                  status=i.get("status"))

    print('--------------------')
    print(clients_pet.name, ',', clients_pet.money, ',', clients_pet.city, ',', clients_pet.status)


    print('--------------------')
    print('Имя клиента: ',clients_pet.name)
    print('Баланс счета клиента: ',clients_pet.money)
    print('Город клиента: ',clients_pet.city)
    print('Статус клиента: ',clients_pet.status)

