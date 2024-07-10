from django.shortcuts import render,get_object_or_404
from django .http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

from resume.models import About, HomeInfo, Projects


# Create your views here.


def home(request):
    info = HomeInfo.objects.all()
    return render(request, "home.html", {"info": info})


def about(request):
    items = About.objects.all()
   
    return render(request, "about.html", {"items": items})


def projects(request):
    project_show = Projects.objects.all()
    # projects_show = [
    #     {
    #         "title": "Ecommerce",
    #         "path": "images/projects_img/ecom.jpeg",
    #     },
    #     {
    #         "title": "Salon",
    #         "path": "images/projects_img/hairsalon.jpeg",
    #     },
    #     {
    #         "title": "Portfolio",
    #         "path": "images/projects_img/portfolio_project.jpeg",
    #     },
    # ]
    return render(request, "projects.html", {"project_show": project_show})

def aboutproject(request, project_id):
    project = get_object_or_404(Projects, id=project_id)
    print(project.title, project.decription) 
    return render(request, "aboutproject.html", {"project": project})


def experience(request):
    experience = [
        {
            "Company": "Google",
            "Position": "Software Engineer",
            "Duration": "2020-present",
        },
        {
            "Company": "Microsoft",
            "Position": "Django Developer",
            "Duration": "2020-2021",
        },
        {
            "Company": "Arco",
            "Position": "Django Developer",
            "Duration": "2020-2021",
        },
        {
            "Company": "Facebook",
            "Position": "Django Developer",
            "Duration": "2020-2021",
        },
        {
            "Company": "Facebook",
            "Position": "Django Developer",
            "Duration": "2020-2021",
        },
        {
            "Company": "Facebook",
            "Position": "Django Developer",
            "Duration": "2020-2021",
        },
    ]
    return render(request, "experience.html", {"experience": experience})


def certificates(request):
    return render(request, "certificates.html")


def contact(request):
    return render(request, "contact.html")

def resume(request):
    resume_path ="cv/python.pdf"
    resume_path = staticfiles_storage.path(resume_path)
    if  staticfiles_storage.exists(resume_path):
        with open(resume_path, 'rb') as resume_file:
            response = HttpResponse(resume_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="python.pdf"'
            return response
    else:
        return HttpResponse("Resume not found", status=404)
