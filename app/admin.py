"""
Define models to import into admin
"""

from django.contrib import admin
from app.models import ProjectType
from app.models import Generator

admin.site.register(ProjectType)
admin.site.register(Generator)
