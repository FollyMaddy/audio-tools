# audio-tools
For now, audacity label changing for audio-files


Program : audacity-label-changer.py

Version : 1.3

Use : 

Makes files from an existing labelfile (containing points).

Converts this into tracks for use in audacity.

Also makes a conversion into tracks in hh:mm:ss format,

for FFmpeg program based splitting.

Example txt in :

2,640000	2,640000	1

513,684675	513,684675	2

847,240000	847,240000	3

1101,087761	1101,087761	4

1414,390000	1414,390000	5

1851,758419	1851,758419	6

2244,480000	2244,480000	7

2569,040000	2569,040000	8

2830,303492	2830,303492	9

Example txt out for audacity:

2,640000	513,684675	1

513,684675	847,240000	2

847,240000	1101,087761	3

1101,087761	1414,390000	4

1414,390000	1851,758419	5

1851,758419	2244,480000	6

2244,480000	2569,040000	7

2569,040000	2830,303492	8

Example txt out for FFmpeg program based splitting:

0:00:03	0:08:34	1

0:08:34	0:14:07	2

0:14:07	0:18:21	3

0:18:21	0:23:34	4

0:23:34	0:30:52	5

0:30:52	0:37:24	6

0:37:24	0:42:49	7

0:42:49	0:47:10	8


I will try to add more programs to this repository.
