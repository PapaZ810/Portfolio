# This file has been automatically generated.
# Instead of changing it, create a file called import_helper.py
# and put there a class called ImportHelper(object) in it.
#
# This class will be specially casted so that instead of extending object,
# it will actually extend the class BasicImportHelper()
#
# That means you just have to overload the methods you want to
# change, leaving the other ones intact.
#
# Something that you might want to do is use transactions, for example.
#
# Also, don't forget to add the necessary Django imports.
#
# This file was generated with the following command:
# C:\Users/capta/python/Portfolio\manage.py dumpscript page
#
# to restore it, run
# manage.py runscript module_name.this_script_name
#
# example: if manage.py is at ./manage.py
# and the script is at ./some_folder/some_script.py
# you must make sure ./some_folder/__init__.py exists
# and run  ./manage.py runscript some_folder.some_script
import os, sys
from django.db import transaction

class BasicImportHelper:

    def pre_import(self):
        pass

    @transaction.atomic
    def run_import(self, import_data):
        import_data()

    def post_import(self):
        pass

    def locate_similar(self, current_object, search_data):
        # You will probably want to call this method from save_or_locate()
        # Example:
        #   new_obj = self.locate_similar(the_obj, {"national_id": the_obj.national_id } )

        the_obj = current_object.__class__.objects.get(**search_data)
        return the_obj

    def locate_object(self, original_class, original_pk_name, the_class, pk_name, pk_value, obj_content):
        # You may change this function to do specific lookup for specific objects
        #
        # original_class class of the django orm's object that needs to be located
        # original_pk_name the primary key of original_class
        # the_class      parent class of original_class which contains obj_content
        # pk_name        the primary key of original_class
        # pk_value       value of the primary_key
        # obj_content    content of the object which was not exported.
        #
        # You should use obj_content to locate the object on the target db
        #
        # An example where original_class and the_class are different is
        # when original_class is Farmer and the_class is Person. The table
        # may refer to a Farmer but you will actually need to locate Person
        # in order to instantiate that Farmer
        #
        # Example:
        #   if the_class == SurveyResultFormat or the_class == SurveyType or the_class == SurveyState:
        #       pk_name="name"
        #       pk_value=obj_content[pk_name]
        #   if the_class == StaffGroup:
        #       pk_value=8

        search_data = { pk_name: pk_value }
        the_obj = the_class.objects.get(**search_data)
        #print(the_obj)
        return the_obj


    def save_or_locate(self, the_obj):
        # Change this if you want to locate the object in the database
        try:
            the_obj.save()
        except:
            print("---------------")
            print("Error saving the following object:")
            print(the_obj.__class__)
            print(" ")
            print(the_obj.__dict__)
            print(" ")
            print(the_obj)
            print(" ")
            print("---------------")

            raise
        return the_obj


importer = None
try:
    import import_helper
    # We need this so ImportHelper can extend BasicImportHelper, although import_helper.py
    # has no knowlodge of this class
    importer = type("DynamicImportHelper", (import_helper.ImportHelper, BasicImportHelper ) , {} )()
except ImportError as e:
    # From Python 3.3 we can check e.name - string match is for backward compatibility.
    if 'import_helper' in str(e):
        importer = BasicImportHelper()
    else:
        raise

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

try:
    import dateutil.parser
    from dateutil.tz import tzoffset
except ImportError:
    print("Please install python-dateutil")
    sys.exit(os.EX_USAGE)

def run():
    importer.pre_import()
    importer.run_import(import_data)
    importer.post_import()

def import_data():
    # Initial Imports

    # Processing model: page.models.Project

    from page.models import Project

    page_project_1 = Project()
    page_project_1.title = 'Minijava'
    page_project_1.image = 'Cast.png'
    page_project_1.short_description = 'A project in the compilers class that generated JVM assembly code.'
    page_project_1.text = 'Minijava was a project in the compilers class at Westminster University that had the students design and implement the front end of a compiler to take minijava code and convert it into Java virtual machine assembly so that a different program, jasmin, could convert it into a .class file. This .class file could then easily be run and the output from the program could be seen. I had a lot of fun with this project and learning about compilers in general, but it did require a lot of work to create. The project was broken up over the last two months of the semester, with the first two getting the basics down on how parsing, lexing and adding semantic actions worked both in Java and how we were going to write them for our project. Overall, I enjoyed seeing the incremental progress of putting this compiler together, getting more and more of it working. It was really great when I could first write a normal looking Java program and get it to compile with no errors. Having to figure out precisely how jasmin wanted the assembly code and implementing that into the generator was difficult but extremely rewarding.<br><br><img src="/static/images/cast.png" alt="A picture of the code required to cast integers to doubles and vice versa as well as from numbers to Strings" class="rounded-3"><hr>A picture of the code required to cast integers to doubles and vice versa as well as from numbers to Strings. The full extent of the code is linked in the section header.,'
    page_project_1 = importer.save_or_locate(page_project_1)

    page_project_2 = Project()
    page_project_2.title = 'JPEG Image Compression Script'
    page_project_2.image = 'House.png'
    page_project_2.short_description = 'A python script created for my Linear Algebra class final project.'
    page_project_2.text = 'This project started off as a final project for the Linear Algebra class at WU but evolved over the past couple of years to be much more streamlined in code style. Most of the work that I put into it was to make it faster, as it originally took over a minute to compress a 3.5MB file down to 800KB. I didn\'t have time to make it much faster and considered the task of multithreading the script to be quite daunting at the time, but after I presented my work to the class I gained a renewed energy to work on it that unfortunately didn\'t get very far. After that, I left it for over a year while I focused on other classwork, and in the Fall of 2023 I came back to it, with more experience and ideas for how to complete this. The first step was to see if there was any way to make my code any cleaner. In the first version there were a lot of nested for loops and I was curious if there were any ways to manipulate the arrays in place. And, of course, there were! Using these optimizations I was able to significantly improve the quality of the code, going from someone who only knew Java to a proper programmer. My main idea for making the program faster was to multithread it, using multiple different cores on the device to speed up the lengthy operations I was doing on the images. But after a lot of work on converting the script to use four threads, the script was slower to complete on the same image. I then made two more branches that used two and eight threads but they were still slower. I made a massive breakthrough when I learned about vectorized array operations, turning one of the last nested for loop functions into just two lines. Not only did this improve the look of the code, but it made the script run much faster, going from over a minute to compress that previously mentioned 3.5MB file to just 6 seconds. I still have some bugs to iron out, most notably that the Fourier conversion doesn\'t really work and it\'s the main part of the compression.\r\n<hr>\r\n<img src="/static/images/windows.png" alt="A picture showing the difference between the non-compressed picture and the compressed picture." class="rounded-3">\r\n<br>\r\n<br>\r\n<img src="/static/images/house.png" alt="Another picture showing the difference between the non-compressed picture and the compressed picture." class="rounded-3">'
    page_project_2 = importer.save_or_locate(page_project_2)

    page_project_3 = Project()
    page_project_3.title = 'ZenSpelling'
    page_project_3.image = 'zenspellinglogo.jpg'
    page_project_3.short_description = 'A spelling game that myself and some classmates made for our Software Engineering class.'
    page_project_3.text = 'ZenSpelling was a project myself and a few classmates completed as part of our class work in Software Engineering CMPT 322. It\'s a web-based spelling game for 1st-5th grade students to improve their spelling skills by building a garden. The game was built in Django using JQuery to transfer data to the frontend and p5.js to draw the canvas that holds the tiles on the game board. Students can track their progress in the game throught the profile screen and they can earn medals through exceptional gameplay. The game tracks the amount of time you played the game, how many questions you answer incorrectly and how many questions you answer correctly in a row and shows you all of those datapoints when you complete a game. It will also give the student medals based on those metrics after the game completes. It also saves the metrics to the database to be viewed by the student on the profile page and by the Teacher through the admin panel. I mainly worked on the database side of the game, but working in a team for this project got me to learn a lot about the AGILE process and about how effective communication can greatly improve productivity. \r\n<br>\r\n<hr>\r\nHere are some pictures from the game!\r\n<br>\r\n<br>\r\n<img alt="The login page of ZenSpelling" src="/static/images/ZenSpellingLogin.jpg" class="rounded-3 w-50">\r\n<br>\r\n<br>\r\nThe login page where all students are required to log in to the app to log all metrics to the database.\r\n<br>\r\n<br>\r\n<img alt="The profile page of ZenSpelling" src="/static/images/ZenSpellingProfile.jpg" class="rounded-3 w-50">\r\n<br>\r\n<br>\r\nThe profile page shows all of the metrics for the students so that they can track their progress. It also has a section for a planned feature that we never got to, saving the gardens from students\' games to their profile. We had planned it for a future release but never got to it.\r\n<br>\r\n<br>\r\n<img alt="The game setup page of ZenSpelling" src="/static/images/Setup.jpg" class="rounded-3 w-50">\r\n<br>\r\n<br>\r\nThe game setup page allows the student to customize their game how they want. The page offers different multiple different game board sizes and support for question sets. Question sets are a way for teachers to customize which questions the student receives to better augment their learning. It was also served as a way for students to focus on their worst words to spell them better, but that was also not automatically built in.\r\n<br>\r\n<br>\r\n<img src="/static/images/ZenSpellingGamePage.jpg" alt="The game page of ZenSpelling" class="rounded-3 w-50">\r\n<br>\r\n<br>\r\nThis is the game page where all the gameplay happens. Tiles are dragged from the left side of the screen onto the board and a question pops down from the top of the screen. Once the question is answered, a sound plays and according to whether or not the student got the question right. If they answer incorrectly, the tile that the student placed will change into a weed. The weed can be removed by clicking on it. This will pop up with another question and if that question is answered correctly, the weed will disapear. Once the allotted questions have been answered, the student is taken to the complete screen. The complete screen shows the metrics for the game that the student completed and any medals they earned.'
    page_project_3 = importer.save_or_locate(page_project_3)

    page_project_4 = Project()
    page_project_4.title = 'Chatroom'
    page_project_4.image = 'chatroom.jpg'
    page_project_4.short_description = 'This was the final project for the Networks class that I took in 2023.'
    page_project_4.text = 'Chatroom was a project from Greg\'s Network class in Fall of 2023. Chatroom was the final project in the class in which we as a class decided on a network protocol to implement with a chatroom server and client. Our professor started us out with a basic server and basic client GUI to give us a starting point. From there, we were to implement our protocol, and have our client communicate properly with that server. Our protocol allowed for public and private messaging, a command to list all users connected to the server and a command to tell the server that a user had left.  Implementing the protocol was quite simple and that would have been project done, but I had some ideas that I wanted to implement to make the user experience of the client just that much better. I wanted users to be able to graphically see which other users were connected to the chatroom at any time in a sidebar within the client, as well as clicking on any name in the sidebar to select the user they want to private message. This project was a group project, but because the core requirements for the class were already complete and I had time on my hands, I just completed the things I wanted myself. \r\n<hr>\r\n<img src="/static/images/chatroom.jpg" alt="A picture of the Chatroom client" class="rounded-3">\r\n<br>\r\n<br>\r\nIn the end, the app turned out to be a bit more usable than the other clients in the class, one of which was completely command line based as they did not see the extra files that were given to us by our professor, and I am very proud of the work that I did.'
    page_project_4 = importer.save_or_locate(page_project_4)

    page_project_5 = Project()
    page_project_5.title = 'JACL Client Website'
    page_project_5.image = 'homepage.jpg'
    page_project_5.short_description = 'Website client project in a Web Apps class completed while working with UX designers.'
    page_project_5.text = 'This was a project in the Web Development course at Westminster University. The class was about computer science students working with designers from the Communications class that was paired with ours. Over the course of 4 months we as developers learned the software we were going to be using and made a website for a real client. We had meetings with the client so that we could make the best website that we could for them. As developers we had to make decisions on what we could and could not do with the time we had in the class. It was overall an amazing experience working with people and getting a taste of what working in industry may be like in the future. \r\n\r\nOur specific project was working with the President of the SLC chapter of the Japanese American Citizen\'s League(JACL) to create a website for their online presence. At the point that we started working with them, they only had a facebook page. Our first step was to determine what the president wanted for the website. The president wanted most of the website to be editable by herself or a social media person without having to take the website down. This necessitated a large change from just sticking text into an HTML page. We had to make database entries for each page on the website that were editable through Django\'s admin panel. Our team worked great together on the things we were best at and I even made one of the pages myself. At that time, I really wasn\'t the most experienced with CSS, so creating something that worked well with differing screen sizes was a bit of a challenge. \r\n<hr>\r\n<img class="rounded-3 w-50" alt="The Join page of the website" src="/static/images/joinjacl.jpg">\r\n<br>\r\n<br>\r\nThis was the page I worked on. The circles are absolutely positioned and snap to the center when the screen size of the device the website is displayed on is too small. \r\n<br>\r\n<br>\r\n<img class="rounded-3" alt="The footer of the Join page" src="/static/images/joinfooter.jpg">\r\n<br>\r\n<br>\r\nHere is the bottom of the join page that contains a link to the official application form.\r\n<br>\r\n<br>\r\nSome of the other pages on the website include the home page which has a carousel of images from JACL SLC\'s recent events, a calendar page with most recent events at the top of the page, a statements page with editable statements and a mission and vision page which has the SLC Chapter\'s mission and vision.\r\n<hr>\r\n<div class="row-cols-auto">\r\n    <img class="rounded-3 m-3 w-75" alt="This is the homepage" src="/static/images/homepage.jpg">\r\n    <img class="rounded-3 m-3 w-75" alt="This is the upcoming events on the events page" src="/static/images/events.jpg">\r\n    <img class="rounded-3 m-3 w-75" alt="This is the calendar of the events page" src="/static/images/calendar.jpg">\r\n    <img class="rounded-3 m-3 w-75" alt="This is the statements page" src="/static/images/statements.jpg">\r\n    <img class="rounded-3 m-3 w-75" alt="This is the mission and vision page" src="/static/images/missionandvision.jpg">\r\n</div>'
    page_project_5 = importer.save_or_locate(page_project_5)

    # Processing model: page.models.Home

    from page.models import Home

    page_home_1 = Home()
    page_home_1.bio_text = 'Hello! My name is Zoe, and I am a recent Computer Science graduate from Westminster University. I have a huge penchant for problem solving and I love learning. Computers and their intricacies are my passion, as I have been curious about them since I was 10 years old. I built my first computer by myself from parts list to completion when I was 15 and started programming at 17.'
    page_home_1 = importer.save_or_locate(page_home_1)

    # Processing model: page.models.Skill

    from page.models import Skill

    page_skill_1 = Skill()
    page_skill_1.name = 'Java'
    page_skill_1.logo = 'java.png'
    page_skill_1.experience = 'Java is the first language that I learned and I have used it throughout my schooling.'
    page_skill_1 = importer.save_or_locate(page_skill_1)

    page_skill_2 = Skill()
    page_skill_2.name = 'Python'
    page_skill_2.logo = 'python.png'
    page_skill_2.experience = 'I was originally quite scared of Python but it has come to be one of my favorite languages.'
    page_skill_2 = importer.save_or_locate(page_skill_2)

    page_skill_3 = Skill()
    page_skill_3.name = 'C/C++'
    page_skill_3.logo = 'c.png'
    page_skill_3.experience = 'C/C++ is a language that I should spend more time with but is still quite enjoyable for me.'
    page_skill_3 = importer.save_or_locate(page_skill_3)

    page_skill_4 = Skill()
    page_skill_4.name = 'Django'
    page_skill_4.logo = 'django.png'
    page_skill_4.experience = 'Django has become an resource for me to build websites as I already had a foundation in python.'
    page_skill_4 = importer.save_or_locate(page_skill_4)

    page_skill_5 = Skill()
    page_skill_5.name = 'Git'
    page_skill_5.logo = 'git.png'
    page_skill_5.experience = "Git was one of the first tools I learned, but I didn't use it fully until I used it with a team."
    page_skill_5 = importer.save_or_locate(page_skill_5)

    page_skill_6 = Skill()
    page_skill_6.name = 'Github'
    page_skill_6.logo = 'github.png'
    page_skill_6.experience = 'Github was how I first interacted with any version control system and I have come a long way since.'
    page_skill_6 = importer.save_or_locate(page_skill_6)

    page_skill_7 = Skill()
    page_skill_7.name = 'Pytorch'
    page_skill_7.logo = 'pytorch.png'
    page_skill_7.experience = 'Pytorch was a tool I picked up for an AI class that I took in college. Super cool tool!'
    page_skill_7 = importer.save_or_locate(page_skill_7)

    page_skill_8 = Skill()
    page_skill_8.name = 'Antlr4'
    page_skill_8.logo = 'antlr4.png'
    page_skill_8.experience = 'Antlr was a tool I picked up so that I could make a compiler for a language similar to Java.'
    page_skill_8 = importer.save_or_locate(page_skill_8)