from django.shortcuts import render
from django.http import JsonResponse


from .models import Comment
from .models import CommentForm

import datetime


def load_comments(request):
    result, comment_4, comment_3, comment_2, comment_1 = [], [], [], [], []
    comment_5 = Comment.objects.filter(rating=5)[:5]
    for i in comment_5:
        result.append(to_json(i))
    if len(comment_5) < 5:
        comment_4 = Comment.objects.filter(rating=4)[:5-len(comment_5)]
        for k in comment_4:
            result.append(to_json(k))
    if (len(comment_5) + len(comment_4)) < 5:
        comment_3 = Comment.objects.filter(rating=3)[:5-(len(comment_5) + len(comment_4))]
        for j in comment_3:
            result.append(to_json(j))
    return JsonResponse({'comments': result}, safe=False)


def add_comments(request):
    comment_form = CommentForm(request.POST)
    if request.method == 'POST':
        formset = comment_form
        if formset.is_valid():
            author = formset.save(commit=False)
            comment = Comment(user=author.user)
            comment.comment_text = author.comment_text
            comment.pub_date = datetime.datetime.now()
            comment.rating = author.rating
            comment.save()
    else:
        formset = comment_form
    return render(request, "add_comment.html", {"formset": formset})


def to_json(comment):
    # {'1 comment': {'user': asd, 'text': asfasd, 'rating': 1/2/3/4/5, 'date': asojd},
    # '2 comment': {},
    # '3 comment': {},
    # '4 comment': {},
    # '5 comment': {}}
    results = {'user': comment.user.first_name,
               'text': comment.comment_text,
               'rating': comment.rating,
               'date': comment.pub_date,
               'city': comment.user.profile.city,
               'avatar': comment.user.profile.user_avatar.url
              }
    return results
