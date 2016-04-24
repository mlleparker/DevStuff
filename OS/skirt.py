#!/usr/bin/python
#-*- coding: utf-8 -*-


########################################
## Skirt                              ##
########################################
##
## Author   : Mademoiselle Parker
## Email    : base64.b64decode('Z3dlbm5hZWxsZS5nbG9pcmVAZ21haWwuY29t')
## Torchat  :
## Jabber   :
## Ricochet : base64.b64decode('cmljb2NoZXQ6MmRzejV4NnZhczRybXJqeg==')
## Tox      : base64.b64decode('RDE5QzNFQjA3NUQ5QTk3QkU0Q0VBRDdFNzM5QzE3RDU4NkNGMTkwNEY0NDY5M0RCNTQ1NTYzMDEzOEQ2MUEwNTY5QkRFNzIxN0QzQQ==')
## Twitter  : base64.b64decode('QE1sbGVQYXJrM3JfZGV2')
## Github   : base64.b64decode('aHR0cHM6Ly9naXRodWIuY29tL21sbGVwYXJrZXI=')
##
## Version : 0.0.0.0 SubZerro
## Code name : No short !
##
## Semantic:
##  - Header  : 0.0.5.0
##  - Code    : 0.0.3.0
##  - Artcode :
##
## Licence : Free for all, commercial use
## strictly forbidden. If I catch you,
## you'll be busted ! :p
##
## Personal message : Peace in your
## hearts, stop war, stop rage, stop
## fighting, the life can be awesome :)
##
## I ᶫᵒᵛᵉᵧₒᵤ . ♥♥♥
##
########################################
## Features                           ##
########################################
##
## Skirt is a little tool to unshort
##  shorten URLs.
##
########################################
## Divers & Dev notes                 ##
########################################
##
##
##
########################################
## Changelog                          ##
########################################
##
##
##
########################################
## TODO                               ##
########################################
##
##
##
########################################
## Bug tracker                        ##
########################################
##
##
##
########################################




 #
 ##
 ### Modules & lib importations
 ########################################

import urllib2, sys
import base64





 #
 ##
 ### Import my pretty libs
 ########################################

#from lib import clistyle



 #
 ##
 ### Core var
 ########################################

__author__ = "Mademoiselle Parker"
__version__ = "0.0.0.0 SubZerro"
__codename__= "No short !"
__authormail__= base64.b64decode('Z3dlbm5hZWxsZS5nbG9pcmVAZ21haWwuY29t')
__torchat__ = ""
__twitter__ = base64.b64decode('QE1sbGVQYXJrM3I=')
__jabber__ = ""
__ricochet__ = base64.b64decode('cmljb2NoZXQ6MmRzejV4NnZhczRybXJqeg==')
__tox__ = base64.b64decode('RDE5QzNFQjA3NUQ5QTk3QkU0Q0VBRDdFNzM5QzE3RDU4NkNGMTkwNEY0NDY5M0RCNTQ1NTYzMDEzOEQ2MUEwNTY5QkRFNzIxN0QzQQ==')
__coredev__ = "Lioness Studios"
__github__ = base64.b64decode('aHR0cHM6Ly9naXRodWIuY29tL21sbGVwYXJrZXI=')
__semantic__ = {'header':{'version':'0.0.5.0'},
                'source':{'version':'0.0.3.0'},
                'artcode':{'name':''},
                }
__libmode__ = None
__nosplash__ = False


def author():
    return __author__

def version():
    return __version__

def codename():
    return __codename__

def authormail():
    return __authormail__

def torchat():
    return __torchat__

def twitter():
    return __twitter__

def jabber():
    return __jabber__

def ricochet():
    return __ricochet__

def tox():
    return __tox__

def coredev():
    return __coredev__

def github():
    return __github__

def semantic():
    return __semantic__

def libmode():
    return __libmode__

def nosplash():
    return __nosplash__



 #
 ##
 ### External library options & parameters
 ########################################

#clistyle.__printmode__ = "shell"
__skin__ = 'dark'
__skin_color__ = 'green'


def skin():
    return __skin__

def skin_color():
    return __skin_color__


#
# To replace Python prompt.
#
#sys.ps1 = clistyle.loadprompt(skin)
#sys.ps2 = clistyle.loadprompt(skin)

#
# To rotate print mode of CLIStyle.
#
def switchme(mymode):

    if mymode == "irc":

        clistyle.__printmode__ = "irc"

    elif mymode == "shell":

        clistyle.__printmode__ = "shell"



 #
 ##
 ### Source code
 ########################################

#
# Function skirt()
# To unshort URL.
#
# Var scheme:
#  url is string who defines the shorten
#   URL.
#
def skirt(url = None):

    if url:

        return urllib2.urlopen(url).url



if __name__ == '__main__':

    print '\n[>] URL : %s\n' % skirt(sys.argv[1])
