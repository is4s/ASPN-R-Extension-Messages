#!/usr/bin/env bash

# Warning: this script modifies code, including deleting files.

# This script makes the following assumptions:
#     - The firehose ASPN runner is installed and on the path as firehose_convert_aspn_yaml
#     - lcm-gen is installed and on the path

set -xe

# LCM backend appends to files
rm -rf lcm
# Regenerate LCM IDLs
ASPN_PREFIX=aspn_r firehose_convert_aspn_yaml -d lcm -o lcm -e $(pwd) --skip_core_set
# LCM backend produces meson.build for C code output of lcm-gen
rm -rf lcm/c

# Regenerate DDS IDLs
ASPN_PREFIX=aspn_r firehose_convert_aspn_yaml -d dds -o dds -e $(pwd) --skip_core_set

# Regenerate LCM source code collections
lcm-gen -p lcm/*.lcm --ppath generated/python/
lcm-gen -j lcm/*.lcm --jpath generated/java
lcm-gen -x lcm/*.lcm --cpp-hpath generated/cpp
lcm-gen -c lcm/*.lcm --c-cpath generated/c/src --c-hpath generated/c/include

# Rebuild LCM JAR
export LCM_JAR_PATH=$VIRTUAL_ENV/lib/python3.*/site-packages/share/java/lcm.jar
cd generated/
gradle
gradle compileJava
gradle jar
