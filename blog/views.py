from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView,CreateView,UpdateView,DeleteView #추가
from .models import Post, Category, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.models import User

# Create your views here.
#함수 생성
def index(request):
    #db에서 query - select * from post
    posts1111 = Post.objects.all().order_by('-pk')
    categories = Category.objects.all()
    return render(request,
                  'blog/index.html',
                  context={'posts' : posts1111,
                           'categories' :categories
                           }
                 )
#/blog/category/<str:slug>/
#/blog/category/no_category
def category(request, slug):
    categories = Category.objects.all()
    if slug=='no_category':
        #미분류인경우
        posts= Post.objects.filter(category=None)
    else: # 내상세페이지?
        category = Category.objects.get(slug=slug)
        posts= Post.objects.filter(category=category)
    return render(request,
                  template_name='blog/index.html',
                  context={'posts': posts,
                           'categories': categories
                           }
                  )

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    categories = Category.objects.all()
    comments = Comment.objects.filter(post=post)
    commentform = CommentForm()
    return render(request,
                  'blog/detail.html',
                  context={'post':post,
                           'categories':categories,
                           'comments': comments,
                           'commentform': commentform,
                           })
'''
#댓글 전체 리스트 보기
def comment_list(request):
    comments = Comment.objects.all().order_by('-pk')
    return render(request, 'blog/detail.html', {'comments': comments})
'''

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

#/blog/<int:pk>/delete 이런경우글을삭제하겠다
def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('index')    #여기서인덱스는 블로그네임지정=인덱스로 해둔 그거(블로그/유알엘.파이에서 확인가능)
    #return render('/blog/')  이거랑동일함

#/blog/<int:pk>/update  -> pk는 post.pk
def update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        postform = PostForm(request.POST, request.FILES, instance=post)
        if postform.is_valid():
            postform.save()
            return redirect('/blog/')
    else:
        postform = PostForm(instance=post)
    return render(request,
                  template_name='blog/postupdateform.html',
                  context={'postform': postform}
                  )
#댓글작성
def createcomment(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            comment=commentform.save(commit=False)
            comment.author = User.objects.get(username='admin')
            comment.post = post
            comment.save()
            return redirect(f'/blog/{post.pk}/')


    return redirect(f'/blog/{post.pk}/')


#댓글수정
def updatecomment(request, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method=='POST':
        commentform= CommentForm(request.POST, instance=comment)
        if commentform.is_valid():
            commentform.save()
            return redirect(f'/blog/{comment.post.pk}/')
    else:
        commentform = CommentForm(instance=comment)

    return render(request,
                  template_name = 'blog/commentupdateform.html',
                  context = {'commentform': commentform}
                  )

#댓글삭제
def deletecomment(request, pk):
    comment= Comment.objects.get(pk=pk)

    comment.delete()
    return redirect(f'/blog/{comment.post.pk}/')


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