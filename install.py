#!/usr/bin/env python3

import gi
import os
import sys
import locale
import json
import time
import requests
import subprocess
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib, Gio
from locale import gettext as tr

# Tərcümə məlumatları
APPNAME = "turan-helper"
TRANSLATIONS_PATH = "/usr/share/locale"
SYSTEM_LANGUAGE = os.environ.get("LANG")

# Tərcümə funksiyaları
locale.bindtextdomain(APPNAME, TRANSLATIONS_PATH)
locale.textdomain(APPNAME)
locale.setlocale(locale.LC_ALL, SYSTEM_LANGUAGE)

# GTK Builder
builder = Gtk.Builder()
builder.set_translation_domain(APPNAME)
tool_folder = sys.argv[1]
json_file = sys.argv[2]
builder.add_from_file("/usr/share/turan/proqramlar/turan-helper/proqramlar/"+tool_folder+"/main.glade")

window = builder.get_object("program_inswin")

title = builder.get_object("title")
wintitle = builder.get_object("title_window")
description = builder.get_object("description")
install_text = builder.get_object("install-text")
pages = builder.get_object("insstack")
window.show_all()

with open("/usr/share/turan/proqramlar/turan-helper/proqramlar/"+tool_folder+"/"+json_file) as f:
    data = json.load(f)

for item in data:
    name_json = item['name']
    description_json = item['description']
    ikon_json = item['icon']
    main_json = item['main']

class Handler():
     title.set_label(name_json)
     wintitle.set_label(name_json)
     description.set_label(description_json)

     def installprg(self, button):
         pages.set_visible_child_name("page1")
         command = "bash /usr/share/turan/proqramlar/turan-helper/proqramlar/"+tool_folder+"/"+main_json
         terminal = f"xterm -e '{command}'"
         result = subprocess.run(terminal, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
         print(result.stdout.decode())
         if result.returncode == 0:
            print("Finished")
            pages.set_visible_child_name("page2")
         else:
            print("Error")
            pages.set_visible_child_name("page3")

     def exitfinish(self, button):
         Gtk.main_quit()
 
     def exiterror(self, button):
         Gtk.main_quit()

builder.connect_signals(Handler())
Gtk.main()