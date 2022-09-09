def create(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('reservation:detail',article.pk)
    else:
        form = ReservationForm()
    context={
        'form':form
    }
    return render(request,'reservation/create.html',context)



# context 아래 구문의 깊이를 변경.