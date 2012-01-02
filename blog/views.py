'''========================================================================

    Imports

    ======================================================================='''
from views_util import * 
import models

'''========================================================================

    View Functions

    ======================================================================='''
'''========================================================================
    Base Pages
    ======================================================================='''
@render_to('blog/home.html')
def page_home(request):
    '''page_home(request):
    ----------------------
    Renders the base page which provides access to interaction functions
    below'''
    latest_posts = models.Post.objects.order_by('-post_date')[:5]
    return {
        'latest_posts': latest_posts,
    }
