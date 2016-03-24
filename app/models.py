"""
Definition of models.
"""

from django.db import models

class ProjectType(models.Model):
    """Define project types"""

    colours = (
        ('grey', 'Grey'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),
        ('orange', 'Orange'),
        ('red', 'Red'),
        ('pink', 'Pink'),
        ('purple', 'Purple'),
    )

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    colour = models.CharField(
        max_length=20,
        choices=colours,
        default='grey')

    def __str__(self):
        return self.name

class Generator(models.Model):
    """Define Scaffolding Constructors"""

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    yeo_tag = models.CharField(max_length=100)

    def __str__(self):
        return self.name
