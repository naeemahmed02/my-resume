from django.shortcuts import render
from django.http import HttpResponse

from resumeapp.models import PersonalInfo, Project, Education, Experience, Resume


def home(request):
    personal_info = PersonalInfo.objects.first()
    projects = Project.objects.all()[:3]
    educations = Education.objects.all()[:3]
    experiences = Experience.objects.all().all()
    resume = Resume.objects.first()
    context = {'personal_info': personal_info,
               'projects': projects,
               'educations': educations,
               'experiences': experiences,
               'resume': resume,
               }
    return render(request, 'resumeapp/index.html', context)