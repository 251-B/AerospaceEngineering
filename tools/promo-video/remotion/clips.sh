#!/bin/bash
# writes src/clips.json with frame counts of every clip (600 placeholder if not yet recorded)
cd "$(dirname "$0")"
[ -e public/clips ] || ln -s ../../recorder/clips public/clips
names="desktop-hub desktop-search desktop-theory desktop-problems desktop-askai desktop-palettes desktop-focus desktop-timer desktop-sources desktop-trio tablet-trio tablet-materials tablet-askai mobile-trio mobile-problems mobile-timer mobile-theme"
echo "{" > src/clips.json; first=1
for n in $names; do f=public/clips/$n.mp4
  c=; if [ -f "$f" ]; then c=$(ffprobe -v error -count_packets -select_streams v -show_entries stream=nb_read_packets -of csv=p=0 "$f" 2>/dev/null); fi; [ -n "$c" ] || c=600
  [ $first = 1 ] || echo "," >> src/clips.json; first=0; printf '  "%s": %s' $n $c >> src/clips.json; done
echo "}" >> src/clips.json; cat src/clips.json
