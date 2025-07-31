from django.contrib import admin
# 이 밑에 2줄을 적는다
from .models import Post

admin.site.register(Post)

#해당 두 줄은 관리자페이지에 포스트 모델을 등록하는 과정임!
