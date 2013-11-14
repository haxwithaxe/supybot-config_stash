'''
Copyright (c) 2013, haxwithaxe
All rights reserved.
See LICENSE file.
'''

import supybot.utils as utils
from supybot.commands import *
from supybot.registry import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import os
import threading
import git

def reg_get(reg, key):
    try:
        return reg.registryValue(key)
    except NonExistentRegistryEntry as e:
        return None

class Poller(threading.Thread):
    def __init__(self, plugin):
        self.git_bin = '/usr/bin/git'
        self.plugin = plugin
        self.repo = git.Repo(self._get_repo())
        self.cmd = git.cmd.Git(working_dir=self._get_repo())
        self.msg = self.plugin.registryValue('commit_message')

    def _get_repo(self):
        cwd = reg_get(self.plugin, 'git_local')
        if not cwd:
            return os.getcwd()
        return cwd

    def _has_untracked_files(self):
        return (len(self.repo.untracked_files) > 0)

    def _need_commit(self):
        return self.has_untracked_files() or self.repo.is_dirty()

    def _commit(self, msg):
        if self.need_commit():
            try:
                if self.has_untracked_files():
                    add_cmd = [self.git_bin,'add']
                    add_cmd += self.repo.untracked_files
                    self.cmd.execute(add_cmd)
                self.cmd.execute([self.git_bin,'commit','-a', '-m', msg])
            except Exception as e: #FIXME: I need to be more specific in what I catch
                print(repr(e))
                print('Continuing ...')
                return False
        return True
        

class configstash(callbacks.Plugin):
    """Add the help for "@plugin help Config_stash" here
    This should describe *how* to use this plugin."""
    threaded = True
    def __init__(self, irc):
        self.__parent = super(configstash, self)
        self.__parent.__init__(irc)
        self.poller = Poller(self)
        print('ConfigStash.__init__')


Class = configstash


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
