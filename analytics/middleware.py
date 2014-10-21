from django.conf import settings
from ipware.ip import get_real_ip
import requests
from analytics.models import Page, Location, View


class LocationMiddleware(object):
    def process_request(self, request):
        # Get the IP Address of this request
        ip = get_real_ip(request)

        # If we didn't get an IP Address and we're developing locally,
        # make an API call to get our IP Address.
        if ip is None and settings.DEBUG:
            ip = requests.get('http://icanhazip.com/').text

        print ip

        if ip is not None:
            response = requests.get('http://ipinfo.io/{}/json'.format(ip))
            if response.status_code == 200:
                request.location = response.json()
                # Split out the lat and long from the location
                request.location['latitude'], request.location['longitude'] = request.location['loc'].split(',')

        request.ip = ip


class PageViewMiddleware(object):
    def process_request(self, request):
    # # request.META['PATH_INFO']
    #     # get or create the Page object
    #     # find URL - request.META['PATH_INFO']
    #     newurl = request.META['PATH_INFO']
    #     request_page, created = Page.objects.get_or_create(url=newurl)
    #
    #     # get or create the Location object
    #     # get info from request.location
    #
    #     newcity = request.location['city']
    #     newregion = request.location['region']
    #     newcountry = request.location['country']
    #
    #     location = latitude = longitude = None
    #
    #     request_location, created = Location.objects.get_or_create(city=newcity, region=newregion, country=newcountry)
    #
    #     # # create View object every time a request come through
    #     # newtime = request.View['timestamp']
    #     # lat = request.View['latitude']
    #     # lon = request.View['longitude']
    #
    #     View.objects.create(
    #         page=request_page,
    #         location=request_location,
    #         latitude=request.location['latitude'],
    #         longitude=request.location['longitude'],
    #         ip_address=request.ip,
    #     )
        page, created = Page.objects.get_or_create(url=request.META.get('PATH_INFO'))

        location = latitude = longitude = None
        if request.location:
            location, created = Location.objects.get_or_create(city=request.location['city'],
                                                               region=request.location['region'],
                                                               country=request.location['country'])
            latitude = request.location['latitude']
            longitude = request.location['longitude']

        View.objects.create(page=page, location=location, latitude=latitude, longitude=longitude,
                            ip_address=request.ip)



