from django.shortcuts import render

# Create your views here.

def index(req):
    context = {
        #빈 값
    }

    return render(req, 'index.html', context=context) 
    #index 뷰 처리 요청 들어오면 index.html 페이지로 처리해서 브라우저에 넘길 것 