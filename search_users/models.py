from django.db import models
from django_mysql.models import ListCharField

# Create your models here.
class User(models.Model):
    user_id = models.CharField("USERID", max_length=10, primary_key=True)
    name = models.CharField("NAME", max_length=10)
    created_at = models.DateField(auto_now_add=True)
    gold = models.IntegerField("GOLD")
    level = models.IntegerField("LEVEL")
    inventory = ListCharField(
        base_field=models.CharField(max_length=10), size=10, max_length=(10 * 11)
    )

    def __str__(self):
        return self.user_id
