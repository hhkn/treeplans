from django.db import models


class Plan(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    milestone = models.DecimalField(max_digits=10,decimal_places=2)


class Tree(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    plan = models.ForeignKey(Plan, related_name="trees", on_delete=models.CASCADE)
    x = models.DecimalField(max_digits=10,decimal_places=2)
    y = models.DecimalField(max_digits=10,decimal_places=2)
    name = models.CharField(max_length=100, blank=True, null=True)
    sciName = models.CharField(max_length=100, blank=True, null=True)
    diameter = models.DecimalField(max_digits=10,decimal_places=2, blank=True, null=True)
    height = models.DecimalField(max_digits=10,decimal_places=2, blank=True, null=True)
    heightToCrown = models.DecimalField(max_digits=10,decimal_places=2, blank=True, null=True)
    crownSpread = models.DecimalField(max_digits=10,decimal_places=2, blank=True, null=True)
    age = models.DecimalField(max_digits=10,decimal_places=2, blank=True, null=True)
    ontogenetic = models.CharField(max_length=100, blank=True, null=True)
    health = models.CharField(max_length=100, blank=True, null=True)
    note = models.CharField(max_length=100, blank=True, null=True)

