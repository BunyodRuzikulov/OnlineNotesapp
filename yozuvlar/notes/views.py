from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import Note, Folder, Tag
from .forms import LoginForm, CustomUserCreationForm, NoteForm, FolderForm, ProfileForm
from django.urls import reverse
import json

def home(request):
    return render(request, 'index.html')

def auth_view(request):
    login_form = LoginForm()
    signup_form = CustomUserCreationForm()

    if request.method == 'POST':
        if 'login' in request.POST:
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                email = login_form.cleaned_data['email']
                password = login_form.cleaned_data['password']
                user = authenticate(request, username=User.objects.get(email=email).username, password=password)
                if user:
                    login(request, user)
                    return redirect('dashboard')
                messages.error(request, 'Email yoki parol xato!')
        elif 'signup' in request.POST:
            signup_form = CustomUserCreationForm(request.POST)
            if signup_form.is_valid():
                user = signup_form.save()
                login(request, user)
                return redirect('dashboard')
            messages.error(request, 'Ro‘yxatdan o‘tishda xatolik!')

    return render(request, 'auth.html', {'login_form': login_form, 'signup_form': signup_form})

@login_required
def dashboard(request):
    notes = Note.objects.filter(user=request.user, status='active')
    query = request.GET.get('q', '')
    sort = request.GET.get('sort', 'date-desc')

    if query:
        notes = notes.filter(title__icontains=query) | notes.filter(tags__name__icontains=query)

    if sort == 'date-desc':
        notes = notes.order_by('-created_at')
    elif sort == 'date-asc':
        notes = notes.order_by('created_at')
    elif sort == 'name-asc':
        notes = notes.order_by('title')
    elif sort == 'name-desc':
        notes = notes.order_by('-title')

    return render(request, 'dashboard.html', {'notes': notes, 'query': query, 'sort': sort})

@login_required
def create_note(request):
    form = NoteForm()
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            form.save_m2m()  # Save tags
            messages.success(request, 'Yozuv saqlandi!')
            return redirect('dashboard')
    return render(request, 'create.html', {'form': form})

@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    form = NoteForm(instance=note)
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            note = form.save()
            form.save_m2m()
            messages.success(request, 'Yozuv tahrirlandi!')
            return redirect('dashboard')
    return render(request, 'create.html', {'form': form, 'note': note})

@login_required
def view_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    return render(request, 'view.html', {'note': note})

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    note.status = 'deleted'
    note.save()
    messages.success(request, 'Yozuv o‘chirildi!')
    return redirect('dashboard')

@login_required
def categories(request):
    folders = Folder.objects.filter(user=request.user)
    unassigned_notes = Note.objects.filter(user=request.user, folder__isnull=True, status='active')
    if request.method == 'POST':
        form = FolderForm(request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.user = request.user
            folder.save()
            return redirect('categories')
    else:
        form = FolderForm()
    return render(request, 'categories.html', {'folders': folders, 'unassigned_notes': unassigned_notes, 'form': form})

@login_required
def delete_folder(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id, user=request.user)
    folder.delete()
    messages.success(request, 'Papka o‘chirildi!')
    return redirect('categories')

@login_required
def assign_note_to_folder(request, note_id, folder_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    folder = get_object_or_404(Folder, id=folder_id, user=request.user)
    note.folder = folder
    note.save()
    return HttpResponse(json.dumps({'status': 'success'}), content_type='application/json')

@login_required
def archive(request):
    archived_notes = Note.objects.filter(user=request.user, status='archived')
    deleted_notes = Note.objects.filter(user=request.user, status='deleted')
    return render(request, 'archive.html', {'archived_notes': archived_notes, 'deleted_notes': deleted_notes})

@login_required
def restore_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    note.status = 'active'
    note.save()
    messages.success(request, 'Yozuv tiklandi!')
    return redirect('archive')

@login_required
def delete_permanently(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    note.delete()
    messages.success(request, 'Yozuv butunlay o‘chirildi!')
    return redirect('archive')

@login_required
def search(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')
    date_from = request.GET.get('date_from', '')
    date_to = request.GET.get('date_to', '')

    notes = Note.objects.filter(user=request.user, status='active')
    if query:
        notes = notes.filter(title__icontains=query) | notes.filter(content__icontains=query) | notes.filter(tags__name__icontains=query)
    if category:
        notes = notes.filter(folder__name=category)
    if date_from:
        notes = notes.filter(created_at__gte=date_from)
    if date_to:
        notes = notes.filter(created_at__lte=date_to)

    return render(request, 'search.html', {'notes': notes, 'query': query, 'category': category, 'date_from': date_from, 'date_to': date_to})

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil saqlandi!')
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})

@login_required
def settings(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        dark_mode = request.POST.get('dark_mode') == 'on'
        # Save settings (e.g., in user profile or session)
        messages.success(request, 'Sozlamalar saqlandi!')
        return redirect('settings')
    return render(request, 'settings.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')