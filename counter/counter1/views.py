from django.shortcuts import render
from .models import fields
# Create your views here.

def index(request):
	obj = fields.objects.all()
	return render(request, 'new.html', {'fields' : obj})

def count_update_all(request):
	obj = fields.objects.all()
	for ob in obj:
		ob.value = ob.value+1
		ob.save()

	return render(request, 'new.html', { 'fields' : obj})	

def increment(request , count_value):
	obj = fields.objects.all()

	# count_value is the field name in am sending here
	ob = fields.objects.get(field_name = count_value)
	ob.value = ob.value +1
	ob.save()

	return render(request, 'new.html', {'fields' : obj})	

def delete_field(request, count_value):	
	obj = fields.objects.all()
	ob = fields.objects.get(field_name = count_value)
	ob.delete()
	#ob.save()
	return render(request, 'new.html', {'fields' : obj})

def reset(request, count_value):
	obj = fields.objects.all()
	ob = fields.objects.get(field_name = count_value)
	ob.value = 0
	ob.save()
	return render(request, 'new.html', {'fields' : obj})



def nf_press(request):
	obj = fields.objects.all()
	press = True
	return render(request, 'new.html', {'press' : press , 'fields' : obj})	

def new_field(request):
	obj = fields.objects.all()
	
	if request.method == "POST" :
		name = request.POST['field_name']
		ins = fields(field_name= name, value=0)
		ins.save()
		print("added successfully")

	return render(request, 'new.html', {'fields' : obj})	

