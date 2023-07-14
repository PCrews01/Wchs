from flask import Blueprint, render_template, request, flash, url_for, redirect
from flask_login import login_required, current_user
from .models import *
from website import DB
from base64 import b64encode
from lorem_text import lorem
import json
import random
views = Blueprint('views', __name__)

def randomText(length, v):
	if v == "paragraphs":
		return lorem.paragraphs(length)
	elif v == "words":
		return lorem.words(length)
	elif v == "sentence":
		return lorem.sentence()
	return lorem.sentence()

def getImage(img):
	return url_for('static', filename=f"images/{img}.jpg")


def_arti_img  = "protest"

new_article = Article
news_stories = [
		new_article(
			id=0,
		title="Starter Article", 
		story=randomText(3, "paragraphs"), 
		headline=randomText(1, "sentence"), 
		date="06/18/2023", 
		author="Paul Crews", 
		image="Dance1", 
		category="test", 
		tags="test,school,articles", 
		lead_story=True),

		new_article(
			id=1,
		title="Second Starter Article", 
		story=randomText(6, "paragraphs"), 
		headline=randomText(1, "sentence"), 
		date="06/18/2023", 
		author="Paul Crews", 
		image="protest", 
		category="test", 
		tags="test,school,articles", 
		lead_story=True),

		new_article(
			id=2,
		title="Another Starter Article", 
		story=randomText(2, "paragraphs"), 
		headline=randomText(1, "sentences"), 
		date="06/18/2023", 
		author="Paul Crews", 
		image="science", 
		category="test", 
		tags="test,school,articles", 
		lead_story=True),

		new_article(
			id=3,
		title="Last Starter Article", 
		story=randomText(3, "paragraphs"), 
		headline=randomText(1, "sentences"), 
		date="06/18/2023", 
		author="Paul Crews", 
		image="championship", 
		category="test", 
		tags="test,school,articles", 
		lead_story=True)
	]

def changeArticleImg(img):
	def_arti_img = img

@views.route('/', methods=['GET', 'POST'])
def home():
	return render_template('home.html', user=current_user, articles=news_stories, get_image=getImage, random_text=randomText, news_img=def_arti_img, img_changer=changeArticleImg, e=enumerate(news_stories))

@views.route('/academics', methods=['GET', 'POST'])
def academics():
	# CREATE ACADEMICS USING THE 'ACADEMICS' MODEL
	art = Academics()
	biology = Academics()
	chemistry = Academics()
	computer_science = Academics()
	english = Academics()
	health = Academics()
	physical_education = Academics()
	mathematics = Academics()
	music = Academics()
	physics = Academics()
	social_studies = Academics()
	special_education = Academics()

	# CREATE SPORTS OBJECTS USING THE 'SPORT' MODEL
	boys_basketball = Sport()
	boys_football = Sport()
	boys_baseball = Sport()
	boys_soccer = Sport()
	girls_volleyball = Sport()
	girls_softball = Sport()
	girls_soccer = Sport()
	
	# ASSIGN STATIC DATA TO EACH ACADEMIC FOR DISPLAY PURPOSES
	art.staff = 3
	art.students = 300
	art.title = "Art"
	art.blurb = randomText(1, "paragraphs")

	biology.staff = 4
	biology.students = 10
	biology.title = "Biology"
	biology.blurb = randomText(2, "paragraphs")

	chemistry.staff = 2
	chemistry.students = 50
	chemistry.title = "Chemistry"
	chemistry.blurb = randomText(2, "paragraphs")

	computer_science.staff = 2
	computer_science.students = 50
	computer_science.title = "Computer Science"
	computer_science.blurb = randomText(2, "paragraphs")

	english.staff = 10
	english.students = 20
	english.title = "English"
	english.blurb = randomText(2, "paragraphs")

	health.staff = 2
	health.students = 40
	health.title = "Health"
	health.blurb = randomText(2, "paragraphs")

	physical_education.staff = 3
	physical_education.students = 300
	physical_education.title = "Physical Education"
	physical_education.blurb = randomText(2, "paragraphs")

	mathematics.staff = 3
	mathematics.students = 200
	mathematics.title = "Mathematics"
	mathematics.blurb = randomText(2, "paragraphs")

	music.staff = 1
	music.students = 30
	music.title = "Music"
	music.blurb = randomText(2, "paragraphs")

	physics.staff = 2
	physics.students = 210
	physics.title = "Physics"
	physics.blurb = randomText(2, "paragraphs")

	social_studies.staff = 2
	social_studies.students = 100
	social_studies.title = "Social Studies"
	social_studies.blurb = randomText(2, "paragraphs")

	special_education.staff = 2
	special_education.students = 20
	special_education.title = "Special Education"
	special_education.blurb = randomText(2, "paragraphs")

	# CREATE AN ARRAY OF ACADEMICS
	academics = [
		art,
		biology,
		chemistry,
		computer_science,
		english,
		health,
		physical_education,
		mathematics,
		music,
		physics,
		social_studies,
		special_education

	]

	# ASSIGN STATIC DATA TO EACH SPORT FOR DISPLAY PURPOSES
	boys_baseball.championships = 2
	boys_baseball.coach = "Mr. Coach"
	boys_baseball.losses = 0
	boys_baseball.sport = "Boys Baseball"
	boys_baseball.ties = 0
	boys_baseball.winning_years = "2021, 2022"
	boys_baseball.wins = 38

	boys_basketball.championships = 3
	boys_basketball.coach = "Mr. Coach"
	boys_basketball.losses = 0
	boys_basketball.sport = "Boys Basketball"
	boys_basketball.ties = 0
	boys_basketball.winning_years = "2020, 2021, 2022"
	boys_basketball.wins = 41

	boys_football.championships = 1
	boys_football.coach = "Mr. Coach"
	boys_football.losses = 3
	boys_football.sport = "Boys Flag Football"
	boys_football.ties = 0
	boys_football.winning_years = "2022"
	boys_football.wins = 5

	boys_soccer.championships = 2
	boys_soccer.coach = "Mrs. Coach"
	boys_soccer.losses = 0
	boys_soccer.sport = "Girls Soccer"
	boys_soccer.ties = 2
	boys_soccer.winning_years = "2012, 2022"
	boys_soccer.wins = 13

	girls_soccer.championships = 2
	girls_soccer.coach = "Mrs. Coach"
	girls_soccer.losses = 0
	girls_soccer.sport = "Girls Soccer"
	girls_soccer.ties = 2
	girls_soccer.winning_years = "2012, 2022"
	girls_soccer.wins = 13

	girls_softball.championships = 1
	girls_softball.coach = "Mrs. Coach"
	girls_softball.losses = 3
	girls_softball.sport = "Girls Softball"
	girls_softball.ties = 0
	girls_softball.winning_years = "2021"
	girls_softball.wins = 15

	girls_volleyball.championships = 4
	girls_volleyball.coach = "Mrs. Coach"
	girls_volleyball.losses = 0
	girls_volleyball.sport = "Girls Volleyball"
	girls_volleyball.ties = 0
	girls_volleyball.winning_years = "2019, 2020, 2021, 2022"
	girls_volleyball.wins = 19

	# CREATE AN ARRAY OF SPORTS
	sports = [
		boys_baseball,
		boys_basketball,
		boys_football,
		boys_soccer,
		girls_soccer,
		girls_softball,
		girls_volleyball
	]

	rows = len(academics) / 3

	return render_template('pages/academics.html', sports=sports, academics=academics, e=enumerate(academics), rows=rows)

@views.route('/academic/<section>')
def academic(section):

	return render_template('pages/academic.html', section=section)

@views.route('/our-story')
def ourStory():
	bg = url_for('static', filename='images/backgrounds/building.jpg')
	story = [
		"Williamsburg Charter High School (WCHS) stands as an extraordinary institution that has garnered widespread recognition for its exceptional contributions to the world of music production and artistry. With a rich history of cultivating and nurturing budding talent, WCHS has emerged as a veritable breeding ground for future music producers and artists. Through its comprehensive music program, this illustrious institution has equipped students with the skills, knowledge, and opportunities necessary to excel in the competitive music industry. From Grammy-winning music producers to chart-topping artists, the impressive roster of successful alumni is a testament to the school's unwavering commitment to musical excellence.",
		"Moreover, WCHS has not only flourished in the realm of music but has also achieved remarkable success in various athletic arenas. The school's championship-winning legacy is a testament to its dedication to fostering a spirit of sportsmanship, teamwork, and relentless pursuit of greatness. From exhilarating victories on the basketball court to triumphant moments on the soccer field, WCHS has consistently demonstrated its ability to produce well-rounded individuals capable of excelling both academically and athletically. These achievements not only inspire current students but also reflect the profound impact of the school's comprehensive approach to education.",
		"Beyond its extraordinary track record of producing successful musicians and athletes, WCHS takes immense pride in its commitment to shaping the future workforce. The school recognizes the importance of equipping students with the necessary skills and knowledge to thrive in their chosen professions. By providing a rigorous academic curriculum and fostering a supportive learning environment, WCHS empowers its students to transform their aspirations into reality. The school's alumni, who have seamlessly transitioned from being students to esteemed professionals in various fields, serve as living testaments to the transformative power of a WCHS education.",
		"In addition to its outstanding music program and remarkable academic achievements, WCHS prides itself on fostering a vibrant and inclusive community. With a diverse student body and dedicated staff, the school celebrates the richness of different cultures, perspectives, and backgrounds. This diversity not only enhances the learning experience but also prepares students for the interconnected global society they will encounter beyond the school's walls. At WCHS, students are encouraged to embrace their unique identities and appreciate the value of cultural exchange, resulting in a truly enriching educational environment.",
		"In conclusion, Williamsburg Charter High School's illustrious reputation extends far beyond its outstanding music program and championship wins. With an unwavering dedication to nurturing talent, fostering academic and athletic excellence, and promoting diversity and inclusion, WCHS continues to shape the lives of its students and contribute to society at large. By combining a passion for the arts with a commitment to education, WCHS stands as a beacon of inspiration and a testament to the transformative power of a holistic and inclusive approach to learning."
	]

	return render_template('pages/our_story.html', story_paragraphs=story,bg=bg)

@views.route('/student-life')
def studentLife():
	voice = [
		"In recent times, the power of student voices has risen to the forefront of societal consciousness. Today, more than ever, young individuals are harnessing their collective strength to address critical issues that directly affect their lives. An exemplar of this phenomenon is the resolute stance taken by our students against the pervasive problem of gun violence. With unwavering determination, these impassioned advocates have amplified their concerns, ultimately converging on the doors of Gracie Manor in order to convey their persuasive arguments and demand change.",
		"The students' decision to protest gun violence stems from a genuine concern for their safety and the well-being of their peers. Recognizing the urgent need for reform in our nation's gun laws, these resilient young individuals have employed their voices as powerful tools to advocate for meaningful action. Their resounding calls for stricter gun control measures and enhanced safety protocols in schools have reverberated across communities, sparking a national conversation and compelling authorities to acknowledge the gravity of the issue at hand.",
		"Taking their activism to the highest echelons of power, our students have valiantly embarked on a journey to Gracie Manor, where they have sought to captivate the attention of key decision-makers. Armed not with weapons, but with compelling arguments backed by heartfelt conviction, these young activists have sought to engage in a constructive dialogue with policymakers. Their courageous act of holding those in power accountable and demanding change demonstrates the tremendous potential of the student voice in shaping a better future.",
		"In conclusion, our students have emerged as the vanguards of change, bravely confronting the scourge of gun violence through their collective voice and unwavering determination. Their peaceful protests and articulate arguments have cast a spotlight on an issue that affects not only their lives but also the lives of countless others. As high school seniors, these young advocates have displayed a level of civic engagement and activism that is both inspiring and consequential. By bringing their concerns to Gracie Manor, they have demonstrated the indomitable power of the student voice and its ability to effect positive change in society."
	]
	dance = [
		"The dance program at Williamsburg Charter High School (WCHS) is a shining example of the school's unwavering dedication to nurturing artistic talent and fostering a vibrant creative community. As a college senior, The school immense pride in boasting about WCHS's exceptional dance program, which offers a transformative experience that goes far beyond the confines of the classroom. From comprehensive training to collaborative performances, WCHS provides a platform for aspiring dancers to flourish and realize their full potential.",
		"Central to the success of the WCHS dance program is a team of experienced and passionate instructors. These dedicated professionals bring a wealth of knowledge and expertise to the studio, nurturing students' technical proficiency and inspiring their artistic growth. Their commitment to each dancer's development goes beyond imparting technical skills; they instill discipline, resilience, and a deep appreciation for the art form. Under their guidance, WCHS dancers are empowered to explore their unique artistic voices and excel in their chosen styles of dance.",
		"The WCHS dance program offers students an array of performance opportunities that showcase their talents to the broader community. From annual recitals to collaborative productions, dancers at WCHS have the privilege of sharing their artistry with peers, faculty, and family members. These performances not only provide a platform for self-expression but also foster a sense of community and camaraderie among the dancers. Through their captivating performances, WCHS dancers captivate audiences and leave a lasting impact, further cementing the school's reputation for excellence in dance.",
		"In conclusion, the dance program at Williamsburg Charter High School is a testament to the school's commitment to fostering artistic expression and nurturing the next generation of dancers. With dedicated instructors and a multitude of performance opportunities, WCHS dancers receive a comprehensive education that prepares them for success in the dance world and beyond. As a college senior, The WCHS dance program, as it has not only honed many skills but also shaped students into confident and passionate artists."
	]
	music = [
		"The music program at Williamsburg Charter High School (WCHS) is a true gem, standing as a testament to the school's unwavering commitment to artistic excellence and the power of musical expression. As a college senior, WCHS's exceptional music program, which offers a transformative experience that transcends the confines of traditional education. From comprehensive training to awe-inspiring performances, WCHS provides a platform for aspiring musicians to flourish and cultivate their passion for music.",
		"At the core of WCHS's music program is a team of dedicated and accomplished instructors who serve as mentors and guides. These talented professionals bring a wealth of knowledge and expertise to the classroom, inspiring students to unlock their musical potential and pursue their dreams. Their unwavering support and personalized instruction foster an environment where creativity and growth thrive. Under their guidance, WCHS musicians not only develop technical proficiency but also gain a deep understanding of music theory, history, and performance practices.",
		"One of the hallmarks of the WCHS music program is the plethora of performance opportunities available to students. From concerts and recitals to competitions and community events, WCHS musicians have the privilege of showcasing their talents to diverse audiences. These performances not only serve as a testament to the hard work and dedication of the students but also foster a sense of unity and pride within the WCHS community. The transformative power of music becomes palpable as the musicians captivate listeners, convey emotions, and create unforgettable moments through their exceptional performances.",
		"In conclusion, the music program at Williamsburg Charter High School is a shining example of the school's commitment to fostering artistic growth and providing a comprehensive musical education. With a team of dedicated instructors and a wealth of performance opportunities, WCHS musicians are empowered to explore their artistic voices, develop technical proficiency, and cultivate a deep love for music. It has undoubtedly prepared many kids for a future filled with endless possibilities in the world of music."
	]
	theater = [
		"The theater department at Williamsburg Charter High School (WCHS) is a beacon of artistic brilliance, representing the school's unwavering commitment to the transformative power of storytelling and stagecraft. WCHS's exceptional theater department, which offers an immersive experience that nurtures creativity, hones performance skills, and fosters a deep appreciation for the dramatic arts. At the forefront of this extraordinary program is the much-anticipated 2023 production of 'Little Shop of Horrors,' which exemplifies the department's dedication to delivering unforgettable theatrical experiences.",
		"Led by a team of passionate and experienced theater professionals, the WCHS theater department provides students with comprehensive training in acting, directing, stage design, and all facets of theater production. These dedicated instructors serve as mentors, guiding students through a curriculum that emphasizes artistic growth, teamwork, and innovation. They inspire young performers to delve deep into their characters, master their craft, and fearlessly explore the boundaries of their own creativity.",
"The highlight of the WCHS theater department's calendar is undoubtedly the 2023 production of 'Little Shop of Horrors.' This iconic musical, known for its infectious music, dark humor, and unforgettable characters, will showcase the immense talent and hard work of WCHS students. From auditions to rehearsals, the production of 'Little Shop of Horrors' serves as a platform for students to showcase their acting, singing, and dancing abilities. With meticulous attention to detail in set design, costume creation, and technical execution, the department will create a visually stunning and emotionally captivating theatrical experience that will leave audiences in awe.",
"In conclusion, the theater department at Williamsburg Charter High School is a testament to the school's dedication to nurturing the next generation of performers and theater enthusiasts. With a team of passionate instructors and a commitment to delivering exceptional productions, WCHS offers students an immersive and transformative theatrical journey. The 2023 production of 'Little Shop of Horrors' stands as a shining example of the department's commitment to excellence and promises to be an unforgettable theatrical experience for both the performers and the audience. The school immensely proud of the theater department's accomplishments and the lasting impact it has had on the students' artistic journey."
	]
	return render_template('pages/student_life.html', music=music,theater=theater,voice=voice,dance=dance)

@views.route('/contact')
def contact():
	return render_template('pages/contact.html')

@views.route('/news/<article>')
def articles(article):
	selection = news_stories[int(article)]
	return render_template('pages/article.html', article=selection, user=current_user, get_image=getImage, id=int(article), count=len(news_stories))

@views.route('/news')
def news():
	return render_template('pages/news.html',articles=enumerate(news_stories), user=current_user, get_image=getImage)

@views.route('/parent-center')
def parentCenter():

	return render_template('pages/parent_center.html')

@views.route('/student-center')
def studentCenter():

	return render_template('pages/student_center.html')

@views.route('/contact/admissions')
def admissions():

	return render_template('pages/contact/admissions.html')