from django.http import HttpResponse

def login(request):
    return HttpResponse('Ruta de Login')

def create(request):
    return HttpResponse('Create User')

def edit(request):
    return HttpResponse('Edit User')

def delete(request):
    return HttpResponse('Delete User')

def logout(request):
    return HttpResponse('logout User')
