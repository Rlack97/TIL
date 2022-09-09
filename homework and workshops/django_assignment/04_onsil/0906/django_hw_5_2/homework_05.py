def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.title
            content = form.content
            article = Article(title=title,content=content)
            article.save()
            return redirect('articles:detail',article.pk)
    form = ArticleForm()
    context = {
        'form':form
    }
    return render(request,'articles/create.html',context)



    a = form.title
    b = form.content
    c = article.save()