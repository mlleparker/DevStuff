import gtk, geany
import urllib, urllib2
import os, sys



class Chewby(geany.Plugin):

    __plugin_name__ = "Lion Cub"
    __plugin_version__ = "0.0.0.1 SubZero (Yellow Baby Coder)"
    __plugin_description__ = "Post your codes on pastebin.geany.org."
    __plugin_author__ = "Mademoiselle Parker"
    __plugin_author_github__ = "https://github.com/mlleparker"
    __plugin_author_twitter__ = "@MllePark3r"



    def __init__(self):

        self.menu_item = gtk.MenuItem("[LC] Pastebin")

        self.menu_item.show()
        geany.main_widgets.tools_menu.append(self.menu_item)
        self.menu_item.connect("activate", self.on_pastebin_item_clicked)



    #
    # Method cleanup()
    # To unload the plugin.
    #
    def cleanup(self):
        self.menu_item.destroy()



    #
    # Method on_pastebin_item_clicked()
    # Trigger to push source code to pastebin web site
    #  and get back the URL of paste.
    #
    def on_pastebin_item_clicked(widget, data):

        fields = []

        if geany.dialogs.show_question('Confirm data exfiltration please.\n\nTarget :\tpastebin.geany.org'):

            if geany.document.get_current().editor.scintilla.get_selection_contents() != '':
                fields.append(('content', geany.document.get_current().editor.scintilla.get_selection_contents()))

            else:
                fields.append(('content', geany.document.get_current().editor.scintilla.get_contents()))

            #
            # Note :
            #  You can replace 'Lion Cub' by your nickname.
            #  You can replace 'python' by python, text, php, perl, c, bash, ...
            #
            fields.append(('author', 'Lion Cub'))
            fields.append(('lexer', 'python'))

            request = urllib2.Request('http://pastebin.geany.org/api/', urllib.urlencode(fields))
            response = urllib2.urlopen(request)
            result = response.read()


        else:
            result = 'Aborded.'


        geany.dialogs.show_msgbox(result)



