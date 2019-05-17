from django.shortcuts import render

def home_view(request):
	return render(request, "home.html", {})

def about_view(request):
	return render(request, "about.html", {})

def contact_view(request):
	return render(request, "contact.html", {})



# For debug purpose
# -----------------------------------------------------------------
def self_note_view(request):
	return render(request, "self_note.html", {})
