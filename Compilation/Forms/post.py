from django.forms import ModelForm 
from Compilation.models import Post

class PostForm(ModelForm): 
    class Meta: 
        model = Post
        fields = ['Description'] 