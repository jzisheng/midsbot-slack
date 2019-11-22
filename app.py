import os
import logging
import slack
import ssl as ssl_lib
import certifi
# from onboarding_tutorial import OnboardingTutorial,EmailAnnouncement
from EmailTemplate import EmailAnnouncement
from utils import parse_email
# For simplicity we'll store our app data in-memory with the following data structure.
# onboarding_tutorials_sent = {"channel": {"user_id": OnboardingTutorial}}
onboarding_tutorials_sent = {}
def invalid_command(message, web_client: slack.WebClient, user_id: str, channel: str):
    email = EmailAnnouncement(channel)    
    WELCOME_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                message
            ),
        },
    }
    
    message =\
             {
            "ts": email.timestamp,
            "channel": email.channel,
            "username": email.username,
            "icon_emoji": email.icon_emoji,
            "blocks": [
                WELCOME_BLOCK,
            ],
        }
    # Post the onboarding message in Slack
    response = web_client.chat_postMessage(**message)
    pass


def start_onboarding(web_client: slack.WebClient, user_id: str, channel: str):
    # Create a new onboarding tutorial.
    #onboarding_tutorial = OnboardingTutorial(channel)
    email = EmailAnnouncement(channel)
    message = email.get_message_payload()
    response = web_client.chat_postMessage(**message)
    email.timestamp = response["ts"]
    if channel not in onboarding_tutorials_sent:
        onboarding_tutorials_sent[channel] = {}
    onboarding_tutorials_sent[channel][user_id] = email
    pass

def get_announcements(web_client: slack.WebClient, user_id: str, channel: str):
    # Create a new onboarding tutorial.
    #onboarding_tutorial = OnboardingTutorial(channel)
    email = EmailAnnouncement(channel)
    message = email.get_announcements_payload()
    response = web_client.chat_postMessage(**message)
    email.timestamp = response["ts"]
    if channel not in onboarding_tutorials_sent:
        onboarding_tutorials_sent[channel] = {}
    onboarding_tutorials_sent[channel][user_id] = email
    pass


def get_schedule(web_client: slack.WebClient, user_id: str, channel: str):
    # Create a new onboarding tutorial.
    #onboarding_tutorial = OnboardingTutorial(channel)
    email = EmailAnnouncement(channel)
    message = email.get_schedule_payload()
    response = web_client.chat_postMessage(**message)
    email.timestamp = response["ts"]
    if channel not in onboarding_tutorials_sent:
        onboarding_tutorials_sent[channel] = {}
    onboarding_tutorials_sent[channel][user_id] = email
    pass


def get_today(web_client: slack.WebClient, user_id: str, channel: str):
    email = EmailAnnouncement(channel)
    message = email.get_today()
    # Post the onboarding message in Slack
    response = web_client.chat_postMessage(**message)
    email.timestamp=response["ts"]
    pass


def get_litty(web_client: slack.WebClient, user_id: str, channel: str):
    email = EmailAnnouncement(channel)    
    WELCOME_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "BEEP BOOP I'm a bot but heck yes :pparrot:"
            ),
        },
    }
    
    message =\
             {
            "ts": email.timestamp,
            "channel": email.channel,
            "username": email.username,
            "icon_emoji": email.icon_emoji,
            "blocks": [
                WELCOME_BLOCK,
            ],
        }
    # Post the onboarding message in Slack
    response = web_client.chat_postMessage(**message)

    pass


# ================ Team Join Event =============== #
# When the user first joins a team, the type of the event will be 'team_join'.
# Here we'll link the onboarding_message callback to the 'team_join' event.
@slack.RTMClient.run_on(event="team_join")
def onboarding_message(**payload):
    """Create and send an onboarding welcome message to new users. Save the
    time stamp of this message so we can update this message in the future.
    """
    """
    # Get WebClient so you can communicate back to Slack.
    web_client = payload["web_client"]

    # Get the id of the Slack user associated with the incoming event
    user_id = payload["data"]["user"]["id"]

    # Open a DM with the new user.
    response = web_client.im_open(user_id)
    channel = response["channel"]["id"]

    # Post the onboarding message.
    start_onboarding(web_client, user_id, channel)
    """
    pass


# ============= Reaction Added Events ============= #
# When a users adds an emoji reaction to the onboarding message,
# the type of the event will be 'reaction_added'.
# Here we'll link the update_emoji callback to the 'reaction_added' event.
@slack.RTMClient.run_on(event="reaction_added")
def update_emoji(**payload):
    """Update the onboarding welcome message after receiving a "reaction_added"
    event from Slack. Update timestamp for welcome message as well.
    """
    """
    data = payload["data"]
    web_client = payload["web_client"]
    channel_id = data["item"]["channel"]
    user_id = data["user"]

    if channel_id not in onboarding_tutorials_sent:
        return

    # Get the original tutorial sent.
    onboarding_tutorial = onboarding_tutorials_sent[channel_id][user_id]

    # Mark the reaction task as completed.
    onboarding_tutorial.reaction_task_completed = True

    # Get the new message payload
    message = onboarding_tutorial.get_message_payload()

    # Post the updated message in Slack
    updated_message = web_client.chat_update(**message)

    # Update the timestamp saved on the onboarding tutorial object
    onboarding_tutorial.timestamp = updated_message["ts"]
    """

    """
    email = EmailAnnouncement(channel)

    # Get the onboarding message payload
    message = email.get_message_payload()

    # Post the onboarding message in Slack
    response = web_client.chat_postMessage(**message)
    """
    pass
    

# =============== Pin Added Events ================ #
# When a users pins a message the type of the event will be 'pin_added'.
# Here we'll link the update_pin callback to the 'reaction_added' event.
@slack.RTMClient.run_on(event="pin_added")
def update_pin(**payload):
    """Update the onboarding welcome message after receiving a "pin_added"
    event from Slack. Update timestamp for welcome message as well.
    """
    
    """
    data = payload["data"]
    web_client = payload["web_client"]
    channel_id = data["channel_id"]
    user_id = data["user"]

    # Get the original tutorial sent.
    onboarding_tutorial = onboarding_tutorials_sent[channel_id][user_id]

    # Mark the pin task as completed.
    onboarding_tutorial.pin_task_completed = True

    # Get the new message payload
    message = onboarding_tutorial.get_message_payload()

    # Post the updated message in Slack
    updated_message = web_client.chat_update(**message)

    # Update the timestamp saved on the onboarding tutorial object
    onboarding_tutorial.timestamp = updated_message["ts"]
    """
    pass

# ============== Message Events ============= #
# When a user sends a DM, the event type will be 'message'.
# Here we'll link the message callback to the 'message' event.
@slack.RTMClient.run_on(event="message")
def message(**payload):
    """Display the onboarding welcome message after receiving a message
    that contains "start".
    """
    data = payload["data"]
    web_client = payload["web_client"]
    channel_id = data.get("channel")
    user_id = data.get("user")
    text = data.get("text")
    words = [""]
    if text:
        words = text.lower().split(" ")
    if text and  "announcements" in words:
        return get_announcements(web_client, user_id, channel_id)
    elif text and  "week" in words:
        return get_schedule(web_client, user_id, channel_id)    
    elif text and "today" in words:
        return get_today(web_client, user_id, channel_id)
    elif text and "litty" in words:
        return get_litty(web_client, user_id, channel_id)    
    elif text and "help" in words:
        return invalid_command("Here's some commands: \n \t week: this week's schedule \n \t today: today's schedule \n \t announcements : this week's announcements",web_client, user_id, channel_id)
        pass


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
    key_file = open("/home/zisheng/key.txt")
    key = key_file.read()
    slack_token = key
    rtm_client = slack.RTMClient(token=slack_token, ssl=ssl_context)
    rtm_client.start()
