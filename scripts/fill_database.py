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
        bioText="Hello! My name is Zoe, and I am a recent Computer Science graduate from Westminster University."
    )
    fill_projects()

    print("\033[1;32mDone!")
