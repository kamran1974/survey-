from .views import OpinionViewSet, ClientViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'opinion', OpinionViewSet)
router.register(r'client', ClientViewSet)
urlpatterns = router.urls