from localflavor.us.us_states import STATES_NORMALIZED
from blog.models import Post, Tag, Author, Ad


def latest_post(request):
    return {
        'latest_post': Post.objects.latest('created')
    }

def tag_list(request):
    return {
        'tags': Tag.objects.all(),
        'posts': Post.objects.all(),
        'tags_count': Tag.objects.count()
    }

def author_list(request):
    return {
        'authors': Author.objects.all(),
        'authors_count': Author.objects.count()
    }

def location(request):
    return {
            'location': request.location
    }

def ad_list(request):

    # state= request.location['region'].lower()
    # location = STATES_NORMALIZED[state]

    return {
            # 'ads': Ad.objects.all(),
        # 'ads': Ad.objects.get(id=1)           # get by id number
        'ads': Ad.objects.all().order_by('?')[0] # random pick
        # 'ads': Ad.objects.filter(state=location).order_by('?')[0]
    }

