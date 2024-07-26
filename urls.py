from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_complaint, name='submit_complaint'),
    path('success/', views.complaint_success, name='complaint_success'),
    path('resolve/<int:complaint_id>/', views.resolve_complaint, name='resolve_complaint'),
    path('resolved/', views.complaint_resolved, name='complaint_resolved'),
]
