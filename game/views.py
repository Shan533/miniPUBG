from django.http import HttpResponse


def index(request):
    line1 = '<h1 style="text-align: center">Hello, Aaron</h1>'
    line2 = '<img src= "https://labuget.ro/wp-content/uploads/2018/06/pubg.jpg">'
    line3 = '<hr>'
    line4 = '<a href="play/">START GAME</a>'
    return HttpResponse(line1 + line4 + line3 + line2)

def play(request):
    line1 = '<h1 style = "text-align: center">YOU DIE!</h1>'
    line2 = '<img src= "https://img4.18183.com/uploads/allimg/180111/88-1P111151448-50.jpg@q_80">'
    return HttpResponse(line1 + line2)
