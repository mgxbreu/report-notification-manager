import slack
from slack_sdk.errors import SlackApiError
import os

client = slack.WebClient(token=os.environ['SLACK_BOT_TOKEN'])


def send_message(message):
    try:
        response = client.chat_postMessage(channel='#testing', text=message)
        assert response["message"]["text"] == message
    except SlackApiError as e:
        assert e.response["ok"] is False
        assert e.response["error"] 
        print(f"Got an error: {e.response['error']}")