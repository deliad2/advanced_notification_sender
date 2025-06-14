import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback

from .const import DOMAIN

class AdvancedNotificationSenderConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title="Advanced Notification Sender", data={})
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({}),
            errors=errors
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return AdvancedNotificationSenderOptionsFlowHandler(config_entry)

class AdvancedNotificationSenderOptionsFlowHandler(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        return self.async_create_entry(title="", data={})
