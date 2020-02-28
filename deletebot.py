import praw
import time

now = time.time()

reddit = praw.Reddit('DeleteBot')

myuser = reddit.redditor(reddit.config.username)
daystokeep = int(reddit.config.custom['daystokeep'])



for acomment in myuser.comments.new(limit=500):
	print("Text: ", acomment.body[0:50])
	if ((now - acomment.created_utc) > (daystokeep * 86400)):
		print("Replacing comment with a single period.")
		acomment.edit(".")
		print("Deleting the comment.")
		print(" ")
		acomment.delete()

for asubmission in myuser.submissions.new(limit=500):
	print("Text: ", asubmission.selftext[0:50])
	if ((now - asubmission.created_utc) > (daystokeep * 86400)):
		print("Deleting...")
		print(" ")
		asubmission.delete()