from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
<b>Hello {}!!!

This Bot Is Under Maintenance.Ask To The <a href='https://t.me/vivek2k6'>Owner</a> For More Information📜.</b>
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⚙️Support Group⚙️', url='https://t.me/vkp_bots')
        ]]
    )
