from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CourseEnrollForm


class StudentRegistrationView(CreateView):
    """ Регистрирует нового студента, в случае успеха - редирект на главную страницу """
    template_name = 'students/student/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('course_list')

    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'],
                            password=cd['password1'])
        login(self.request, user)
        return result


class StudentEnrollCourseView(LoginRequiredMixin, FormView):
    """ Записывает студента на курс, в случае успеха - редирект на главную страницу """
    course = None
    form_class = CourseEnrollForm
    success_url = reverse_lazy('course_list')

    def form_valid(self, form):
        self.course = form.cleaned_data['course']
        self.course.students.add(self.request.user)
        return super().form_valid(form)
    