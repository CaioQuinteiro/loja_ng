from django.contrib import admin
from django.urls import path, include
from estoque.views import DashboardView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estoque/', include('estoque.urls', namespace='estoque')),
    path('', DashboardView.as_view(), name='dashboard'),          # home → dashboard
    path('admin/', admin.site.urls),
    path('estoque/', include('estoque.urls', namespace='estoque')),
]