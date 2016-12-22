from django.http import HttpResponse
from django.shortcuts import render_to_response
from . import change

def maker(request):
	query = request.GET.get("query","")
	query = query.encode("utf-8")
	if not query:
		return HttpResponse("ERROR: QUERY NOT PROVIDED!")
	else:
		encypted = change.change(query)
		print encypted
		return render_to_response("changed.html",{"data":encypted,"mode":"CHEAT"})

	return HttpResponse(str(query))




def revise(request):
	query = request.GET.get("query","")
	query = query.encode("utf-8")

	if not query:
		return HttpResponse("ERROR: QUERY NOT PROVIDED!")
	else:
		encypted = change.leave_blanks(query)
		print encypted
		return render_to_response("changed.html",{"data":encypted,"mode":"REVISE",'l':True})

	return HttpResponse(str(query))


def home(request):
	return render_to_response('index.html')


def about(request):
	return render_to_response('about.html')

def abt(request):
	return render_to_response('abt_language.html')