from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin

from courses.models import Course

from .forms import CourseEnrollForm


class StudentRegistrationView(CreateView):
    """ Регистрирует нового студента, в случае успеха - редирект на страницу его курсов """

    template_name = 'students/student/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('student_course_list')

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

    def form_valid(self, form):
        self.course = form.cleaned_data['course']
        self.course.students.add(self.request.user)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('student_course_detail',
                            args=[self.course.id])


class StudentCourseListView(LoginRequiredMixin, ListView):
    """ Отображает курсы, на которые зачислен студент """

    model = Course
    template_name = 'students/course/list.html'
    context_object_name = 'courses'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(students__in=[self.request.user])


class StudentCourseDetailView(DetailView):
    """ Отображает выбранный студентом курс """
    
    model = Course
    template_name = 'students/course/detail.html'
    context_object_name = 'course'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(students__in=[self.request.user])

    def get_context_data(self, **kwargs):
        """ Добавляет в контекст номер модуля курса, если он задан в URL. 
        Иначе задает первый модуль курса """

        context = super().get_context_data(**kwargs)

        course = self.get_object()
        if 'module_id' in self.kwargs:
            context['module'] = course.modules.get(id=self.kwargs['module_id'])
        else:
            context['module'] = course.modules.all()[0]
        return context
    