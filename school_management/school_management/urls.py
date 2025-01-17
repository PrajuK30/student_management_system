


from django.contrib import admin
from django.urls import path, include
from students import views  # Import the home view from students app

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin panel
    path('', views.home, name='home'),  # Root URL (/) maps to home view
    path('students/', include('students.urls')),  # Include students app URLs
]


