import gtk, geany
import urllib, urllib2
import os, sys



class Chewby(geany.Plugin):

    __plugin_name__ = "Lion Cub"
    __plugin_version__ = "0.0.0.3 SubZero (Yellow Baby Coder)"
    __plugin_description__ = "Post your codes on pastebin.geany.org."
    __plugin_github__ = "https://github.com/mlleparker/DevStuff/tree/master/GeanyPy/Plugins/Lion%20Cub"
    __plugin_author__ = "Mademoiselle Parker"
    __plugin_author_github__ = "https://github.com/mlleparker"
    __plugin_author_twitter__ = "@MllePark3r"



    def __init__(self):

        #
        # Pastebin feature.
        #
        self.pastebin_item = gtk.MenuItem("[LC] Pastebin")

        self.pastebin_item.show()
        geany.main_widgets.tools_menu.append(self.pastebin_item)
        self.pastebin_item.connect("activate", self.on_pastebin_item_clicked)


        #
        # Meow feature.
        #
        self.meow_item = gtk.MenuItem("[LC] Meow touch !")

        self.meow_item.show()
        geany.main_widgets.tools_menu.append(self.meow_item)
        self.meow_item.connect("activate", self.on_meow_item_clicked)



    #
    # Method cleanup()
    # To unload the plugin.
    #
    def cleanup(self):
        self.pastebin_item.destroy()
        self.meow_item.destroy()



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
            #
            fields.append(('author', 'Lion Cub'))
            fields.append(('lexer', '%s' % geany.document.get_current().file_type.display_name.lower() if geany.document.get_current().file_type.display_name.lower() != 'aucun' else 'text'))

            request = urllib2.Request('http://pastebin.geany.org/api/', urllib.urlencode(fields))
            response = urllib2.urlopen(request)
            result = response.read()


        else:
            result = 'Aborded.'


        geany.dialogs.show_msgbox(result)



    #
    # Method on_meow_item_clicked()
    # Just for testing.
    #
    def on_meow_item_clicked(widget, data):
        geany.dialogs.show_msgbox('Meowwwwwwww !')




