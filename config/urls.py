from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from config.rest import router
from graphene_django.views import GraphQLView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    url(
        r"^about/$",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),
    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, admin.site.urls),
    # User management
    url(r"^users/", include("bootcamp.users.urls", namespace="users")),
    url(r"^accounts/", include("allauth.urls")),
    # Third party apps here
    url(r"^comments/", include("django_comments.urls")),
    url(r"^graphql", GraphQLView.as_view(graphiql=True)),
    url(r"^markdownx/", include("markdownx.urls")),
    # Local apps here
    url(
        r"^notifications/",
        include("bootcamp.notifications.urls", namespace="notifications"),
    ),
    url(r"^articles/", include("bootcamp.articles.urls", namespace="articles")),
    url(r"^news/", include("bootcamp.news.urls", namespace="news")),
    url(r"^messages/", include("bootcamp.messager.urls", namespace="messager")),
    url(r"^qa/", include("bootcamp.qa.urls", namespace="qa")),
    url(r"^search/", include("bootcamp.search.urls", namespace="search")),

    url(r"^photos/", include('photologue.urls', namespace='photos')),

    url(r'api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/', include(router.urls)),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development
    urlpatterns += [
        url(
            r"^400/$",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        url(
            r"^403/$",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        url(
            r"^404/$",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        url(r"^500/$", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [url(r"^__debug__/", include(debug_toolbar.urls))] + urlpatterns
