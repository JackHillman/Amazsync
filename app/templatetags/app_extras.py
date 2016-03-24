from django import template
from app import models

register = template.Library()

@register.filter
def getcolour(key):
    project_types = models.ProjectType.objects.all()
    colors = {}
    for project in project_types:
        colors[project.name] = project.colour

    return colors.get(key)
