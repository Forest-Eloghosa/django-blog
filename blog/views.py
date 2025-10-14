from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from .models import Event



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

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )


def event_detail(request, event_id):
    """
    Display an individual :model:`blog.Event`.

    Context:
    ``event`` - an Event instance

    Template:
    `events/event_detail.html`
    """
    event = get_object_or_404(Event, event_id=event_id)

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