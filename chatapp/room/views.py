from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect

from .models import Message, Room
from .forms import RoomForm
@login_required
def rooms(request):	
	
	if request.method == 'POST':
		form = RoomForm(request.POST)
		if form.is_valid():
			form.save() 
			return redirect('rooms')  
	else:
		form = RoomForm()			
		rooms = Room.objects.all()
		context = {
			'rooms': rooms,
			'form': form,
		}	
	return render(request, 'room/rooms.html',context)
@login_required    
def room_make(request):
	if request.method == 'POST':
		form = RoomForm(request.POST)
		if form.is_valid():
			form.save()   
	else:
		form = RoomForm()
	return render(request, 'room/room1.html', {'form': form})
@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'room/room.html', {'room': room, 'messages': messages})
	
