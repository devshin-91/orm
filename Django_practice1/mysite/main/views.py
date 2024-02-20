from django.shortcuts import render

# 블로그 글에 sample data
blog_data = [
    {
        "id": 1,
        "title": "첫 번째 글",
        "content": "첫 번째 글 내용입니다.",
    },
    {
        "id": 2,
        "title": "두 번째 글",
        "content": "두 번째 글 내용입니다.",
    },
    {
        "id": 3,
        "title": "세 번째 글",
        "content": "세 번째 글 내용입니다.",
    },
    {
        "id": 4,
        "title": "네 번째 글",
        "content": "네 번째 글 내용입니다.",
    },
]

# Create your views here.
def index(request):
    return render(request, "main/index.html")

def about(request):
    return render(request, "main/about.html")

def notice(request, pk):
    print(pk)
    print(blog_data[pk])
    return render(request, "notice.html")

def user(request, s):
    print(s)
    return render(request, "user.html")
'''
def notice_1(request):
    return render(request, "main/notice/1.html")

def notice_2(request):
    return render(request, "main/notice/2.html")

def notice_3(request):
    return render(request, "main/notice/3.html")
'''

'''
def contact(request):
    return render(request, "main/contact.html")

def atod(request):
    return render(request, "main/a/b/c/d.html")
'''


'''
def user_hojun(request):
    return render(request, "main/user/hojun.html")

def user_mini(request):
    return render(request, "main/user/mini.html")
'''