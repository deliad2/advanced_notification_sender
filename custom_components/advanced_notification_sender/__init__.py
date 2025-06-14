import logging
from homeassistant.core import HomeAssistant, ServiceCall

_LOGGER = logging.getLogger(__name__)
DOMAIN = "advanced_notification_sender"

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    async def handle_send(call: ServiceCall):
        mode = call.data.get("mode")
        person = call.data.get("person")
        tts_text = call.data.get("tts_text")
        tts_channel = call.data.get("tts_message_channel")
        text_message = call.data.get("text_message")
        text_channel = call.data.get("text_message_channel")

        if mode == "person" and person:
            entity = hass.states.get(person)
            trackers = entity.attributes.get("device_trackers", []) if entity else []
        else:
            trackers = [state.entity_id for state in hass.states.async_all("device_tracker")]

        for tracker in trackers:
            notify_target = tracker.replace("device_tracker.", "")
            service_name = f"notify.{notify_target}"

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

    hass.services.async_register(DOMAIN, "send", handle_send)
    return True
