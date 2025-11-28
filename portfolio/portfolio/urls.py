"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from resume.views import home, profile, projects, blog, contact
from uauth.views import login, signup, password_reset

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    
    path('home/', home.home_view, name="home"),
    path('profile/', profile.profile_view, name="profile"),
    path('projects/', projects.project_view, name="projects"),
    # path('blog/', blog.blog_view, name="blog"),
    # path("post/<slug:post_id>/", blog.post_view, name="blog_post")
    path('contact/', contact.contact_view, name="contact"),
    path("contact/submit/", contact.contact_submit, name="contact_submit"),

    path('login/', login.login_view, name="login"),
    path('signup/', signup.signup_view, name="signup"),
    path('reset/', password_reset.password_reset_view, name="password_reset"),


]