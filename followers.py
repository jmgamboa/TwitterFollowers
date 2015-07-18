import tweepy
import random

# Set authorization tokens
auth = tweepy.OAuthHandler(x, y)
auth.set_access_token(x, y)
# Instantiate Tweepy Module
api = tweepy.API(auth)

# unfollow amount by page; 20 a page
def unfollow(limit):
	pages = range(limit)
	for page in pages:
		# get friends
		x = api.me().friends(page=page)
		for i in x:
			# unfollow
			api.destroy_friendship(i.id)

# get suggestions based off slug
def get_suggestions(slug):
	# get suggested users
	x = api.suggested_users(slug=slug)
	return x

# get categories suggested
def get_suggested_cats():
	categories = api.suggested_categories()
	array_cats = []
	for i in categories:
		array_cats.append(i.name)
	return array_cats

# follow from ID
def follow(user_id):
	api.create_friendship(user_id)


# choose random cat
def random_item(array):
	oneCat = random.choice(array)
	return oneCat


# unfollow(100)
# cats = get_suggested_cats()
# oneCat = random_item(cats)
# x = get_suggestions(oneCat)
# for user in x:
# 	print user.screen_name
# 	follow(user.screen_name)

