# urls.py
from django.urls import path
from .views import RepPerformanceView, TeamPerformanceView, PerformanceTrendsView

urlpatterns = [
    path('rep_performance', RepPerformanceView.as_view(), name='rep_performance'),
    path('team_performance', TeamPerformanceView.as_view(), name='team_performance'),
    path('performance_trends', PerformanceTrendsView.as_view(), name='performance_trends'),
]
