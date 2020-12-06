from django.urls import path
from . import views
# from knox import views as knox_views
from rest_framework_simplejwt.views import TokenRefreshView
from .views import ModTokenObtainPairView

urlpatterns = [
    path('register/', views.RegisterUserView.as_view()),
    path('update/<int:id>/', views.UpdateUserView.as_view()),
    # path('login/', views.LoginUserView.as_view()),
    # path('logout/', knox_views.LogoutView.as_view(), name='knox-logout')
    path('token/', ModTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]