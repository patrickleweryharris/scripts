import praw
# Delete all saved posts / comments on your reddit account with PRAW. Needs Python 2.7 + and Praw 5.3.0



# Replace fields in capitals with your info. CLIENT_ID and CLIENT_SECRET come from creating a developer app on reddit
r = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, password=PASSWORD,username=USERNAME, user_agent='/u/USERNAME delete all saved entries')

saved = r.user.me().saved(limit=1000)
for s in saved:
  try:
    s.unsave()
  except AttributeError as err:
    print(err)
