from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Post
from .models import Event
from .forms import CommentForm


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            # associate the comment with the logged-in user and the current post
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.success(request, "Comment submitted and awaiting approval")
            # create a new blank form after successful submit
            comment_form = CommentForm()
    else:
        # GET: present an empty comment form
        comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
         {
        "post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
    },
        
    )


def event_detail(request, event_id):
    """
    Display an individual :model:`blog.Event`.

    Context:
    ``event`` - an Event instance

    Template:
    `events/event_detail.html`
    """
    event = get_object_or_404(Event, pk=event_id)

    return render(
        request,
        "events/event_detail.html",
        {"event": event},
    )

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6