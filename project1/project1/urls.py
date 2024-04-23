
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # for function based view
    path('studentapi/', views.student_api),
    # for class based view
    path('studentapi/', views.StudentAPIView.as_view(), name='student_api'),
]
