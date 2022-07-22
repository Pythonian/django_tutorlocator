from django.shortcuts import render

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
    pass


def courses(request):
    pass


def course(request, slug):
    pass
