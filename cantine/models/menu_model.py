from django.db import models

from base.helpers.named_date_time_model import NamedDateTimeModel


class MenuModel(NamedDateTimeModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=180)
    dishes = models.OneToOneField('DishesModel', on_delete=models.CASCADE, related_name='menu')

