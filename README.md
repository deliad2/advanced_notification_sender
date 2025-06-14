# Advanced Notification Sender

A custom integration for [Home Assistant](https://www.home-assistant.io/) that enables sending both **TTS** and **text** notifications to:

- All `device_tracker` entities in your system
- Or only the trackers linked to a specific `person` entity

Ideal for alerting users via **mobile_app notify services** with both spoken and visual messages.

---

## 🔧 Features

✅ Send both TTS (Text-To-Speech) and plain text messages  
✅ Choose between sending to all devices or a specific person  
✅ Integrates natively into Home Assistant as a service  
✅ Multilingual translation (English and Hebrew)  
✅ Easy to use in automations or scripts

---

## 📤 Service Provided

```yaml
service: advanced_notification_sender.send
```

### 🔹 Fields:

| Field                 | Type     | Required | Description                                    |
|----------------------|----------|----------|------------------------------------------------|
| `mode`               | string   | ✅        | `"person"` or `"all"`                          |
| `person`             | entity   | ❌        | Person entity (if `mode: person`)              |
| `tts_text`           | string   | ✅        | Text to be spoken via TTS                      |
| `tts_message_channel`| string   | ✅        | Channel for TTS notification                   |
| `text_message`       | string   | ✅        | Text message to be displayed                   |
| `text_message_channel`| string  | ✅        | Channel for the text message                   |

---

## 📦 Installation (Manual)

1. Download this repository as ZIP  
2. Extract to:  
   ```
   /config/custom_components/advanced_notification_sender/
   ```
3. Restart Home Assistant  
4. Use the service `advanced_notification_sender.send` in Developer Tools or automations

---

## 💡 Example YAML Usage

```yaml
service: advanced_notification_sender.send
data:
  mode: person
  person: person.david_levi
  tts_text: "Warning! The front door is open"
  tts_message_channel: "tts_alerts"
  text_message: "Front door was left open"
  text_message_channel: "general_notifications"
```

---

## 🌍 Translations

- ✅ English (`en.json`)
- ✅ Hebrew (`he.json`)

---

## 🧑‍💻 Author

Made by [@deliad2](https://github.com/deliad2)

Licensed under the MIT License.