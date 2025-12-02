from resume.model.certificate import Certificate
from resume.model.contact_message import ContactMessage
from resume.model.line_item import LineItem
from resume.model.school import School
from resume.model.skill import Skill
from resume.model.work_ex import WorkExperience
from resume.model.project import Project
from datetime import datetime
from uauth.model.user import User
from django.contrib.auth.hashers import make_password

from blog.models.post import BlogPost

def populate_certificates(user):
    c1 = Certificate(
        title="Crash Course on Python",
        issuer="Coursera",
        link="https://www.coursera.org/account/accomplishments/certificate/HHMNEUBJCFFU/",
        date = datetime(2021, 1, 30)
    )
    c1.save(user)
    c2 = Certificate(
        title="Problem Solving (Basic)",
        issuer="HackerRank",
        link="https://www.hackerrank.com/certificates/2c40fc9e4485",
        date = datetime(2021, 1, 12)
    )
    c2.save(user)

    c3 = Certificate(
        title="C++ (Basic) Certificate",
        issuer="HackerRank",
        link="https://www.hackerrank.com/certificates/c1693af613e5",
        date = datetime(2021, 1, 12)
    )
    c3.save(user)

    c4 = Certificate(
        title="Python (Advanced) Certificate",
        issuer="HackerRank",
        link="https://www.hackerrank.com/certificates/e85e9cb8f40e",
        date = datetime(2020, 9, 12)
    )
    c4.save(user)

    c5 = Certificate(
        title="Algorithmic Toolbox (Uc San Diego)",
        issuer="Coursera",
        link="https://www.coursera.org/account/accomplishments/certificate/XJAAWUNX3TLP",
        date = datetime(2020, 5, 1)
    )
    c5.save(user)
    

    c6 = Certificate(
        title="Algorithms (Stanford)",
        issuer="Coursera",
        link="https://www.coursera.org/account/accomplishments/certificate/XJAAWUNX3TLP",
        date = datetime(2019, 8, 1)
    )
    c6.save(user)

def populate_schools(user):
    s1 = School(
        institution="Birla Institute of Technology and Science, Pilani",
        degree="Master of Science in Biology & Bachelor of Engineering in Civil Engineering (Hons.)",
        start_date = datetime(2017, 5, 1),
        end_date = datetime(2022, 6, 1),
        description = [],
        location="Pilani, Rajasthan, India"

    )
    s1.save(user)
    # s2 = School(
    #     institution="Example Institute of Technology",
    #     degree="Master of Science in Software Engineering",
    #     start_date = datetime(2020, 9, 1),
    #     end_date = datetime(2022, 6, 15),
    #     description = [],
    #     location="New York"
    # )
    # s2.save()


def populate_skills(user):
    s1 = Skill(name="Python", proficiency=9)
    s1.save(user)
    s2 = Skill(name="FastAPI", proficiency=9)
    s2.save(user)
    s3 = Skill(name="Docker", proficiency=7)
    s3.save(user)
    s4 = Skill(name="Django", proficiency=8)
    s4.save(user)

    s5 = Skill(name="Kotlin", proficiency=7)
    s5.save(user)
    s6 = Skill(name="Springboot", proficiency=7)
    s6.save(user)
    s7 = Skill(name="Celery", proficiency=7)
    s7.save(user)
    s8 = Skill(name="Redis", proficiency=8)
    s8.save(user)

def populate_work_experiences(user):
    '''
    class LinkItem:
    name = StringField(required=True, max_length=100)
    url = StringField(required=True)

class LineItem(MongoBaseModel):
    meta = {'collection': 'line_item'}
    name = StringField(required=True, max_length=100)
    description = StringField(default="")
    link = ListField(field=LinkItem, default=[])
    '''
    desc1 = [
        LineItem.create(
            name="1",
            description="Re-engineered inventory APIs using aggregation pipelines, improving system performance and reducing average latency by 20%, delivering smoother user workflows across high-traffic dashboards",
            link=[]
        ),
        LineItem.create(
            name="2",
            description="Designed and implemented a full-featured inventory system tracking material lifecycle, suppliers, warehouse locations, pricing, and project assignments, ensuring data accuracy at scale.",
            link=[]
        ),
        LineItem.create(
            name="3",
            description="Built a resilient two-way QuickBooks Online sync engine supporting multiple company accounts; guaranteed data integrity with conflict resolution, incremental updates, and configurable sync policies",
            link=[]
        ),
        LineItem.create(
            name="4",
            description="Implemented intelligent email ingestion pipelines that extracted invoices and leads, drastically reducing manual entry and accelerating financial operations for end-users.",
            link=[]
        ),
        LineItem.create(
            name="5",
            description="Developed a dependency-aware project scheduling engine using topological sorting, ensuring accurate and reliable task ordering even under complex constraints.",
            link=[]
        ),
        LineItem.create(
            name="6",
            description="Implemented a timezone-aware attendance/payroll engine to accurately compute labor costs across global teams, improving financial transparency for customers.",
            link=[]
        )

    ]
    w1 = WorkExperience(
        org="Merlin AI",
        role="Software Engineer",
        start_date=datetime(2025, 2, 20),
        end_date=None,
        description=desc1,
        location="Remote"
    )
    w1.save(user)
    desc2 = [
        LineItem.create(
            description="Designed a scalable Domain-Driven entity platform enabling customers to create dynamic schemas, import/export large datasets, and manage complex vendor/product/contract information with high reliability.",
            name="1",
            link=[]
        ),
        LineItem.create(
            description="Built a conditional migration execution framework ensuring safe, tenant-specific schema evolution across multi-organization environments",
            name="2",
            link=[]
        ),
        LineItem.create(
            description="Developed a high-throughput AuditLog system using MongoDB Change Streams and in‑memory listeners, giving users real-time visibility into critical operations.",
            name="3",
            link=[]
        ),
        LineItem.create(
            description="Architected a modular, plug‑and‑play chat service used for cross‑team and cross‑organization negotiations, built for resilience and minimal coupling",
            name="4",
            link=[]
        ),
        LineItem.create(
            description="Implemented an ECS Fargate–based scheduler that spawned isolated workers for each job, ensuring fault-tolerance and efficient resource utilization.",
            name="5",
            link=[]
        )
    ]
    w2 = WorkExperience(
        org="Expent",
        role="Software Engineer",
        start_date=datetime(2022, 12, 1),
        end_date=datetime(2024, 10, 31),
        description=desc2,
        location="Remote"
    )
    w2.save(user)

    desc3 = [
        LineItem.create(
            name="1",
            description="Automated end-to-end KYC by integrating complex, stateful Digio APIs, transforming a multi‑day manual onboarding into a fully online 5‑minute flow, significantly improving user experience and operational scalability",
            link=[]
        ),
        LineItem.create(
            name="2",
            description="Designed resilient async pipelines to execute onboarding Steps using Celery, ensuring fault-tolerance, idempotency and smooth execution of long-running tasks under real-world load.",
            link=[]
        )
    ]
    w3 = WorkExperience(
        org="Wealthy",
        role="Software Engineer",
        start_date=datetime(2022, 1, 5),
        end_date=datetime(2022, 11, 30),
        description=desc3,
        location="Bengauluru, India"
    )
    w3.save(user)


def populate_projects(user):
    '''
    class Project(MongoBaseModel):
    meta = {'collection': 'project'}
    name = StringField(required=True, max_length=100)
    published_date = DateTimeField()
    description = ListField(field=LineItem(), default=[])
    link = StringField(default="")
    '''
    d1 = [
        LineItem.create(
            name="Developed a personal portfolio website using Django",
            description="Showcased projects, skills, and experience with a responsive design.",
            link=[]
        ),
        LineItem.create(
            name="Implemented SEO best practices to improve site visibility.",
            description="Increased organic traffic by optimizing content and metadata.",
            link=[]
        )

    ]
    p1 = Project(
        name="Personal Portfolio Website",
        published_date=datetime(2025, 11, 24),
        description=d1,
        link="https://www.example.com/portfolio"
    )
    p1.save(user)
    # d2 = [
    #     LineItem.create(
    #         name="Designed and developed a full-featured e-commerce platform.",
    #         description="Implemented user authentication, product management, and payment processing.",
    #         link=[]
    #     ),
    #     LineItem.create(
    #         name="Integrated third-party APIs for shipping and inventory management.",
    #         description="Enhanced functionality and streamlined operations.",
    #         link=[]
    #     )
    # ]
    # p2 = Project(
    #     name="E-commerce Platform",
    #     published_date=datetime(2023, 7, 10),
    #     description=d2,
    #     link="https://www.example.com/ecommerce"
    # )
    # p2.save()


def populate_blog_post(user):
    post = BlogPost(
        title = "Personal Portfolio",
        summary = "Showcasing my projects, skills, and experience through a personal portfolio website built with Django.",
        content = '''In this blog post, I will walk you through the development of my personal portfolio website using Django. The website serves as a platform to showcase my projects, skills, and professional experience.
        ''',
        is_published = True,
        published_at = datetime(2025, 12, 1)
    )
    
    post.save(user)

def populate_user():
    user = User.objects(email="ibhatia1998@gmail.com").first() or User()
    user.email = "ibhatia1998@gmail.com"
    user.password = make_password("Ishan@2025!")
    user.first_name = "Ishan"
    user.last_name = "Bhatia"
    user.profile_picture = "https://i.postimg.cc/Y2DPgcCs/from-fractions-to-fractals.jpg"
    user.github_url = "https://github.com/Ishanbhatia98"
    user.leetcode_url = "https://leetcode.com/u/ishanbhatia/"
    user.linkedin_url = "https://www.linkedin.com/in/ishan-bhatia-512aa0a2/"
    user.resume_url = "https://drive.google.com/file/d/1L4GttaKwM7z6b4MdX1AAMhaRZgW-1kfP/view"
    user.hackerrank_url = ""
    user.full_name = "Ishan Bhatia"
    user.summary = '''Passionate software engineer with 3+ years of experience in building scalable web applications and services.
        Competent in Python, FastAPI, Django, and cloud technologies like AWS and Docker.
        Adept at designing robust backend systems, optimizing performance, and implementing efficient algorithms.
        '''.strip()
    return user.save()
    
    
def clean_all():
    Certificate.objects.delete()
    School.objects.delete()
    Skill.objects.delete()
    WorkExperience.objects.delete()
    Project.objects.delete()
    ContactMessage.objects.delete()

def populate_all():
    from portfolio.mongo import connect_db
    connect_db()
    user = populate_user()
    populate_certificates(user)
    populate_schools(user)
    populate_skills(user)
    populate_work_experiences(user)
    populate_projects(user)
    populate_blog_post(user)


if __name__=='__main__':
    populate_all()