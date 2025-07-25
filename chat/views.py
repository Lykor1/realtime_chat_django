from django.shortcuts import render, redirect


def chat_page(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('login')
    context = {}
    return render(request, 'chat/chat_page.html', context)
