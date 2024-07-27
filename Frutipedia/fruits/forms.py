from django import forms

from Frutipedia.fruits.models import Category, Fruit


class CreateBaseCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter category name'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = ''


class CreateCategory(CreateBaseCategory):
    pass


class CreateBaseFruits(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter fruit name'}),
            'Image_url': forms.URLInput(attrs={'placeholder': 'Enter image url'}),
            'description': forms.TextInput(attrs={'placeholder': 'Enter description'}),
            'nutrition': forms.NumberInput(attrs={'placeholder': 'Enter nutrition'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = ''


class CreateFruits(CreateBaseFruits):
    pass


class EditFruits(CreateBaseFruits):
    pass


class DeleteFruits(CreateBaseFruits):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled = True
