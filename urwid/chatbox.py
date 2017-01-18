#!/usr/bin/env python3

import threading

import time
import urwid

'''

  AWESOME TITLE
  ------------------------------------------------------------
  user1 > Hi, how are you?
  user2 > I'm fine!


  ------------------------------------------------------------
  user1 > ____________________
 
'''

class ChatInput(urwid.Edit):
    ''' Custom edit for chat-like input field '''
    _metaclass_ = urwid.signals.MetaSignals  
    signals = ['done']

    def keypress(self, size, key):
        if key == 'enter':
            urwid.emit_signal(self, 'done', self, self.get_edit_text())
            super(ChatInput, self).set_edit_text('')
        elif key == 'esc':
            super(ChatInput, self).set_edit_text('')
        else:
            urwid.Edit.keypress(self, size, key)

def createUserMessage(user, msg):
    ''' Template to create user message widgets '''
    return urwid.Text(user + ' > ' + msg)

def createSysMessage(msg):
    ''' Template to create system message widgets '''
    return urwid.Text(('sysmsg', 'sys > ' + msg))

def onSubmit(widget, text):
    listWalker.append(createUserMessage('user1', text))
    loop.draw_screen()

listWalker = urwid.SimpleFocusListWalker([
    createSysMessage("Connection established"),
    createUserMessage("user1", "Hi, how are you?")
])

listBox = urwid.ListBox(listWalker)

textEdit = ChatInput('user1 > ')
urwid.connect_signal(textEdit, 'done', onSubmit)

frame = urwid.Frame(
    urwid.AttrWrap(listBox, 'body'),
    header=urwid.BoxAdapter(urwid.ListBox([
        urwid.Text('AWESOME TITLE'),
        urwid.Divider('-')
    ]), 2),
    footer=urwid.BoxAdapter(urwid.ListBox([
        urwid.Divider('-'),
        textEdit
    ]), 5)
)

palette = [
    ('sysmsg', 'black', 'light gray', 'standout,underline', 'black,underline', '#88a')
]

loop = urwid.MainLoop(urwid.Padding(frame, left=2, right=2), palette)
loop.run()
