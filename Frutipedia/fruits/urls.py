from django.urls import path, include

from Frutipedia.fruits import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-categories/', views.create_categories, name='create_categories'),
    path('create-fruit', views.create_fruit, name='create_fruit'),
    path('<int:pk>/', include([
        path('delete-fruit/', views.delete_fruit, name='delete_fruit'),
        path('detail-fruit/', views.detail_fruit, name='detail_fruit'),
        path('edit-fruit/', views.edit_fruit, name='edit_fruit'),
    ]))
]