#!/usr/bin/env python
#
# ******************************************************************************
#
# DISC ELITE DECRYPTION SCRIPT
#
# Written by Mark Moxon
#
# This script removes encryption and checksums from the compiled binaries for
# the main game code. It reads the encrypted "D.CODE.bin" and "T.CODE.bin"
# binaries and generates decrypted versions as "D.CODE.decrypt.bin" and
# "T.CODE.decrypt.bin"
#
# Files are saved using the decrypt.bin suffix so they don't overwrite any
# existing unprot.bin files, so they can be compared if required
#
# Run this script by changing directory to the repository's root folder and
# running the script with "python sources/elite-decrypt.py"
#
# You can decrypt specific releases by adding the following arguments, as in
# "python sources/elite-decrypt.py -rel1" for example:
#
#   -rel1   Decrypt the release from Ian Bell's site
#   -rel2   Decrypt the Stairway to Hell release
#
# If unspecified, the default is rel2
#
# ******************************************************************************

from __future__ import print_function
import sys

print()
print("BBC disc Elite decryption")

argv = sys.argv
release = 2
folder = "sth"

for arg in argv[1:]:
    if arg == "-rel1":
        release = 1
        folder = "ib-disc"
    if arg == "-rel2":
        release = 2
        folder = "sth"

# Configuration variables for D.CODE

load_address = 0x11E3
scramble_from = 0x1300
scramble_to = 0x5600
scramble_eor = 0x33

data_block = bytearray()

# Load assembled code file

elite_file = open("extracted/" + folder + "/D.CODE.bin", "rb")
data_block.extend(elite_file.read())
elite_file.close()

print()
print("[ Read    ] extracted/" + folder + "/D.CODE.bin")

# Do decryption

# SC routine, which EORs bytes between &1300 and &9FFF
# Can be reversed by simply repeating the EOR

for n in range(scramble_from, scramble_to):
    data_block[n - load_address] = data_block[n - load_address] ^ (n % 256) ^ scramble_eor

print("[ Decrypt ] extracted/" + folder + "/D.CODE.bin")

# Write output file for D.CODE.decrypt

output_file = open("extracted/" + folder + "/D.CODE.decrypt.bin", "wb")
output_file.write(data_block)
output_file.close()

print("[ Save    ] extracted/" + folder + "/D.CODE.decrypt.bin")

# Configuration variables for T.CODE

load_address = 0x11E3
scramble_from = 0x1300
scramble_to = 0x6000
scramble_eor = 0x33

data_block = bytearray()

# Load assembled code file

elite_file = open("extracted/" + folder + "/T.CODE.bin", "rb")
data_block.extend(elite_file.read())
elite_file.close()

print()
print("[ Read    ] extracted/" + folder + "/T.CODE.bin")

# Do decryption

# SC routine, which EORs bytes between &1300 and &9FFF
# Can be reversed by simply repeating the EOR

for n in range(scramble_from, scramble_to):
    data_block[n - load_address] = data_block[n - load_address] ^ (n % 256) ^ scramble_eor

print("[ Decrypt ] extracted/" + folder + "/T.CODE.bin")

# Write output file for T.CODE.decrypt

output_file = open("extracted/" + folder + "/T.CODE.decrypt.bin", "wb")
output_file.write(data_block)
output_file.close()

print("[ Save    ] extracted/" + folder + "/T.CODE.decrypt.bin")
print()
