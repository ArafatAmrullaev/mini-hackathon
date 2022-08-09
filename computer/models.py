from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# модельки
# Компьютер (модель, кол-во ядер(2, 4, 8, 16), оператвная память (2-120), цена, фото)
# Рейтинг (пользователь, компьютер, значение(1-5))

class Computer(models.Model):
    model = models.CharField(max_length=50)
    count_core = models.IntegerField(choices=[(2,2), (4,4), (8,8), (16,16)])
    ram = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(120),
            MinValueValidator(2)
        ]
     )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='computers', blank=True, null=True)




    @property
    def average_rating(self):
        ratings = [rating.value for rating in self.ratings.all()]
        if ratings:
            return sum(ratings)/len(ratings)
        else:
            return 0
