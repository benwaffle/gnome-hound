#!/usr/bin/env python2
import sys
sys.path.insert(0, '/root/jhbuild')

import jhbuild.main
import jhbuild.moduleset
from jhbuild.versioncontrol.git import GitBranch
import __builtin__
import json

__builtin__.__dict__['SRCDIR'] = "/home/ben/jhbuild/checkout/jhbuild"
__builtin__.__dict__['PKGDATADIR'] = None
__builtin__.__dict__['DATADIR'] = None

config = jhbuild.config.Config(None, [])
config.interact = False
moduleset = jhbuild.moduleset.load(config)

repos = {}

for module in moduleset.modules.values():
    if isinstance(module.branch, GitBranch):
        repos[module.name] = {
            'url': module.branch.module,
            'branch': module.branch.branch or 'master'
        }

with open('config.json', 'w') as conf:
    json.dump({
        'max-concurrent-indexers': 2,
        'dbpath': '/db',
        'repos': repos
    }, conf, sort_keys=True, indent=4, separators=(',', ': '))
