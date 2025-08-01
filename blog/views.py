from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm     #한줄추가. 뷰에서 폼을 임포트하기

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'blog/index.html',
        {
            'posts': posts,
        }
    )

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(
        request,
        'blog/detail.html',
        {
            'post': post,
        }
    )


#/blog/create/ 370p참고 이런 폼포스트인지포스트폼인지그냥폼인지만들기
@login_required  # 여기에 데코레이터 추가
def create(request):
    if request.method == 'POST':
        # form의 칸에 정보를 다 넣고, 제출 버튼을 누른경우.
        # 작성하다가 제출 버튼을 누른경우
        postform = PostForm(request.POST, request.FILES)
        if postform.is_valid():
            post1 = postform.save(commit=False)
            post1.title = post1.title + "이부분문장추가하면모든제목에이문장이추가됨"
            post1.author = request.user  #로그인한 유저를 아서필드에 자동할당
            post1.save()
            return redirect('/blog/')
            # 정상값인 경우
    else:  # get , 새글작성하기 버튼을 눌러서 create()함수로 들어온 경우
        postform = PostForm()
    return render(request,
                  template_name='blog/postform.html',
                  context={'postform': postform})

'''
if request.method == 'POST':
→ 사용자가 웹 폼에 내용을 입력하고, "제출" 버튼을 눌러서 서버에 데이터를 보낸 상황을 뜻해요.

postform = PostForm(request.POST, request.FILES)
→ 사용자 입력한 텍스트나 파일 데이터를 받아서 PostForm 폼 객체를 생성하는 부분입니다.
→ request.POST는 입력된 텍스트 데이터,
→ request.FILES는 첨부된 이미지나 파일 데이터입니다.

if postform.is_valid():
→ 폼에 입력된 데이터가 모두 올바른지(필수 입력, 글자 길이, 파일 형식 등) 검사하는 부분입니다.
→ 문제가 없으면 True, 그렇지 않으면 False가 됩니다.

post1 = postform.save(commit=False)
→ 폼 데이터를 바로 DB에 저장하지 말고, post1이라는 객체만 만들라는 뜻입니다.
→ 저장하기 전에 추가 작업(필드 수정 등)을 할 수 있도록 미뤄둔 거예요.

post1.title = post1.title + ""
→ 여기서는 제목에 빈 문자열을 더하는 코드인데, 보통은 이 부분에 원하는 문구를 덧붙이거나 가공하는 코드가 들어갑니다.
→ 예) "홍길동 만세"를 덧붙이거나 할 수 있어요.

post1.save()
→ 이제 post1 객체를 실제 데이터베이스에 저장합니다.

return redirect('/blog/')
→ 저장이 완료되면 글 목록 페이지(/blog/)로 이동시키는 코드입니다.

else: (GET 요청일 때)
→ 사용자가 처음 글쓰기 페이지에 들어왔을 때, 아무 입력도 없는 빈 폼을 만들어 보여줍니다.

return render(...)
→ 최종적으로 postform 폼 객체를 템플릿에 넘겨서 화면에 보여줍니다.
→ 사용자는 여기에 글을 쓰고 제출할 수 있습니다.

요약
코드 부분	의미
if request.method == 'POST':	폼 제출해서 데이터가 서버에 도착한 경우
PostForm(request.POST, request.FILES)	사용자가 입력한 데이터로 폼 객체 생성
is_valid()	입력 데이터 검증
save(commit=False)	DB 저장 전 객체 생성 (임시저장)
post1.title = ...	저장 전 데이터 수정 가능
post1.save()	DB에 실제 저장
redirect('/blog/')	저장 후 글 목록 페이지로 이동
else	폼을 처음 열었을 때 빈 폼 보여주기
render(...)	폼을 HTML 페이지에 렌더링해서 보여주기

'''