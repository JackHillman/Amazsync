import subprocess
from directory import save_project

def CreateProject(project, generator, args):
    try:
        subprocess.check_call(['yeo', generator])
    except:
        return subprocess.CalledProcessError
    else:
        save_project(project)
