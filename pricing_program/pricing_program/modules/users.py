from django.http import HttpResponse

def create(request):
    return HttpResponse('Create User')

def edit(request):
    return HttpResponse('Edit User')

def delete(request):
    return HttpResponse('Delete User')

def login(request):
    return HttpResponse('Ruta de Login')

def logout(request):
    return HttpResponse('logout User')

def show(request):
    return HttpResponse('Show users list')

def load(request):
    return HttpResponse('Show user')