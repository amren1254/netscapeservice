from django.urls import path, re_path
from . import views
from main.sitemaps import TutorialSitemap
from django.contrib.sitemaps.views import sitemap  # Add this import
# TutorialCategorySitemap, TutorialSeriesSitemap,

app_name = 'main'  # here for namespacing of urls.
# sitemaps = {
#     'categories': TutorialCategorySitemap,
#     'series': TutorialSeriesSitemap,
#     'tutorials': TutorialSitemap,
# }
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register/", views.register, name="register"),
    path("logout", views.logout_request, name="logout"),
    path("login", views.login_request, name="login"),
    path("<single_slug>", views.single_slug, name="single_slug"),
    path("sitemap.xml/", views.sitemap, name="sitemap"),
    # path("ads.txt/", views.ads_txt, name="ads_txt"),
    path("ads.txt/", views.ads_txt_view, name="ads_txt_view"),




]
