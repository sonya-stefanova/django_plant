from django.shortcuts import render, redirect
from django_plant.web.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm, PlantCreateForm, PlantEditForm, PlantDeleteForm
from django_plant.web.models import Profile, Plant


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None

def show_home(request):
    profile = get_profile()
    if profile is None:
        return redirect('create profile')

    context = {
        'profile': profile,
    }

    return render(request, 'home-page.html', context)


def create_profile(request):
    profile = get_profile()
    if profile is not None:
        return redirect('index')

    if request.method == 'POST':
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = ProfileCreateForm()

    context = {
        'profile':profile,
        'form': form,
    }
    return render(request, 'create-profile.html', context)



def show_catalogue(request):
    profile = Profile.objects.first()
    plants = Plant.objects.all()
    context = {
        'profile': profile,
        'plants':plants,
    }

    return render(request, 'catalogue.html', context)




def edit_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')
    else:
        form = ProfileEditForm(instance=profile)

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'edit-profile.html', context=context)

def details_profile(request):
    profile = get_profile()
    plants = Plant.objects.all().count()

    context = {
        'profile': profile,
        'plants':plants,

    }
    return render(request, 'profile-details.html', context=context)

def delete_profile(request):
    profile = get_profile()
    plants = Plant.objects.all()

    if request.method == 'POST':
        form = ProfileDeleteForm(profile, instance=profile)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = ProfileDeleteForm(instance=profile)

    context = {
        'profile': profile,
        'forms': form,

    }
    return render(request, 'delete-profile.html', context=context)


def create_plant(request):
    profile = get_profile()

    if request.method == 'POST':
        form = PlantCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = PlantCreateForm()

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'create-plant.html', context)



def edit_plant(request, pk):
    profile=get_profile()
    plant = Plant.objects.filter(pk=pk).get()

    if request.method == 'POST':
        form = PlantEditForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('details plant', plant.pk)
    else:
        form = PlantEditForm(instance=plant)

    context = {
        "profile": profile,
        "plant": plant,
        'form': form,

    }
    return render(request, 'edit-plant.html', context)

def details_plant(request, pk):
    profile = get_profile()
    plant = Plant.objects.filter(pk=pk).get()

    context = {
        'profile': profile,
        'plant': plant,
    }
    return render(request, 'plant-details.html', context = context)

def delete_plant(request, pk):
    profile = get_profile()
    plant = Plant.objects.\
        filter(pk=pk).\
        get()

    if request.method == 'POST':
        form = PlantDeleteForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = PlantDeleteForm(instance=plant)

    context = {
        'profile': profile,
        'form': form,
        'plant': plant,
    }
    return render(request, 'delete-plant.html', context )