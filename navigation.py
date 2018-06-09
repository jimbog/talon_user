from talon.voice import Context, Key

ctx = Context('navigation')

keymap = {
    # Requires activation of System Preferences -> Shortcuts -> Input Sources
    # -> "Select the previous input source"
    # 'change language': Key('ctrl-space'),

    # Application navigation
    'launcher': Key('cmd-space'),
    'swick': Key('cmd-tab'),
    'tab close': Key('cmd-w'),
    'window new': Key('cmd-n'),
    'window close': Key('cmd-shift-w'),
    '(window next | gibby)': Key('cmd-`'),
    '(window last | shibby)': Key('cmd-shift-`'),
    'window space right': Key('cmd-alt-ctrl-right'),
    'window space left': Key('cmd-alt-ctrl-left'),

    # Following three commands should be application specific
    'tab last': Key('cmd-shift-['),
    'tab next': Key('cmd-shift-]'),
    'tab new': Key('cmd-t'),
    'tab reload': Key('cmd-r'),

    # deleting
    'junk': Key('backspace'),
    'scrap': Key('delete'),
    'kite': Key('alt-delete'),
    'snip left': Key('cmd-shift-left delete'),
    'snip right': Key('cmd-shift-right delete'),
    'slurp': Key('backspace delete'),
    'trough': Key('alt-backspace'),

    # moving
    '(tab | tarp)': Key('tab'),
    'tarsh': Key('shift-tab'),
    'slap': [Key('cmd-right enter')],
    'locky': Key('alt-left'),
    'rocky': Key('alt-right'),
    'ricky': Key('cmd-right'),
    'lefty': Key('cmd-left'),
    'jeep': Key('up'),
    'lloyd':  Key('left'),
    'chris': Key('right'),
    'doom':  Key('down'),
    'doom way': Key('cmd-down'),
    'jeep way': Key('cmd-up'),

    # selecting
    'snatch': Key('cmd-x'),
    'shackle': [Key('cmd-left'), Key('shift-cmd-right')],
    'stoosh': Key('cmd-c'),
    'spark': Key('cmd-v'),
    'shreepway': Key('cmd-shift-up'),
    'shroomway': Key('cmd-shift-down'),
    'shreep': Key('shift-up'),
    'shroom': Key('shift-down'),
    'lecksy': Key('cmd-shift-left'),
    'ricksy': Key('cmd-shift-right'),
    'shlocky': Key('alt-shift-left'),
    'shrocky': Key('alt-shift-right'),
    'shlicky': Key('shift-left'),
    'shricky': Key('shift-right'),
}

keymap.update({'tab %s' % v: Key('cmd-%s' % v) for v in range(1, 10)})
ctx.keymap(keymap)
