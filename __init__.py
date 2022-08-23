from mycroft import MycroftSkill, intent_file_handler


class GroceryWebhook(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('webhook.grocery.intent')
    def handle_webhook_grocery(self, message):
        item = message.data.get('item')

        self.speak_dialog('webhook.grocery', data={
            'item': item
        })


def create_skill():
    return GroceryWebhook()

