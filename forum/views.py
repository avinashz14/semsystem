from django.shortcuts import render ,redirect, get_object_or_404
from django.views.generic import TemplateView
from forum.models import Bang, Category
from forum.forms import Rev, Edi
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms import ModelForm


class HomeView(TemplateView):
	template_name='forum/home.html'
	 
	
	def get(self, request):
		form = Rev()
		kings = Bang.objects.all().order_by('-created_at') 
		args = {'form':form, 'kings':kings }
		return render(request, self.template_name, args)

		

		

@login_required
def rev(request):
	if request.method=='POST':
		form = Rev(request.POST,request.FILES)
		if form.is_valid():
			p=form.save(commit=False)
			p.user=request.user
			p.save()
			return HttpResponseRedirect('/forum')
		       
		else:
			return HttpResponseRedirect('/home/rev')

	else:
		form = Rev()
		args={'form':form}
		return render(request,'forum/rev.html',args)


class RevForm(ModelForm):
    class Meta:
        model = Bang
        fields = [
		 'name',
		'category',
		'location',
		'title',
		'rating',
		'review',
		
		 
		 ]

def rev_update(request, pk, template_name='forum/forum_form.html'):
	rev= get_object_or_404(Bang, pk=pk)
	form = RevForm(request.POST or None , instance=rev)
	if form.is_valid():
		form.save()
		return redirect('/forum/')
	return render(request, template_name, {'form':form})


def about(request):
	return render(request, 'forum/about.html')


def fil(request,pk):
	some_category = Category.objects.get(pk=pk)
	product=Bang.objects.filter(category=some_category)
	context = {'product': product}
	template = 'forum/filter.html'  
	return render(request, template, context)  

def cate(request):
	ca=Category.objects.all()
	return render(request,'forum/category.html',{'ca':ca})