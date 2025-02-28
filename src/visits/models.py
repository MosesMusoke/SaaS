from django.db import models

# Create your models here.
class PageVisits(models.Model):
    # database -> table
    # id -> hidden -> primary key -> autofield -> 1,2,3,4
    path = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)



