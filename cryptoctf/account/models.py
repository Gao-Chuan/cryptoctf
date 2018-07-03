from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userinfo(User):
    country = models.CharField(max_length = 1, null=True, blank=True, default = '')
    pt = models.IntegerField(default=0)
    doneList = models.TextField(default = '{"doneList": []}')
    class Meta:
        db_table = 'userinfo'