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
        "he Mar Thoma Public School is a dream come true of the Marthoma community in and around Ernakulam. Established in 1990 and run by the Mar Thoma Educational Society, the Senior Secondary School affiliated to CBSE, New Delhi, maintains the highest standard in curricular and co-curricular activities. The Society is registered under the Travancore Kochi Literary, Scientific and Charitable Society Act XIII of 1995. The school is managed by the Society and its elected representatives under the auspicious leadership of its Chief Patron (Diocesan Bishop) and Manager (a priest appointed by the Chief Patron).The school is situated in sylvan surroundings in Edachira, about 2 kilometers from Kakkanad Civil Station, and a kilometer from Info Park. The school has Science, Commerce and Humanities streams at +2 level. Specialized Counselors take care of the emotional and psychological growth of the pupils and special attention is given to adolescents by imparting life skill techniques.COURSESWe offer complete schooling from LKG to Std. XII. While English is the medium of instruction. Hindi, Malayalam and French can also be learnt as second and third languages. We have introduced Smart classes to bring about revolutionary change in the way the students learn in the classroom. Computer, Science and Mathematics Laboratories are fully equipped with state of art instruments and equipments. The school also has a well established Library. A comprehensive system with various co-curricular activities is adopted to bring out the latent abilities of the students. Scholastically weak students are assisted with special tuitions.ADDITIONAL STREAM FOR SENIOR SECONDARYMar Thoma Public School is one of the two schools in Kerala which has introduced Financial Marketing Management during the year 2007 – 2008 at +2 levels, in view of its present importance and futuristic scope.NON-SCHOLASTIC PURSUITSSchooling is complete only when its focus is widened from just acquiring knowledge to include development of character, emotional and social maturity, and life experiences and above all, attaining wisdom.Learning is made a natural and joyous experience when students are involved in planning and organizing various activities and projects both as groups and as individuals. Co – curricular activities include Sports, Music, Drawing, Dancing, Gardening, Yoga, Painting, Needlework and Quiz. Besides these Science Club, Maths Club, Cyber Club, Green Club, Literary Club, Fitness Club, Cookery Club, Reading Club, Personality Development and SEED Club help to bring out the hidden potentials and creativity of the students. These talents find expression in the periodic exhibitions held at the school, which further help to enhance the emotional intelligence of the learners. .A proper exposure to the realities of life is provided in the frequent study tours and field trips organized to create a sense of belonging in the students and to protect them from the onslaughts of the modern cosmetic culture. Stress is laid on augmenting the Emotional Quotient and Social Quotient of every student by encouraging participation in social work, team building and community living.GRADINGThe School follows Grading System from LKG to Class X, which encourages a child’s development in a stress – free environment. A continuous and comprehensive evaluation system has been adopted for assessing the progress of these children. This helps the little minds to grow in harmony unpolluted by the unhealthy atmosphere of threat and competition.",
        "input: Grading system",
        "output: Yes, Mar Thoma Public School follows a Grading System from LKG to Class X.",
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
