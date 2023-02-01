

def sesion(request):
    usuario_actual= request.user
    
    context={
        'usuario_actual':usuario_actual,
        
    }
    return context