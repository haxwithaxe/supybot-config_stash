"""
Copyright (c) 2013, haxwithaxe
All rights reserved.
See LICENSE file.
"""

from supybot import conf, registry

def configure(advanced):
    """
    This will be called by supybot to configure this module.  advanced is
    a bool that specifies whether the user identified himself as an advanced
    user or not.  You should effect your configuration by manipulating the
    registry as appropriate.
    """
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('config_stash', True)


config_stash = conf.registerPlugin('config_stash')

# This is where your configuration variables (if any) should go.  For example:
conf.registerGlobalValue(config_stash, 'ssh_key',
    registry.String(None, """Path to ssh key."""))

conf.registerGlobalValue(config_stash, 'git_remote',
            registry.String(None, """URI of the remote repo."""))


conf.registerGlobalValue(config_stash, 'git_executable',
            registry.String('/usr/bin/git', """Path to the git executable."""))

conf.registerGlobalValue(config_stash, 'git_local',
                    registry.String(None, """Path to the local git repository."""))

conf.registerGlobalValue(config_stash, 'commit_message',
                    registry.String('automatic commit from supybot plugin; configs modified, please see diff.',
                    """Commit message for bot to use when it commits changes automatically."""))

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
