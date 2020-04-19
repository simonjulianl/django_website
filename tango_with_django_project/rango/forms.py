from django import forms
from rango.models import Page, Category, UserProfile
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length = Category.name_length,
                           help_text = "enter the category name")
    views = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
    likes = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
    slug = forms.CharField(widget = forms.HiddenInput(), required = False)

    class Meta:
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length = Page.title_length,
                            help_text = 'Please enter the title of the page')
    url = forms.URLField(max_length = Page.url_length,
                         help_text = "Please enter the URL of the page")
    views = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)

    
    def clean(self):
        cleaned_data = self.cleaned_data
        print(cleaned_data)
        url = cleaned_data.get('url')

        #if the url is not empty
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url
            return cleaned_data
        
    class Meta:
        model = Page
        exclude = ('category','last_visit','first_visit',)
        #fields = ('title', 'url', 'views'), choose 1 to exclude or include

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    website = forms.URLField(required = False)
    picture = forms.ImageField(required = False)
    
    class Meta:
        model = UserProfile
        exclude = ('user',)

        
        
