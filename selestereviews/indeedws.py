import requests
import bs4

BASE_URL = "http://www.indeed.com/cmp/"
RATING_DENOMINATOR = 85.225
AVAILABLE_STARS = 5

company = "indeed"

def get_soup(BASE_URL, company):
	"""
	Retrieve the data and parse it.
	"""
	response = requests.get(BASE_URL + company)

	soup = bs4.BeautifulSoup(response.text, 'html.parser')

	return soup

def get_ratings(soup, company):
	"""
	Pull data out of the "soup" and clean to derive data for a 5 point scale
	"""
	company_ratings = {}

	if len(soup.select('dl#cmp-reviews-attributes dt')) != 0:
		company_ratings[company] = {}
		rating_categories = [dl.get_text() for dl in soup.select('dl#cmp-reviews-attributes dt')]

		# need to grab pixel values from dom, splice, and turn into integers
		rating_stars_raw = [span.attrs.get('style') for span in soup.select('span.cmp-star-on')]
		rating_stars_clean = [float(item[7:-2]) for item in rating_stars_raw]

		for item in rating_categories:
			company_ratings[company][item] = round(((rating_stars_clean[rating_categories.index(item)]/RATING_DENOMINATOR) * AVAILABLE_STARS), 1)

		company_ratings[company]['Overall'] = [float(element.get_text()) for element in soup.select('div span.cmp-average-rating')][0]
		return company_ratings

	else:
		company_ratings[company] = {}
		return company_ratings

print get_soup(BASE_URL, company)
print get_ratings(get_soup(BASE_URL, company), company)
