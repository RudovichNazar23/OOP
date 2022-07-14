class Viber:
    messages = list()

    @classmethod
    def add_message(cls, msg):
        cls.messages.append(msg)

    @classmethod
    def remove_message(cls, msg):
        cls.messages.remove(msg)

    @staticmethod
    def set_like(msg):
        if not Message(msg).fl_like:
            Message(msg).fl_like = True
        elif Message(msg).fl_like:
            Message(msg).fl_like = False
        return Message(msg).fl_like.__dict__

    def show_last_message(self):
        pass

    def total_messages(self):
        return len(self.messages)

class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like


