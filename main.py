#!/usr/bin/env python3

import gi
import os
import locale
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
builder.add_from_file("/usr/share/turan/proqramlar/turan-helper/turan-helper.glade")

window = builder.get_object("window")
# Kategoriyaların pəncərələri
itprog = builder.get_object("it-programming")
robotic = builder.get_object("robotic")
graphic_desing = builder.get_object("graphic-desing")
video_editor = builder.get_object("video-editor")
education = builder.get_object("education")
cybersecurity = builder.get_object("cybersecurity")

itprog_pages = builder.get_object("itprog_pages")
robotic_pages = builder.get_object("robotic_pages")
graphicd_pages = builder.get_object("graphicdesing-pages")
cybersecurity_pages = builder.get_object("cybersecurity-pages")
education_pages = builder.get_object("education-pages")
videoeditor_pages = builder.get_object("videoeditor-pages")


turan_helper_about = builder.get_object("turan-helper-about")
otherservices = builder.get_object("otherservices")
window.show_all()


class Handler():
    def active_turan_helper_about(self, about):
        turan_helper_about.show_all()
    def active_otherservices(self, button):
        otherservices.show_all()

    def install_guide(self, button):
        os.system("atril /usr/share/turan/proqramlar/turan-helper/alətlər/turan-ins-az.pdf") 


    # IT | Proqramlaşdırma kategoriyası
    def it_programming_button(self, button):
        itprog.show_all()
    # Grafik dizayn kategoriyası
    def graphic_desing_button(self, button):
        graphic_desing.show_all()
    # Robototexnika kategoriyası
    def robotic_button(self, button):
        robotic.show_all()
    # Video Editor / Montaj kategoriyası
    def video_editor_montaj_button(self, button):
        video_editor.show_all()
    # Təhsil kategoriyası
    def education_button(self, button):
        education.show_all()
    # Kiber təhlükəsizlik kategoriyası
    def cyber_security_button(self, button):
        cybersecurity.show_all()


    def back_itprog(self, button):
        itprog.hide()
    def back_graphic(self, button):
        graphic_desing.hide()
    def back_robotic(self, button):
        robotic.hide()
    def back_videoeditor(self, button):
        video_editor.hide()
    def back_education(self, button):
        education.hide()
    def back_cyber(self, button):
        cybersecurity.hide()


    # Kategoriyalarda səhifələrə keçmə
    def itprog_page_next(self, button):
        current_page = itprog_pages.get_visible_child_name()
        page_list = [ "page0", "page1", "page2", "page3", "page4", "page5" ]
        current_page_index = page_list.index(current_page)
        if current_page_index < len(page_list) - 1:
            next_page = page_list[current_page_index + 1]
            itprog_pages.set_visible_child_name(next_page)
        if current_page_index == 5:
           itprog_pages.set_visible_child_name("page0")

    def graphicdesing_page_next(self, button):
        current_page = graphicd_pages.get_visible_child_name()
        page_list = [ "page0", "page1", "page2", "page3" ]
        current_page_index = page_list.index(current_page)
        if current_page_index < len(page_list) - 1:
            next_page = page_list[current_page_index + 1]
            graphicd_pages.set_visible_child_name(next_page)
        if current_page_index == 3:
           graphicd_pages.set_visible_child_name("page0")

    def cybersec_page_next(self, button):
        current_page = cybersecurity_pages.get_visible_child_name()
        page_list = [ "page0", "page1", "page2" ]
        current_page_index = page_list.index(current_page)
        if current_page_index < len(page_list) - 1:
            next_page = page_list[current_page_index + 1]
            cybersecurity_pages.set_visible_child_name(next_page)
        if current_page_index == 2:
           cybersecurity_pages.set_visible_child_name("page0")

    def education_page_next(self, button):
        current_page = education_pages.get_visible_child_name()
        page_list = [ "page0", "page1", "page2" ]
        current_page_index = page_list.index(current_page)
        if current_page_index < len(page_list) - 1:
            next_page = page_list[current_page_index + 1]
            education_pages.set_visible_child_name(next_page)
        if current_page_index == 2:
           education_pages.set_visible_child_name("page0")

    def videoeditor_next_page(self, button):
        current_page = videoeditor_pages.get_visible_child_name()
        page_list = [ "page0", "page1", "page2" ]
        current_page_index = page_list.index(current_page)
        if current_page_index < len(page_list) - 1:
            next_page = page_list[current_page_index + 1]
            videoeditor_pages.set_visible_child_name(next_page)
        if current_page_index == 2:
           videoeditor_pages.set_visible_child_name("page0")


    def robotic_page_next(self, button):
        current_page = robotic_pages.get_visible_child_name()
        page_list = [ "page0", "page1" ]
        current_page_index = page_list.index(current_page)
        if current_page_index < len(page_list) - 1:
            next_page = page_list[current_page_index + 1]
            robotic_pages.set_visible_child_name(next_page)
        if current_page_index == 1:
           robotic_pages.set_visible_child_name("page0")




    def active_glade(self, button):
        os.system("python3 /usr/share/turan/proqramlar/turan-helper/install.py glade glade.json")
    def active_qtcreator(self, button):
        os.system("python3 /usr/share/turan/proqramlar/turan-helper/install.py qtcreator qtcreator.json")
    def active_gnomebuilder(self, button):
        os.system("python3 /usr/share/turan/proqramlar/turan-helper/install.py gnome-builder gnome-builder.json")
    def active_atom(self, button):
        os.system("python3 /usr/share/turan/proqramlar/turan-helper/install.py atom atom.json")
    def active_codeblocks(self, button):
        os.system("python3 /usr/share/turan/proqramlar/turan-helper/install.py codeblocks codeblocks.json")
    def active_visualstudiocode(self, button):
        os.system("python3 /usr/share/turan/proqramlar/turan-helper/install.py visual-studio-code visual-studio-code.json")

    def active_arduino(self, button):
        os.system("python3 /usr/share/turan/proqramlar/turan-helper/install.py arduino arduino.json")
    def active_thonny(self, button):
        os.system("python3 /usr/share/turan/proqramlar/turan-helper/install.py thonny thonny.json")

    def active_gimp(self, button):
        os.system("python3 /usr/share/turan/proqramlar/turan-helper/install.py gimp gimp.json")
    def active_krita(self, button):
        os.system("python3 /usr/share/turan/proqramlar/turan-helper/install.py krita krita.json")
    def active_inkspace(self, button):
        os.system("python3 /usr/share/turan/proqramlar/turan-helper/install.py inkspace inkspace.json")
    def active_scribus(self, button):
        os.system("python3 /usr/share/turan/proqramlar/turan-helper/install.py scribus scribus.json")

    def active_metasploit(self, button):
        os.system("python3 /usr/share/turan/proqramlar/turan-helper/install.py metasploit metasploit.json")
    def active_nmap(self, button):
        os.system("python3 /usr/share/turan/proqramlar/turan-helper/install.py nmap nmap.json")
    def active_wireshark(self, button):
        os.system("python3 /usr/share/turan/proqramlar/turan-helper/install.py wireshark wireshark.json")

    def active_scratch(self, button):
        os.system("python3 /usr/share/turan/proqramlar/turan-helper/install.py scratch scratch.json")
    def active_tuxmath(self, button):
        os.system("python3 /usr/share/turan/proqramlar/turan-helper/install.py tuxmath tuxmath.json")
    def active_openboard(self, button):
        os.system("python3 /usr/share/turan/proqramlar/turan-helper/install.py openboard openboard.json")

    def active_kdenlive(self, button):
        os.system("python3 /usr/share/turan/proqramlar/turan-helper/install.py kdenlive kdenlive.json")
    def active_pitivi(self, button):
        os.system("python3 /usr/share/turan/proqramlar/turan-helper/install.py pitivi pitivi.json")
    def active_flowblade(self, button):
        os.system("python3 /usr/share/turan/proqramlar/turan-helper/install.py flowblade flowblade.json")

builder.connect_signals(Handler())
Gtk.main()
