###
# Copyright (c) 2013, haxwithaxe
# All rights reserved.
###

import supybot.conf as conf
import supybot.registry as registry

def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified himself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('Config_stash', True)


Config_stash = conf.registerPlugin('Config_stash')
# This is where your configuration variables (if any) should go.  For example:
conf.registerGlobalValue(Config_stash, 'ssh_key',
    registry.String(None, """Path to ssh key."""))

conf.registerGlobalValue(Config_stash, 'git_remote',
            registry.String(None, """URI of the remote repo."""))


conf.registerGlobalValue(Config_stash, 'git_executable',
            registry.String('/usr/bin/git', """Path to the git executable."""))

conf.registerGlobalValue(Config_stash, 'git_local',
                    registry.String(None, """Path to the local git repository."""))

conf.registerGlobalValue(Config_stash, 'commit_message',
                    registry.String('''automatic commit from supybot plugin;
                    configs modified, please see diff.''', '''Commit message for
                    bot to use when it commits changes automatically.'''))

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
