from django import forms

class ItemForm(forms.Form):
    item_text = forms.CharField(
        widget=forms.fields.TextInput(attrs={
            'placeholder': '작업 아이템 입력',
            'class': 'form-control input-lg'
        }),
    )
    
