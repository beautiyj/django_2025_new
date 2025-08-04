from django.shortcuts import render

def index(request):
    return render(
	request,
	'main_shopping_mall.html',
	)

# 쇼핑몰 홈페이지에 필요한 거 - 상품리스트, 상품 개별 페이지(상세페이지)
#main_shopping_mall.html
