from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Comment
from django.urls import reverse
# Create your views here.
def index(request):
	#comments = Comment.objects.all()
	comments = Comment.objects.all()#order_by('-pub_date')[:5]
	return render(request, 'main/main.html', {'comments':comments})

def leave_comment(request):
	Comment.objects.create(
		first_name = request.POST.get('fn'), 
		last_name = request.POST.get('ln'),
		author_email = request.POST.get('em'), 
		comment_texr = request.POST.get('text'),
	)

	return HttpResponseRedirect(reverse('main:index'))