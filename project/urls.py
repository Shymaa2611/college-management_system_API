"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/data/',view=views.student_data),
    path('api/data/<int:pk>/',view=views.change_data),
    path('api/data/search/',view=views.search_student_GPA),
    path('api/data/first_student/',view=views.get_ten_first_student),
    path('api/data/get_count/',view=views.get_data),
    path('api/data/enroll_subject/',view=views.enroll_subject),
    path('api/data/attendance/<int:pk>/',view=views.student_attendance),
    path('api/data/report/<int:pk>/',view=views.generate_report),
    path('users/',include('accounts.urls'))
]
admin.site.site_header='FCI SYSTEM'
