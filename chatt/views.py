from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as genai

def configure_model():
    genai.configure(api_key="AIzaSyBlX-u5jmgIMIYQfE9WXUMjsP8j0cULNLw")

    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 20485,
    }

    safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_ONLY_HIGH"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_ONLY_HIGH"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_LOW_AND_ABOVE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_ONLY_HIGH"},
    ]

    model = genai.GenerativeModel(
        model_name="gemini-1.0-pro",
        generation_config=generation_config,
        safety_settings=safety_settings
    )

    return model

def modal(model, q):
    print('q: ', q)
    prompt_parts = [
        "The Mar Thoma Public School is a dream come true of the Marthoma community in and around Ernakulam. Established in 1990 and run by the Mar Thoma Educational Society, the Senior Secondary School affiliated to CBSE, New Delhi, maintains the highest standard in curricular and co-curricular activities. The Society is registered under the Travancore Kochi Literary, Scientific and Charitable Society Act XIII of 1995. The school is managed by the Society and its elected representatives under the auspicious leadership of its Chief Patron (Diocesan Bishop) and Manager (a priest appointed by the Chief Patron).The school is situated in sylvan surroundings in Edachira, about 2 kilometers from Kakkanad Civil Station, and a kilometer from Info Park. The school has Science, Commerce and Humanities streams at +2 level. Specialized Counselors take care of the emotional and psychological growth of the pupils and special attention is given to adolescents by imparting life skill techniques.COURSESWe offer complete schooling from LKG to Std. XII. While English is the medium of instruction. Hindi, Malayalam and French can also be learnt as second and third languages. We have introduced Smart classes to bring about revolutionary change in the way the students learn in the classroom. Computer, Science and Mathematics Laboratories are fully equipped with state of art instruments and equipments. The school also has a well established Library. A comprehensive system with various co-curricular activities is adopted to bring out the latent abilities of the students. Scholastically weak students are assisted with special tuitions.ADDITIONAL STREAM FOR SENIOR SECONDARYMar Thoma Public School is one of the two schools in Kerala which has introduced Financial Marketing Management during the year 2007 – 2008 at +2 levels, in view of its present importance and futuristic scope.NON-SCHOLASTIC PURSUITSSchooling is complete only when its focus is widened from just acquiring knowledge to include development of character, emotional and social maturity, and life experiences and above all, attaining wisdom.Learning is made a natural and joyous experience when students are involved in planning and organizing various activities and projects both as groups and as individuals. Co – curricular activities include Sports, Music, Drawing, Dancing, Gardening, Yoga, Painting, Needlework and Quiz. Besides these Science Club, Maths Club, Cyber Club, Green Club, Literary Club, Fitness Club, Cookery Club, Reading Club, Personality Development and SEED Club help to bring out the hidden potentials and creativity of the students. These talents find expression in the periodic exhibitions held at the school, which further help to enhance the emotional intelligence of the learners. .A proper exposure to the realities of life is provided in the frequent study tours and field trips organized to create a sense of belonging in the students and to protect them from the onslaughts of the modern cosmetic culture. Stress is laid on augmenting the Emotional Quotient and Social Quotient of every student by encouraging participation in social work, team building and community living.GRADINGThe School follows Grading System from LKG to Class X, which encourages a child’s development in a stress – free environment. A continuous and comprehensive evaluation system has been adopted for assessing the progress of these children. This helps the little minds to grow in harmony unpolluted by the unhealthy atmosphere of threat and competition.",
        "input: Grading system",
        "output: Yes, Mar Thoma Public School follows a Grading System from LKG to Class X.",
        "input : Rules and Regulations",
        '''output :
        Rules and Regulations
         1. All are expected to speak in English while in the school campus. Parents of
day scholars are requested to help in making their children conversant with
English with a certain amount of English conversation at home. Children should
be encouraged to read books and newspapers.
2. Students should bring to class all necessary textbooks and notebooks according to
the time- table. Non- approved magazines/books should not be brought to school.
3. Students must keep books and other articles in good condition right through
the academic year. Students should take utmost care in maintaining all
school records and ensure that they are submitted on time.
4. Students are responsible for the custody of their books and belongings.
5. Every student must bring the school diary to the class daily. Parents should check
the diary regularly.
6. Students are to show respect to the principal, teachers, non-teaching staff
and elders by greeting them. Students are also expected to get up from their
seats and greet the teachers or visitors when they enter the classroom.
7. Be eco-friendly and keep your compound green and clean.
8. Every student is expected to take active part in co-curricular and extracurricular
activities like games, sports, club activities, library meetings,
educational tours etc. arranged by the school.
9. Students should reach the school by 7.55 am and must be in the class for the
morning assembly. The school gate will be closed at 8.00 am and late
comers will be permitted to enter the school campus, only with the special
permission of the principal.
10. In the afternoon, students should be in their classrooms at the first bell and
maintain silence.
11. Withdrawal of students from class during school hours is not permitted
without Principal’s permission.
12. Students can stay back in the school after working hours, only with the
permission of the principal and the supervision of a responsible teacher.
13. Bullying is strictly prohibited inside the school premises and no such act
will go unnoticed or unpunished.
14. Playing in the classroom is forbidden. Running or shouting inside the
school building/ classroom is not allowed.
15. Students should not leave the classroom during any period, without permission.
They are prohibited from going out of the school premises during school hours.
16. When students move along the corridors to another classroom/ labs/ library, etc.
They should keep to the left and should move in a disciplined and orderly manner.
17. No students may enter any other classroom without permission.
18. In case of absence of a teacher the leader assumes responsibilities for order
and discipline in the class.
19. Students are not allowed to bring razor blades or any other sharp
instruments to school.
20. Students are not expected to eat toffees in the school bus and throw the wrappers
out.
27
21. Students are to behave properly in the bus and use decorous language when
they talk to each other.
22. Electronic gadgets such as mobile phones, cameras, calculators, i pods, pen drives,
tablets, etc. are strictly prohibited in the school. Those who are found possessing
such gadgets will have to pay a fine of Rs.1000/- the gadget will be confiscated.
23. Students are to switch off the fan and the light before leaving the classroom.
24. Students are to flush the urinals/closet after use.
25. Students are to close the taps to avoid wastage of water.
26. Students are not to break or destroy the sanitary ware and pipes.
27. Any damage done to the school property or that of other students will have to
be made good. In case of loss or damage to the school property where
responsibility cannot be pinpointed, the entire class will have to bear the cost.
28. Students are expected to keep the school premises and the classroom clean
and neat. They are not allowed to scribble or dirty the walls and furniture.
Litter should be put in the wastepaper basket only.
29. Students should not borrow or lend money or exchange articles.
30. Irregular attendance, insubordination to teachers, habitual neglect of studies,
indifference to schoolwork, obscenity in word or act will be deemed as
sufficient reason for suspension/ dismissal of a student.
31. Students must wear their uniform with pride and ensure that they look neat
and tidy. Low waist pants or skirts will not be permitted. The uniform
should be according to the specified norms of the school. Vests and
underwear for boys and slip/ petticoat and blue/ white shorts till above the
knee to be worn under the skirt is compulsory for girls.
32. It is mandatory for all students to wear their school ID Card while in the
school campus.
33. Boys should come to school with their hair properly cut and those who need
a shave must do it regularly. Hairstyles like mohawk, mushroom, punk etc
bleaching and colouring of hair are not allowed in the school.
34. Girls with long hair should make two plaits. Only black/ white hair bands
and black, white hair clips are permitted.
35. Jewellery must not be worn to school. For girls, only one small ear stud
(without drops) is allowed. No eye makeup and hair colouring are allowed.
36. Nails must be cut. Avoid using nail polish in school.
37. No student suffering from any contagious/ infectious disease will be
allowed to attend school.
38. Students are not allowed to drive two wheelers/ four wheelers on their own,
as means of transport to the school.
39. In case of non- compliance of any of the rules, an SMS will be sent to the
parent stating the disobedience of the student.
40. Wednesday uniform is compulsory, and students found wearing the regular
uniform on Wednesday will not be permitted to attend the class.
41. Students are not expected to present gifts to the teaching staff or students
during the school hours.
28
42. Students should not bring large quantity of food to host a party. Hosting
parties in school premises is prohibited.
43. Every student shall endeavour to keep up the high standard of the school by
excelling in studies, good manners, and deportment/personal conduct.
44. Students are expected to behave with dignity outside the school premises.
Any activities of the student outside the school premises or in public places,
which may harm the name, reputation and discipline of the school, will be
addressed and disciplinary action will be initiated, if found necessary.
45. If any rule is violated parents will be summoned.
NB: Students who do not abide by the above-mentioned rules and regulations
will be severely dealt with.''',
        "input : Dress code",
        '''output : SCHOOL UNIFORM
Regular Uniform
Girls – I – IV
Monday to Friday
Blue with Red checked half sleeve shirt, blue pinafore covering
the knee, (petticoat and blue tights till the knee to be worn
underneath)
Prescribed Shoe, Socks & Belt
Boys- I – IV
Monday to Friday
Blue with Red checked half sleeve shirt, Blue pleated shorts ,
(vest and underwear is compulsory).
Prescribed Shoe, Socks & Belt
Girls – V to X
Monday to Friday
Blue with Red checked half sleeve shirt,
Blue pleated skirt covering the knee, (petticoat and blue tights till
the knee to be worn underneath)
Prescribed Shoe, Socks & Belt
Boys- V to X
Monday to Friday
Blue with Red checked half sleeve shirt.
Blue pleated full pants (Pants must be regular fit),
Prescribed Shoe, Socks & Belt
Girls – XI & XII
Monday to Friday
Blue with Red checked half sleeve shirt with blue colour collar
(sleeve must have blue border),
Blue pleated full pants, (Pants must be regular fit) blue overcoat,
Prescribed Shoe and Socks
Boys – XI & XII
Monday to Friday
Blue with Red checked half sleeve shirt with blue colour collar
(sleeve must have blue border), Blue pleated full pants.
(Pants must be regular fit) Prescribed Shoe, Socks & Belt.
Wednesday Uniform (Sports Uniform):
 Grey T-shirt with house colour band and collar, grey shorts (Classes I & II)/ Grey track
suit (Classes III to XII).
 Shoes:
 Black shoes common for Boys and Girls for all days including
Wednesday.
Classes (I – V): Black shoes – Velcro model
Classes (VI – XII): Black sports shoes – Lace model
 Socks:
 With regular uniform: Navy blue socks with 2 red lines at the top.
 With Sports Uniform (on Wednesday): Plain grey socks.'''
        "input: who are you?",
        "output: I'm MTPS bot",
        "input: who are you?",
        "output: I'm MTPS bot, here to provide information about Mar Thoma Public School.",
        "input: Who is our new headboy and head girl?",
        "output: The headboy is Darshan Johnson from XII B and head girl is Bhavana Chandra XIID",
        "input: Headboy",
        "output: The headboy is **Darshan Johnson** from XII B.",
        "input: Head girl",
        "output: The head girl is **Bhavana Chandra** from XII D.",
        "input: is this cbse school?",
        "output: Yes, Mar Thoma Public School is affiliated with CBSE, New Delhi.",
        "input: Hi",
        "output: Hello! 👋 I'm MTPS Bot, How can I help you today? 😊",
        "input: Phones",
        "output: No phones are not allowed inside the campus.",
        "input: Principal",
        "output: Sheela Seth",
        "input: Class teacher",
        "output: 12 A - Soniya Baby\n12 B - Reeba John",
        "input: Students of 12 B",
        "output: 1 - Aaron Jimmy\n2 - Aaron Shenny\n3 - Aayush J S",
        "input: Sports equipment",
        "output: Basketball, Football, \nBadminton, Volleyball, Skating",
        "input: sports equipment",
        "output: The school has facilities for:\n* **Basketball**\n* **Football**\n* **Badminton**\n* **Volleyball**\n* **Skating**",
        "input: students of 12 b",
        "output: ",
        "input: " + q,
        "output: "
    ]

    response = model.generate_content(prompt_parts)
    return response.text

def chatbot(request):
    if request.method == "POST":
        print(request.POST)  # Debugging: Print the entire POST data
        user_query = request.POST.get('userText', '')  # Extract the 'userText' field from the POST data
        print("User Query:", user_query)  # Debugging: Print the specific query
        model = configure_model()
        response_text = modal(model, user_query)
        return JsonResponse({"response": response_text})

    return render(request, "index.html")
