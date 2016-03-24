"""Directory Items"""

import os
import json


class Project():
    """ Define each project """

    projects = []

    # Constructor
    def __init__(self, path, project=None, new=False, name=None):
        if not new:
            try:
                self.name = project['name']
                self.description = project['description']
                self.created = project['created']
                self.project_type = project['type']
            except KeyError:
                self.error = True
        else:
            self.name = name

        self.new = new
        self.path = path.replace('\\', '/')

        # Add self to list
        self.projects.append(self)

def list_projects():
    """ Gets all projects in directory """
    for root, dirs, files in os.walk('..\\sites'):
        for directory in dirs:
            path = os.path.abspath(root) + '\\' + directory
            # path = os.path.join(root, dir)
            # If already init
            try:
                project_data = json.load(open(path + '/project_data.json'))
                Project(path, project_data)
            # Else mark as new
            except FileNotFoundError:
                Project(path, new=True, name=directory)

    projects = Project.projects
    Project.projects = []
    return projects

def save_project(project):
    """Save project to JSON"""

    project = {
        'name': project['name'],
        'description': project['description'],
        'created': project['created'],
        'type': project['type'],
        'path': project['path'],
    }

    project_data = open(project['path'] + '/project_data.json', 'w')

    json.dump(project, project_data)

def get_project(path):
    project_data = None

    try:
        project_data = json.load(open(path + '/project_data.json'))
    except FileNotFoundError:
        return False

    return project_data

def edit_project(project):
    """Edit settings of project"""
