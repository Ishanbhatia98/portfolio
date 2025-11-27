from django.shortcuts import render



# home page
# matrix style - red pill / blue pill
# download cv button
# -- or --
# play game button - game about life events

# education
# work
# projects(currently hidden)
# connect with me page

# linkedin, leetcode, codechef,
# hackerrank, github, codefoces(hidden)



def home_view(request):
    context = {"data": "Gfg is the best"}
    return render(request, "home.html", context)

def check_age(request):
    age = None
    if request.method == 'POST':
        age = int(request.POST.get('age', 0))
    return render(request, 'projects.html', {'age': age})

def loop(request):
    data = "Gfg is the best"
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    context = {
        "data": data,
        "list": number_list
    }
    return render(request, "work_experience.html", context)