from talon.voice import Context, Key, press, Str
from talon import applescript
from user.utils import parse_words_as_integer

# It is recommended to use this script in tandem with Vimium, a Google Chrome plugin for controlling the browser via keyboard
# https://vimium.github.io/

websites = {
    'facebook': 'https://facebook.com',
    'twitter': 'https://twitter.com',
    'trello': 'https://trello.com',
    'gmail': 'https://gmail.com',
    'get hub': 'https://github.com',
    'talon docs': 'https://github.com/dwighthouse/unofficial-talonvoice-docs',
    'talon official docs': 'https://talonvoice.com/docs/index.html',
}

context = Context('GoogleChrome', bundle='com.google.Chrome')

context.set_list('websites', websites.keys())

def open_website(m):
    name = str(m._words[1])
    w = websites.get(name)
    code = r'''
    tell application "Google Chrome"
	set t to make new tab at end of tabs of window 1
	set URL of t to "%s"
    end tell
    ''' % w
    applescript.run(code)

keymaps = {
  'back': Key('cmd-['),
  'forward': Key('cmd-]'),
  'website {GoogleChrome.websites}': open_website,
}

context.keymap(keymaps)
