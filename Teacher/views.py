from django.shortcuts import render
from .Forms.post import PostForm 
from .models import Post 






# Create your views here.

  





class Q_Create(View): 
    
    def get(self, request, *args, **kwargs):
           
        if request.user.is_authenticated:
            return render(request,'postcreate.html',{'form':PostForm})
        else:
            return render(request,'login.html')
    
    def post(self, request):
        f = PostForm(request.POST)
        p = Post()
        if f.is_valid() and request.FILES['input_file'] and request.FILES['output_file']:
            myfile = request.FILES['input_file']
            
            name = "_".join(request.POST.get("pn").split())

            myfile.name = name+".txt"
            fs = FileSystemStorage(location=MEDIA_ROOT+"\\"+"input")
            fs.save(myfile.name, myfile)

            myfile = request.FILES['output_file']
            myfile.name = name+".txt"
            fs = FileSystemStorage(location=MEDIA_ROOT+"\\"+"testcase")
            fs.save(myfile.name, myfile)

            p.Problem_Name = request.POST.get("pn")
            p.Problem_Rank = request.POST.get("pr")
            p.Memory_Size = request.POST.get("ms")
            p.Time_Limit = request.POST.get("tl")
            p.Output_Limit = request.POST.get("ol")
            p.Testcase_Number = request.POST.get("tl")
            p.Testcase_Linenumber = request.POST.get("tlines")
            p.Description= f.cleaned_data["Description"]

            p.save()
        return HttpResponseRedirect(reverse('home'))