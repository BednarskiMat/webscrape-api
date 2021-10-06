from shows.models import Show
import requests, re
from pyquery import PyQuery as pq



def scrape():
    r = requests.get('https://www.imdb.com/list/ls057886464/?sort=user_rating,desc&st_dt=&mode=detail&page=1')
    source = r.text
    d = pq(source)
    shows = d('div.lister-item-content')
    for show in shows:
        d = pq(show)
        external_id = d('h3 span').text().replace('.', '')
        years = d('h3 span.lister-item-year.text-muted.unbold').text()
        external_id = external_id.replace(years, '')
        external_id = int(external_id.strip())
        name = d('h3.lister-item-header a').text()
        desc = re.findall(r'<p class="">\s*?(.*)<\/p>\s*?<p class="text-muted text-small">', str(d))[0]
        rating = d('div.ipl-rating-star.small span.ipl-rating-star__rating').text()
        obj, created = Show.objects.update_or_create(
            external_id=external_id, title=name, desc=desc, rating=rating
        )

    

