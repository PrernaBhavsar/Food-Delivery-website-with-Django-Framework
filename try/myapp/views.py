from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView
from .forms import Newsletter_form
from django.contrib import messages

def main(request):
    if(request.method == 'GET'):
        template_name = 'myapp/index.html'
        return render(request, template_name)

def submit(request):
    if request.method == "POST":
        form_obj = Newsletter_form(data=request.POST)
        print(form_obj.is_valid(), form_obj.errors, type(form_obj.errors))
        if form_obj.is_valid():
            model_obj = form_obj.save()
            model_obj.save()
            print(model_obj.name)
            return render(request, 'menu/indexnewsletter.html')
        else:
            return render(request, 'menu/indexerror.html')

    else:
        form_obj = Newsletter_form()
    return render(request, "myapp/index.html", {'form': form_obj})

def first(request):
    return redirect('/main/')


# class newsletter(TemplateView):
#     template_name = 'myapp/index.html'
#     def get(self, request):
#         form_obj = Newsletter_form(request.GET)
#         return render(request, self.template_name, {'form': form_obj})
#
#     def post(self, request):
#         form_obj = Newsletter_form(request.POST)
#         print(form_obj.is_valid(), form_obj.errors, type(form_obj.errors))
#         if form_obj.is_valid():
#             model_obj = form_obj.save()
#             model_obj.save()
#             return HttpResponse("Done")
#         else:
#             form_obj = Newsletter_form()
#             return render(request, "myapp/index.html", {'form': form_obj})


