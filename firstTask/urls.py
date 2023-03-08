from django.urls import path
from . import views


urlpatterns = [
    path('', views.display),
    path('about',views.formCreation,name = 'ab'),
    path('<str:name>', views.PersonInfo,name="info"),
    path('delete/<int:id>', views.deleteStudent,name="delete"),
    path('update/<int:id>', views.updateStudent,name="update"),


]