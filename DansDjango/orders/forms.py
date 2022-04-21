from django import forms
# from orders.models import Post

class CreateOrder(forms.ModelForm):
    item = forms.IntegerField(required=False)
    
    # class Meta:
    #     model = post
    #     fields = ('post',)
    