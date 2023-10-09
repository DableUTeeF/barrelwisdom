from django.db import models
from games.A25.misc_a25.models import Name, Desc
from games.A25.item_a25.models import Item

# this may look cute and small but what if I added monsters...?

class Encounter(models.Model):
    name  = models.ForeignKey(Name, on_delete=models.CASCADE)
    exp = models.IntegerField()
    combat_level = models.IntegerField()
    cole = models.IntegerField(default=0)
    gems = models.IntegerField(default=0)
    kind = models.ForeignKey(Name, on_delete=models.CASCADE)

class Reward(models.Model):
    encount = models.ForeignKey(Encounter, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    num = models.IntegerField(blank=True, null=True)
    tier = models.IntegerField(default=1)