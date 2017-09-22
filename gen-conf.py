#!/usr/bin/env python2
import sys
sys.path.insert(0, '/root/jhbuild')

import jhbuild.main
import jhbuild.moduleset
from jhbuild.versioncontrol.git import GitBranch
import __builtin__

__builtin__.__dict__['SRCDIR'] = "/home/ben/jhbuild/checkout/jhbuild"
__builtin__.__dict__['PKGDATADIR'] = None
__builtin__.__dict__['DATADIR'] = None

config = jhbuild.config.Config(None, [])
config.interact = False
moduleset = jhbuild.moduleset.load(config)

for module in moduleset.modules.values():
    sys.stdout.write(module.name + ' - ')
    if isinstance(module.branch, GitBranch):
        sys.stdout.write(module.branch.module)
    sys.stdout.write('\n')

