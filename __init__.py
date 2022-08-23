# Copyright 2022 Derek Antrican
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#    http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from mycroft import MycroftSkill, intent_file_handler
import requests

class GroceryWebhookSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
    
    def initialize(self):
        self.settings_change_callback = self.on_settings_changed
        self.on_settings_changed()

    def on_settings_changed(self):
        self.webhook_url = self.settings.get('webhook_url')
        self.http_method = self.settings.get('http_method')
        self.log.info(f"Settings changed! \n\tNew method: {self.http_method} \n\tNew webhook: {self.webhook_url}")

    @intent_file_handler('add.intent')
    def enquire_new_email(self, message):
        item = message.data.get('item').lower()
        
        # Todo: validate webhook_url & http_method by checking "" or None

        self.log.info(f"Making a {self.http_method} request to {self.webhook_url} with {item}")

        try:
            if self.http_method == "post":
                requests.post(self.webhook_url, data = item)
            elif self.http_method == "get":
                requests.get(self.webhook_url, data = item)
        except Exception as e:
            self.log.exception(f"Exception occured when trying to call webhook: {str(e)}")

        # Todo: report any errors
        self.speak_dialog("added", data={"item": item})


def create_skill():
    return GroceryWebhookSkill()