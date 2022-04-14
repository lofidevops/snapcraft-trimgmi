# trimgmi
# Copyright 2022 David Seaward
# SPDX-License-Identifier: GPL-3.0-or-later

import sys
from pathlib import Path

from trimgmi.sample import reformat_file

if __name__ == "__main__":
    output_format = str.upper(sys.argv[1])
    input_path = Path(sys.argv[2])
    output_path = Path(sys.argv[3])
    reformat_file(output_format, input_path, output_path)
