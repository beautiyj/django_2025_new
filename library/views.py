from django.shortcuts import render

def index(request):
    return render(
	request,
	'library/main_library.html',
	)


# 책 홈페이지에 필요한 거 - 책리스트, 책 개별 페이지(상세페이지)
#main_library.html