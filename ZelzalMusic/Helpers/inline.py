from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from ZelzalMusic import BOT_USERNAME

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="• مسح •", callback_data="close")]]
)


buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="▶️", callback_data="resume_cb"),
            InlineKeyboardButton(text="⏸", callback_data="pause_cb"),
            InlineKeyboardButton(text="⏭️", callback_data="skip_cb"),
            InlineKeyboardButton(text="⏹", callback_data="end_cb"),
        ]
    ]
)


pm_buttons = [
    [
        InlineKeyboardButton(
            text="‹ اضفني الى مجموعتك ›",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="• اوامࢪ التشغيل •", callback_data="zelzal_help")],
    [
        InlineKeyboardButton(text="• مطـوࢪ البـوت •", user_id=config.OWNER_ID),
    ],
    [
        InlineKeyboardButton(text="• قنـاة السوࢪس •", url=config.SUPPORT_CHANNEL),
    ],
]


gp_buttons = [
    [
        InlineKeyboardButton(
            text="‹ اضفني الى مجموعتك ›",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton(text="• مطـوࢪ البـوت •", user_id=config.OWNER_ID),
    ],
    [
        InlineKeyboardButton(text="• قنـاة السوࢪس •", url=config.SUPPORT_CHANNEL),
    ],
]


helpmenu = [
    [
        InlineKeyboardButton(
            text="• اوامࢪ التشغيل •",
            callback_data="zelzal_cb help",
        )
    ],
    [
        InlineKeyboardButton(text="• اوامࢪ المطور •", callback_data="zelzal_cb sudo"),
        InlineKeyboardButton(text="• اوامࢪ المالك •", callback_data="zelzal_cb owner"),
    ],
    [
        InlineKeyboardButton(text="• ࢪجوع •", callback_data="zelzal_home"),
        InlineKeyboardButton(text="• مسح •", callback_data="close"),
    ],
]


help_back = [
    [InlineKeyboardButton(text="• قنـاة السوࢪس •", url=config.SUPPORT_CHANNEL)],
    [
        InlineKeyboardButton(text="• ࢪجوع •", callback_data="zelzal_help"),
        InlineKeyboardButton(text="• مسح •", callback_data="close"),
    ],
]
