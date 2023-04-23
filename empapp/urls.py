
from django.urls import path
from empapp import views

urlpatterns = [
    
    path('add/', views.add_employee_view),
    path('list/', views.employee_list),
    path('detail/<int:id>/', views.employee_detail),
    path('update/<int:id>/', views.update_employee),
    path('delete/<int:id>/', views.delete_employee),
    path('register/', views.user_register_view)

    
]