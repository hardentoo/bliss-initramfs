#!/usr/bin/env python

# Copyright (C) 2012, 2013 Jonathan Vasquez <jvasquez1011@gmail.com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os
from subprocess import check_output

# Enable/Disable Hook
use_lvm = "0"

lvm = check_output("whereis lvm | cut -d ' ' -f 2", universal_newlines=True, shell=True).strip()

if os.path.isfile(lvm + ".static"):
	lvm_bins = [ lvm + ".static" ]
elif os.path.isfile(lvm):
	lvm_bins = [ lvm ]
else:
	lvm_bins = []