#!/usr/env/python
import os

INFILE = "file.in"
OUTFILE = "file.out"

FRAME_SIZE = 956
RANDOM_BYTES = (1024*250)

f2 = open(INFILE)
f2_size = os.path.getsize(INFILE)
f = open(OUTFILE, "w+")

header="\xff\xfb\xe4\x44"
res = ''

while True:
	content = f2.read(FRAME_SIZE)
	zeros = f2.tell() % FRAME_SIZE
	res+=header+content+"\x00"*zeros
	if f2.tell() == f2_size:
		break

f.write(res)
f.close()