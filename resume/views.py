from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

from resume.models import About, HomeInfo, Projects, Experience, Certificates
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def home(request):
    info = HomeInfo.objects.all()
    return render(request, "home.html", {"info": info, "is_homepage": True})


def about(request):
    items = About.objects.all()
    return render(request, "about.html", {"items": items})


def projects(request):
    project_show = Projects.objects.all()
    paginator = Paginator(project_show, 1)
    page = request.GET.get("page")
    print(page)
    try:
        project_show = paginator.page(page)
    except PageNotAnInteger:
        project_show = paginator.page(1)
    except EmptyPage:
        project_show = paginator.page(paginator.num_pages)
        print(project_show)

    return render(
        request, "projects.html", {"project_show": project_show, "page": page}
    )


def aboutproject(request, project_id):
    project = get_object_or_404(Projects, id=project_id)
    print(project.title, project.decription)
    return render(request, "aboutproject.html", {"project": project})


def experience(request):
    experience = Experience.objects.all()
    return render(request, "experience.html", {"experience": experience})


def certificates(request):
    show_cert = Certificates.objects.all()
    return render(request, "certificates.html", {"show_cert": show_cert})


def contact(request):
    return render(request, "contact.html")


def resume(request):
    resume_path = "cv/python.pdf"
    resume_path = staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path, "rb") as resume_file:
            response = HttpResponse(resume_file.read(), content_type="application/pdf")
            response["Content-Disposition"] = 'attachment; filename="python.pdf"'
            return response
    else:
        return HttpResponse("Resume not found", status=404)
