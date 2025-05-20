from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

from courses.views import CourseListView, logout_user


urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', logout_user, name='logout'),
    path('course/', include('courses.urls')),
    path('students/', include('students.urls')),
    path('admin/', admin.site.urls),
    path('', CourseListView.as_view(), name='course_list'),
    path('api/v1/', include('courses.api.urls'), name='api'),
]


if settings.DEBUG:
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls'))]       
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
