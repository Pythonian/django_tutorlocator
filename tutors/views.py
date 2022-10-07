from django.shortcuts import get_object_or_404, render

from accounts.models import Tutor
from .models import Course, Testimonial


def home(request):
    courses = Course.objects.order_by('?')[:8]
    testimonials = Testimonial.objects.all()[:5]

    template = 'home.html'
    context = {
        'courses': courses,
        'testimonials': testimonials,
    }
    return render(request, template, context)


def tutors(request):

    template = 'tutors.html'
    context = {}
    return render(request, template, context)


def tutor_requests(request):

    template = 'tutor_requests.html'
    context = {}
    return render(request, template, context)


def search(request):
    
    template = 'search.html'
    context = {}
    return render(request, template, context)


def courses(request):
    courses = Course.objects.all()
    
    template = 'courses.html'
    context = {
        'courses': courses,
    }
    return render(request, template, context)


def course(request, slug):
    course = get_object_or_404(Course, slug=slug)
    tutors = Tutor.objects.filter(course=course)
    
    template = 'course.html'
    context = {
        "course": course,
        "tutors": tutors,
    }
    return render(request, template, context)
