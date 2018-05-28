from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from treeplan import views

router = DefaultRouter()
router.register(r'plans', views.PlanViewSet)
router.register(r'trees', views.TreeViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
