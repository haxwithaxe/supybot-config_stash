""" commits config changes to a git repo and pushes them to a repo server
Copyright (c) 2013, haxwithaxe
All rights reserved.
See LICENSE file.
"""

import supybot
import supybot.world as world

__version__ = "0.1"

__author__ = "haxwithaxe"

__license__ = "GPLv3"

# This is a dictionary mapping supybot.Author instances to lists of
# contributions.
__contributors__ = {}

# This is a url where the most recent plugin package can be downloaded.
__url__ = "https://github.com/haxwithaxe/supybot-config_stash"

import config
import plugin
reload(plugin) # In case we're being reloaded.
# Add more reloads here if you add third-party modules and want them to be
# reloaded when this plugin is reloaded.  Don't forget to import them as well!

if world.testing:
    import test

Class = plugin.Class
configure = config.configure

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
