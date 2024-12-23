from collections import namedtuple
from email.policy import default

product=namedtuple('product',['name', 'created_at', 'colour', 'price'],
                   defaults=['i phone 16',2024,'qora',1700,])

car=product('gentra',2023,'qora',17000)
phone=product('24_ultra',2024,'seriy',1200)
fridge=product('samsung',2020,'grey',500)
i_phone=product
user=namedtuple('user',['fullname','age','phone','email'])

students=[
        ['Ali_Aliev','20',1234567,'Ali@gmail.com'],
        ['Nodir_Qodirov','22', 10008348,'Nodir@gmail.com'],
        ['Aziza_Lazizov','18', 22244466,'Aziza.gmail.com']
]
# print(car._fields)
# print(i_phone._field_defaults)
#
# for users in students:
#     x=user._make(users)
#     print(f"{x.fullname},{x.age},{x.phone},{x.email}")

class item(namedtuple('product',['name', 'price'])):
    def sale(self):
        if self.price > 1000:
            x=(self.price-(self.price/10))
            return x

product=item('samsung',1500)
print(product.sale())


