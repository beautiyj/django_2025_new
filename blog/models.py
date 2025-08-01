# Post 모델은 models 모듈의 Model 클래스를 확장해서 만든 파이썬 클래스.
from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100, unique=True, allow_unicode=True)

	def get_url(self):
		return f'/blog/category/{self.slug}/'

	def __str__(self):
		return f'{self.name}----{self.slug}'

class Post(models.Model) :
	title = models.CharField(max_length=30)    # title 필드는 CharField (문자열필드정의 클래스), 문자필드, 최대 길이(필수설정) 30으로 설정
	content = models.TextField()			   # content 필드는 TextField (텍스트저장 문자열필드클래스), 문자열의 길이 제한 없도록(본문내용이니까)

	uploaded_image = models.ImageField(upload_to="images/", null=True, blank=True)
	uploaded_file = models.FileField(upload_to="files/", null=True, blank=True)

	created_at = models.DateTimeField(auto_now_add=True, null=True)	   # created_at 필드는 DateTimeField(날짜+시간저장 필드클래스),2025-07-30 14:32:00 등의형식으로저장됨
								   # 해당 필드에는 작성된 시간 등 저장 가능,
								   # auto_now_add=True 같은 옵션을 주면 자동으로 생성 시간 저장도 가능.
	updated_at = models.DateTimeField(auto_now=True, null=True)  # 해당줄추가

	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)  # 카테고리 연결 추가

	def __str__(self):
		return f' [ {self.pk} ]{self.title}'  # 두줄추가하기.

	def get_absolute_url(self) :
		return f'/blog/{self.pk}/'