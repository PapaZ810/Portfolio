from page.models import *
from csv import reader


def fill_projects():
    with open('./scripts/projects.csv', mode='r', encoding='utf-8-sig') as file:
        for row in reader(file, delimiter=']'):
            _, created = Project.objects.update_or_create(
                title=row[0],
                image=row[1],
                short_description=row[2],
                text=row[3],
            )
            print(created)


def run():
    Home.objects.update_or_create(
        bio_text="""Hello! My name is Zoe, and I am a recent Computer Science graduate from Westminster University. 
        I have a huge penchant for problem solving and I love learning. 
        Computers and their intricacies are my passion, as I have been curious about them since I was 10 years old. 
        I built my first computer by myself from parts list to completion when I was 15 and started programming at 17."""
    )
    fill_projects()

    print("\033[1;32mDone!")
