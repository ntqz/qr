from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index_views(request):
	return HttpResponse('index应用中的index视图')

def login_views(request):
	return HttpResponse('index应用中的login视图')

def getTemp_views(request):
	t=loader.get_template('01_template.html')
	html=t.render()
	return HttpResponse(html)

def render_views(request):
	return render(request,'01_template.html')

def var_views(request):
	dic={
		'title':'测试模板',
		'content':'模板的内容',
	}
	return render(request, '02_var.html', dic)

def varExer_views(request):
	title='水浒传'
	author='施耐庵'
	topic='105个男人和3个女人的故事'
	return render(request, '03_exer.html', locals())

def fun(a,b):
	return a+b

class A:
	a='A 类中的属性a'
	
	def f(self):
		return 'this is the method of A'

def varTemp_views(request):
	l = ['老舍', '朱自清', '莫言', '泰戈尔', '奥斯特洛夫斯基']
	t = ('冰心', '韩寒', '郭敬明')
	d = {'A': 'Andrew', 'B': 'BEYOND', 'C': 'Controller'}
	return render(request, '04_var.html',{
		'num':10086,
		'str':'中国移动',
		'list':l,
		'tup':t,
		'dic':d,
		'fun':fun(25,52),
		'A':A()
		})