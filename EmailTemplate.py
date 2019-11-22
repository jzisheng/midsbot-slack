from utils import *
import datetime

WEEK = {0:"Mon",1:"Tues",2:"Wed",3:"Thurs",4:"Fri"}

class EmailAnnouncement:    
    DIVIDER_BLOCK = {"type": "divider"}
    WELCOME_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Hey, :wave: Here's what I found for the announcements and schedule for this week "
            ),
        },
    }

    def __init__(self, channel):
        self.channel = channel
        self.username = "billy"
        self.icon_emoji = ":robot_face:"
        self.schedule, self.announcements = parse_email("example-email.txt")
        self.timestamp = ""
        
    def get_announcements_payload(self):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.WELCOME_BLOCK,
                self.DIVIDER_BLOCK,                
                *self._get_announcements_block(),

            ],
        }
        
    def get_schedule_payload(self):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.WELCOME_BLOCK,
                self.DIVIDER_BLOCK,
                *self._get_schedule_block(),
            ],
        }

    def get_message_payload(self):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.WELCOME_BLOCK,
                self.DIVIDER_BLOCK,
                *self._get_schedule_block(),
            ],
        }


    def get_today(self):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                *self._get_today()
            ],
        }

    
    def _get_schedule_block(self):
        text = (
            "*Schedule*"
        )
        information = (
            "{}".format(convert(self.schedule))
        )
        return self._get_task_block(text, information)

        
    def _get_announcements_block(self):
        text = (
            f"*Announcements*"
        )
        information = (
            "{}".format(convert(self.announcements))
        )
        return self._get_task_block(text, information)

    
    def _get_reaction_block(self):
        pass

    def _get_pin_block(self):
        return self._get_task_block(text, information)


    def _get_today(self):
        d = datetime.datetime.today()
        day = datetime.datetime.today().weekday()
        sw = sched_to_week(self.schedule)        
        try:
            return self._get_task_block("*Here's whats today for {}/{}*"\
                                        .format(d.month,d.day)\
                                        ,sw[day+1])
        except IndexError:
            return self._get_task_block("*I couldn't find anything for today*","Sorry about that, if you think this isn't right please feel free to reach out to Jason.")            
            pass
        
    
    @staticmethod
    def _get_checkmark(task_completed: bool) -> str:
        pass

    @staticmethod
    def _get_task_block(text, information):
        return [
            {"type": "section", "text": {"type": "mrkdwn", "text": text}},
            {"type": "section", "text": {"type": "mrkdwn", "text": information} },
        ]

    

    

