from base.helpers.named_date_time_model import NamedDateTimeModel
from django.db import models

class DishesModel(NamedDateTimeModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=180)
    summary = models.TextField()

    def __str__(self):
        return self.name
