# Advanced Notification Sender

Custom Home Assistant integration to send both TTS and text messages to either:
- All `device_tracker` devices in the system
- Only those linked to a specific `person` entity

## 📤 Service: `advanced_notification_sender.send`

### Fields:
- `mode`: `"person"` or `"all"`
- `person`: Optional if `mode` is `"person"` (e.g., `person.david_levi`)
- `tts_text`: Text to be spoken
- `tts_message_channel`: Channel name for TTS
- `text_message`: Regular message
- `text_message_channel`: Channel name for text

## 🚀 Installation
1. Extract to: `/config/custom_components/advanced_notification_sender/`
2. Restart Home Assistant
3. Call the service: `advanced_notification_sender.send`

MIT License.