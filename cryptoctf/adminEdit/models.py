from django.db import models
from django.core.validators import validate_comma_separated_integer_list

# Create your models here.
class challengeinfo(models.Model):
    name = models.CharField(max_length = 1024)
    author = models.CharField(max_length = 100, null = True, blank = True)
    description = models.TextField()
    group = models.CharField(max_length = 10)
    pt = models.IntegerField(default=0)
    times = models.IntegerField(default=0)
    solvers = models.TextField(default = '{"solvers": []}')
    flag = models.CharField(max_length = 128)
    attachment = models.CharField(max_length = 128, null = True)

