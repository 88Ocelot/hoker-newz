from posts.api import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register("posts", views.PostView, basename="posts")
urlpatterns = router.urls
