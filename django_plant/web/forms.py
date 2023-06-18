from django import forms
from django_plant.web.models import Profile, Plant


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name')


class ProfileCreateForm(ProfileBaseForm):
    pass

class ProfileEditForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name', 'profile_picture')

class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()

    def save(self, commit=True):
        if commit:
            Plant.objects.all().delete()
            self.instance.delete()
        return self.instance



class PlantBaseForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ('type', 'name', 'image_url', 'description', 'price')


class PlantCreateForm(PlantBaseForm):
    pass

class PlantEditForm(PlantBaseForm):
    pass

class PlantDeleteForm(PlantBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance



    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.disabled = True


