# Advanced Notification Sender

This Home Assistant custom integration allows you to send both TTS and text notifications
to either all device trackers or to all devices belonging to a specific person entity.

## Features

- Sends TTS and text messages to mobile devices
- Target specific person entities or all devices
- Configurable channels and priorities
- Supports config_flow for integration visibility

## Installation

1. Copy the contents of `custom_components/advanced_notification_sender/` into your Home Assistant `custom_components` folder
2. Restart Home Assistant
3. Add the integration from the UI (Settings → Devices & Services → Add Integration)
4. Call the service `advanced_notification_sender.send` from Developer Tools or automations

## Example Service Call

```yaml
service: advanced_notification_sender.send
data:
  mode: person
  person: person.john
  tts_text: "Emergency Alert"
  tts_message_channel: "alarm"
  text_message: "Check the front door"
  text_message_channel: "notification"
```
