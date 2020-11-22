from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post

class LatestEntriesFeed(Feed):
    title = "Recent posts"
    link = "/sitenews/"
    description = "Recent posts from my site."

    def items(self):
        return Post.objects.order_by('created_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    # item_link is only needed if NewsItem has no get_absolute_url method.
#    def item_link(self, item):
#        return reverse('list_view', args=[item.pk])