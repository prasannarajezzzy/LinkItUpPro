from django.shortcuts import render, HttpResponse

import openai


openai.api_key = "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"


max_tokens = 1024

model_engine = "text-davinci-003"

def getResponse(prompt):


    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return  completion.choices[0].text


def index(request):
    context = {
        'name': 'prasanna'
    }
    return render(request, 'index.html', context)


def contact(request):
    return HttpResponse("Thsu s home")


def about(request):
    return HttpResponse("Thsu s home")


def login(request):

    return HttpResponse("Thsu s home")


def logout(request):
    return HttpResponse("Thsu s home")
