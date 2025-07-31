from django.shortcuts import render
from .models import Post   	#한줄추가. Post 모델 임포트하는 과정

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-pk')	#한줄추가. 인덱스함수에서 Post.objects.all()로 모든 Post 레코드를 가져와서 posts에 저장

    return render(
	request,
	'blog/index.html',
        {
        	'posts': posts,  # { 'posts': posts, } 추가하기
        }
)
