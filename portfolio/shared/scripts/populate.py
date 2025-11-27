from resume.model.certificate import Certificate
from resume.model.contact_message import ContactMessage
from resume.model.line_item import LineItem
from resume.model.school import School
from resume.model.skill import Skill
from resume.model.work_ex import WorkExperience
from resume.model.project import Project
from datetime import datetime

def populate_certificates():
    c1 = Certificate(
        name="Certified Kubernetes Administrator (CKA)",
        issuer="Cloud Native Computing Foundation",
        link="https://www.cncf.io/certification/cka/"
    )
    c1.save()
    c2 = Certificate(
        name="AWS Certified Solutions Architect – Associate",
        issuer="Amazon Web Services",
        link="https://aws.amazon.com/certification/solutions-architect-associate/"
    )
    c2.save()
    
def populate_schools():
    '''
        name = StringField(required=True, max_length=100)
    degree = StringField(default="")
    start_date = DateTimeField()
    end_date = DateTimeField()
    description = ListField(field=LineItem(), default=[])
    '''
    s1 = School(
        name="University of Example",
        degree="Bachelor of Science in Computer Science",
        start_date = datetime(2015, 8, 15),
        end_date = datetime(2019, 5, 20),
        description = []

    )
    s1.save()
    s2 = School(
        name="Example Institute of Technology",
        degree="Master of Science in Software Engineering",
        start_date = datetime(2020, 9, 1),
        end_date = datetime(2022, 6, 15),
        description = []
    )
    s2.save()


def populate_skills():
    s1 = Skill(name="Python", proficiency=9)
    s1.save()
    s2 = Skill(name="JavaScript", proficiency=8)
    s2.save()
    s3 = Skill(name="Docker", proficiency=8)
    s3.save()
    s4 = Skill(name="Kubernetes", proficiency=7)
    s4.save()

def populate_work_experiences():
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
            name="Developed RESTful APIs using Flask and Django.",
            description="Created scalable backend services for various applications.",
            link=[]
        ),
        LineItem.create(
            name="Implemented CI/CD pipelines using Jenkins and GitHub Actions.",
            description="Automated the deployment process to improve efficiency.",
            link=[]
        )

    ]
    w1 = WorkExperience(
        org="Tech Solutions Inc.",
        role="Software Engineer",
        start_date=datetime(2019, 6, 1),
        end_date=datetime(2021, 8, 31),
        description=desc1
    )
    w1.save()

    desc2 = [
        LineItem.create(
            name="Led a team of 5 engineers to deliver cloud-native applications.",
            description="Managed project timelines and ensured quality standards.",
            link=[]
        ),
        LineItem.create(
            name="Optimized application performance, reducing latency by 30%.",
            description="Implemented caching strategies and database optimizations.",
            link=[]
        )
    ]
    w2 = WorkExperience(
        org="Innovatech Corp.",
        role="Senior Software Engineer",
        start_date=datetime(2021, 9, 1),
        end_date=datetime(2024, 5, 31),
        description=desc2
    )
    w2.save()


def populate_projects():
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
            name="Developed a personal portfolio website using React and Node.js.",
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
        published_date=datetime(2022, 3, 15),
        description=d1,
        link="https://www.example.com/portfolio"
    )
    p1.save()
    d2 = [
        LineItem.create(
            name="Designed and developed a full-featured e-commerce platform.",
            description="Implemented user authentication, product management, and payment processing.",
            link=[]
        ),
        LineItem.create(
            name="Integrated third-party APIs for shipping and inventory management.",
            description="Enhanced functionality and streamlined operations.",
            link=[]
        )
    ]
    p2 = Project(
        name="E-commerce Platform",
        published_date=datetime(2023, 7, 10),
        description=d2,
        link="https://www.example.com/ecommerce"
    )
    p2.save()



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
    populate_certificates()
    populate_schools()
    populate_skills()
    populate_work_experiences()
    populate_projects()


if __name__=='__main__':
    populate_all()