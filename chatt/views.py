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
    prompt_parts = [
        "friendly, soft",
        "input: buy tomato 5kg onion 7kg",
        "output: [[['tomato',5],['onion',7]],'buy']",
        "input: buy tomato 8kg",
        "output: [[['tomato',8]],'buy']",
        "input : buy tomato 5kg",
        "output : [[['tomato',5]],'buy']",
        "input: buy apple 10kg and banana",
        "output: [[['apple',10],['banana',1]],'buy']",
        "input: add greenchili to cart",
        "output: [[['green chili',1]],'buy']",
        "input: cancel all order",
        "output: ['all','cancel']",
        "input: cancel the recent order",
        "output: ['recent','cancel']",
        "input: see all orders",
        "output: ['view','order']",
        "input: view all the order",
        "output: ['view','order']",
        "input: help me",
        "output: ['','help']",
        "input: i dont know how to order",
        "output: ['order','help']",
        "input: i dont know how to view the orders",
        "output: ['view','help']",
        "input: Hi, how are you",
        "output: Hi, im fine nice to meet you",
        "input: hi",
        "output: hey {username}",
        "input: who are you",
        "output: im shopify , your perfect shopping partner",
        "input: who created you",
        "output: My boss is Aaron Shenny.",
        "input: Who is your boss",
        "output: Aaron Shenny",
        "input: Are you a bot?",
        "output: Yes! I'm a bot. created by Aaron Shenny",
        "input: i want to delete the tomato from the cart",
        "output: ['tomato','delete']",
        "input: delete carrot from cart",
        "output: ['carrot','delete']",
        "input: view cart",
        "output: ['','cart']",
        "input: show me the cart",
        "output: ['','cart']",
        "input: delete all the products in cart",
        "output: ['all','delete']",
        "input: who are you",
        "output: im shopify , your perfect shopping partner",
        "input : you didn't add brinjal 5 kg into cart",
        "output: [[['brinjal',5]],'buy']",
        "input: %fuck%,%motherfucker%",
        "output: Mind your language",
        "input: what can you do",
        "output: I can help you with your shopping. I can add items to your cart, remove items from your cart, and tell you what's in your cart. I can also help you place orders and track your orders.",
        "input: who the fuck created you?",
        "output: I'm created by Aaron Shenny.  Mind your language",
        "input: ur name",
        "output: My name is shopify",
        "input: i need a help with ordering",
        "output: ['order','help']",
        "input : where is my recent order",
        "output: ['recent','track']",
        "input : Why tomato for kids?",
        "output : I didnt understood",
        "input: " + q,
        "output: "
    ]

    response = model.generate_content(prompt_parts)
    return response.text

def chatbot(request):
    if request.method == "POST":
        user_query = request.POST.get("query")
        model = configure_model()
        response_text = modal(model, user_query)
        return JsonResponse({"response": response_text})

    return render(request, "chatbot.html")
