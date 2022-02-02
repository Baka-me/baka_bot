PM_START_TEXT = """
Hey there! my name is *{}*. 
A modular group management bot with useful features. [ㅤ](https://telegra.ph/file/fed9ba09e9add9b197c21.png)
◑ *Uptime:* `{}`
◑ `{}` *Users, across* `{}` *chats.*
Any issues or need help related to me?
Join our official group [IDNCoderX](https://t.me/IDNCoderX).
Click help button to know my commands!
"""

buttons = [
    [
        InlineKeyboardButton(
            text="❔  About bot",
            callback_data="HELP_BACK",
        ),
    ],
    [
        InlineKeyboardButton(
            text="Add Zeldris to Your Group 👥",
            url="t.me/ZeldrisRobot?startgroup=true",
        ),
    ],
]


HELP_BACK = BUTTON = [
        [
            Button.url("📢 Updates", "https://t.me/"),
            Button.url("🚑 Support", "https://t.me/"),
        ]
    ]
    (buttons=BUTTON)
