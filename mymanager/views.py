from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Trainer, Course, Announcement

# Create your views here.


def index(request):
    return render(request, 'index.html')


def trainers(request):
    trainers = Trainer.objects.all()

    return render(request, 'trainers.html', {'trainers': trainers})


def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})


def announcements(request):
    announcements = Announcement.objects.all()

    return render(request, 'announcements.html', {'announcements': announcements})


def add_trainer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        bio = request.POST.get('bio')
        experience = request.POST.get('experience')

        # saving the new trainer to the database

        Trainer.objects.create(name=name, bio=bio, experience=experience)

        return redirect('trainers')

    return render(request, 'add_trainers.html')


def add_course(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        duration = request.POST.get('duration')

        # saving the new course to the database

        Course.objects.create(
            title=title, description=description, duration=duration)

        return redirect('courses')

    return render(request, 'add_course.html')


def add_announcement(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        message = request.POST.get('message')

        # saving the new announcement to the database
        # Create announcement - date_posted will be auto-set by the model

        Announcement.objects.create(
            title=title, message=message)

        return redirect('announcements')

    return render(request, 'add-announcement.html')


# adding delete for the  differnt pages
def delete_trainer(request, id):
    trainer = trainer = get_object_or_404(Trainer, id=id)
    trainer.delete()
    return redirect('trainers')


def delete_course(request, id):
    course = get_object_or_404(Course, id=id)
    course.delete()
    return redirect('courses')


def delete_announcement(request, id):
    announcement = get_object_or_404(Announcement, id=id)
    announcement.delete()
    return redirect('announcements')
