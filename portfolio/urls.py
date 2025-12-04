from django.contrib import admin
from django.urls import include, path
from blog.views import blog, post
from resume.views import home, profile, projects, contact, skils, school, work_ex, certificate, project

from uauth.views import login, signup, password_reset




urlpatterns = [
    # Django's normal admin (KEEP THIS)
    path('admin/', admin.site.urls),

    # MongoEngine admin (THIS is the correct location)

    
    # Authentication (Allauth)
    path('accounts/', include('allauth.urls')),

    # App routes
    path('home/', home.home_view, name="home"),

    # Resume
    path('profile/', profile.profile_view, name="profile"),

    # Resume API
    path('api/skill/', skils.SkillCRUDAPIView.as_view()),
    path('api/skill/<str:skill_id>/', skils.SkillCRUDAPIView.as_view()),

    path('api/school/', school.SchoolCRUDAPIView.as_view()),
    path('api/school/<str:school_id>/', school.SchoolCRUDAPIView.as_view()),

    path('api/work/', work_ex.WorkExCRUDAPIView.as_view()),
    path('api/work/<str:work_ex_id>/', work_ex.WorkExCRUDAPIView.as_view()),

    path('api/certificate/', certificate.CertificateCRUDAPIView.as_view()),
    path('api/certificate/<str:certificate_id>/', certificate.CertificateCRUDAPIView.as_view()),

    path('api/project/', project.ProjectCRUDAPIView.as_view()),
    path('api/project/<str:project_id>/', project.ProjectCRUDAPIView.as_view()),

    path('projects/', projects.project_view, name="projects"),

    path('contact/', contact.contact_view, name="contact"),
    path('contact/submit/', contact.contact_submit, name="contact_submit"),


    # Blog
    path('blog/', blog.blog_view, name="blog"),
    path('post/<slug:post_id>/', post.post_view, name="blog_post"),

    # Blog API
    # path('api/blog/', blog.BlogPostListCreateAPI.as_view()),
    # path('api/post/<str:pk>/', post.BlogPostRetrieveUpdateDeleteAPI.as_view()),

    # User auth (custom)
    path('login/', login.login_view, name="login"),
    path('signup/', signup.signup_view, name="signup"),
    path('reset/', password_reset.password_reset_view, name="password_reset"),
]