from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import views

# Router for the API only accepts ViewSets, Not views, as Views not get_extra_actions
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', include(router.urls), name='users'),  # noqa # Includes URLs from the router
    # path('restaurant/booking/', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),  # noqa Enables browsable API
    path('menu-items', views.MenuItemView.as_view(), name='menu-items'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth', obtain_auth_token),
]
