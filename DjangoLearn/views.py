from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm


def home_page(request):
	context = {
		"title":"Hello world !",
		"content":"Welcome to the home page"
	}
	return render(request, "home_page.html", context)

def about_page(request):
	context = {
		"title": "About page!",
		 "content":"Welcome to the about page"
	}
	return render(request, "home_page.html", context)

def contact_page(request):
	contact_form = ContactForm()
	context = {
		"title": "Contact page !",
		"content": "Welcome to the contact page",
		"form": contact_form
	}
	if request.method == 'POST':
		print(request.POST.get('fullname'))
		print(request.POST.get('email'))
		print(request.POST.get('content'))
	return render(request, "contact/view.html", context)

def home_page_old(request):
	return render(request, "home_page.html", {})

	html_ = """
	<!doctype html>
	<html lang="en">
  	<head>
    	<!-- Required meta tags -->
    	<meta charset="utf-8">
    	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

	    <!-- Bootstrap CSS -->
    	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

	    <title>Hello, world!</title>
  	</head>
  	<body>
  		<div class='text-center'>
    	<h1>Hello, world!</h1>
		</div>
	    <!-- Optional JavaScript -->
    	<!-- jQuery first, then Popper.js, then Bootstrap JS -->
    	<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    	<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    	<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
  	</body>
	</html>
	"""
	return HttpResponse(html_)