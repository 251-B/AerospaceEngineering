#!/bin/bash
# Render -> detect paint-defect frames -> re-render only those -> repeat until clean -> encode.
# Headless Chrome occasionally screenshots a frame before every raster tile of the
# zoomed device screens is painted (a device or a tile goes missing for one frame).
# The defect lands on different frames each run, so re-rendering a flagged frame fixes it.
set -e
cd "$(dirname "$0")"
SEQ='out/frames/element-%04d.jpeg'
npx remotion bundle src/index.ts --out-dir=build --log=error
rm -rf out/frames
npx remotion render build Promo out/frames --sequence --image-format=jpeg --jpeg-quality=95 --concurrency=4 --log=error
for round in 1 2 3 4 5 6; do
  bad=$(python3 check_frames.py "$SEQ" 90 | python3 -c "import sys,json; print(' '.join(map(str, json.load(sys.stdin)['bad'])))")
  echo "round $round: frames to re-render: ${bad:-none}"
  [ -z "$bad" ] && break
  node repair.mjs out/frames $bad
done
ffmpeg -loglevel error -y -framerate 60 -i "$SEQ" -i public/soundtrack.wav -map 0:v -map 1:a \
  -c:v libx264 -preset slow -crf 19 -pix_fmt yuv420p -profile:v high -level 4.2 -r 60 -movflags +faststart \
  -af "afade=t=in:d=0.33" -c:a aac -b:a 192k -shortest out/promo-aerospace.mp4
python3 check_frames.py out/promo-aerospace.mp4 90
