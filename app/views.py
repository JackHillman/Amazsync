"""
Definition of views.
"""

import json
from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext
from app import directory
from app import models

def bad_request(request):
    return render (
        request,
        'app/bad.html',
        context_instance=RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'name':'Amazsync',
        })
    )

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    project_list = directory.list_projects()
    project_types = models.ProjectType.objects.all()

    if request.method == 'POST':
        directory.save_project(request.POST)

    return render(
        request,
        'app/index.html',
        context_instance=RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'name':'Amazsync',
            'projects':project_list,
            'count':len(project_list),
            'types':project_types,
        })
    )

def get_project_data(request):
    """Returns Project Data"""
    assert isinstance(request, HttpRequest)
    if not request.is_ajax():
        return bad_request(request)


    project_data = None
    request_path = str(request.GET.get('path'))
    if request.method == 'GET':
        project_data = directory.get_project(request_path)
        return HttpResponse(json.dumps(project_data), content_type="application/json")


def gen(request):
    """Renders the generator page."""
    assert isinstance(request, HttpRequest)
    generators = models.Generator.objects.all()
    return render(
        request,
        'app/generator.html',
        context_instance=RequestContext(request,
        {
            'generators': generators,
            'title': 'Generator',
            'year':datetime.now().year,
            'name':'Amazsync',
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance=RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance=RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )
