import logging
import voluptuous as vol
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.typing import ConfigType

_LOGGER = logging.getLogger(__name__)
DOMAIN = "advanced_notification_sender"

SERVICE_SEND = "send"

SEND_SCHEMA = vol.Schema({
    vol.Required("mode"): vol.In(["all", "person"]),
    vol.Optional("person"): cv.entity_id,
    vol.Required("tts_text"): cv.string,
    vol.Required("tts_message_channel"): cv.string,
    vol.Required("text_message"): cv.string,
    vol.Required("text_message_channel"): cv.string,
})

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:

    async def handle_send(call: ServiceCall):
        mode = call.data["mode"]
        person = call.data.get("person", None)
        tts_text = call.data["tts_text"]
        tts_channel = call.data["tts_message_channel"]
        text_message = call.data["text_message"]
        text_channel = call.data["text_message_channel"]

        if mode == "person" and person:
            trackers = hass.states.get(person).attributes.get("device_trackers", [])
        else:
            trackers = [state.entity_id for state in hass.states.async_all("device_tracker")]

        for tracker in trackers:
            notify_target = tracker.replace("device_tracker.", "")
            service_name = f"notify.{notify_target}"

            # TTS
            await hass.services.async_call(
                "notify", notify_target,
                {
                    "message": "TTS",
                    "data": {
                        "ttl": 0,
                        "importance": "high",
                        "priority": "high",
                        "tts_text": tts_text,
                        "media_stream": "alarm_stream",
                        "channel": tts_channel
                    }
                },
                blocking=True
            )

            # Text
            await hass.services.async_call(
                "notify", notify_target,
                {
                    "message": text_message,
                    "data": {
                        "ttl": 0,
                        "importance": "high",
                        "priority": "high",
                        "media_stream": "alarm_stream",
                        "channel": text_channel
                    }
                },
                blocking=True
            )

    hass.services.async_register(DOMAIN, SERVICE_SEND, handle_send, schema=SEND_SCHEMA)
    return True