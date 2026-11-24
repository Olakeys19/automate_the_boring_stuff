# PUSH NOTIFICATIONS

# Sendung Notifications
import requests
requests.post('https://ntfy.sh/OlakeysANproject26001xyz', 'Hello, world!')      # send the message Hello world! TO ALL USERS SUBSCRIBED TO THE TOPIC: OlakeysANproject26001xyz

# NOTE: The ntfy app must be installed on your device and you must be subscribed to the specified topic to receive notificationss


# Transmitting Metadata
"""
A title is similar to an email subject line, and most apps display it above the message text in a larger font. A priority level ranges from 1 (the lowest priority) to 5 (the highest), with 3 being the default. A higher priority doesn’t deliver messages any faster; it just allows subscribers to configure their notification apps to display only messages of a certain priority or higher. Tags are keywords that subscribers can use to filter messages. Tags can also be the name of an emoji to display next to the message title. You can find a list of these emojis at https://docs.ntfy.sh/publish/#tags-emojis.

"""
import requests
requests.post('https://ntfy.sh/OlakeysANproject26001xyz', 'The rent is too high!', headers={'Title':'Important: Read this!', 'Tags': 'warning,neutral_face', 'Priority':'5'})



# Receiving Notifications
import requests
resp = requests.get('https://ntfy.sh/OlakeysANproject26001xyz/json?poll=1') # This is retrieving messages through polling, which returns all the messages for a topic that the server has
resp.text
# NOTE: we call the requests.get() function to receive notifications, unlike the requests.post() function used when sending notifications. Also, the URL ends in /json?poll=1.

# NOTE:
"""
You can also add a since URL parameter after poll=1 to get the messages by one of the following criteria:

since=10m Retrieves all messages for the topic in the last 10 minutes. You can also use s for seconds and h for hours, such as since=2h30m for all messages in the last two and a half hours.

since=1737866912 Retrieves all messages since the Unix epoch timestamp of 1737866912. This kind of timestamp is returned by time.time() and represents the number of seconds since January 1, 1970. Chapter 19 covers time-related functions.

since=wZ22cjyKXw1F Retrieves all messages after the message that had the ID of 'wZ22cjyKXw1F'.

"""

resp = requests.get('https://ntfy.sh/OlakeysANproject26001xyz/json?poll=1&since=10m')       # get all messages within the last 10 minutes
resp.text


# The text of this HTTP response is not valid JSON, since it contains a JSON object on each line of text, rather than one JSON object, so we use the splitlines() string method before parsing them individually with the json module.
import json
notifications = []
for json_text in resp.text.splitlines():
    notifications.append(json.loads(json_text)) 
print(notifications[0]['message'])
print(notifications[1]['message'])
