#!/usr/bin/env python3

import threading

import time
import urwid

'''

  AWESOME TITLE
  ------------------------------------------------------------
  ListView with Buttons
  < Button 1                                                 >
  < Button 1                                                 >
  < Exit                                                     >
  < Dynamically added Button                                 >



  ------------------------------------------------------------
  FOOTER
 
'''

def onExit(key):
    raise urwid.ExitMainLoop()
    
exitButton = urwid.Button("Exit")
urwid.connect_signal(exitButton, 'click', onExit)

listWalker = urwid.SimpleFocusListWalker([
    urwid.Text("ListView with Buttons"),
    urwid.Button("Button 1"),
    urwid.Button("Button 2"),
    exitButton
])

listBox = urwid.ListBox(listWalker)

header = urwid.BoxAdapter(urwid.ListBox([
    urwid.Text('AWESOME TITLE'),
    urwid.Divider('-')
]), 2)

footer = urwid.BoxAdapter(urwid.ListBox([
    urwid.Divider('-'),
    urwid.Text('FOOTER for e.g logs')
]), 5)

frame = urwid.Frame(
    urwid.AttrWrap(listBox, 'body'),
    header=header,
    footer=footer
)

wrapper = urwid.Padding(frame, left=2, right=2)

loop = urwid.MainLoop(wrapper)

# Add Button dynamically
def async():
    time.sleep(1)
    listWalker.append(urwid.Button("Dynamically added Button"))
    loop.draw_screen()
threading.Thread(target=async).start()

loop.run()
