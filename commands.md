```bash
ffmpeg -i bad_apple.mp4 -c copy -t 10 input.mp4
python main.py
cd output_img
ffmpeg -framerate 30 -pattern_type glob -i '*.jpg' \
  -c:v libx264 -pix_fmt yuv420p ../out.mp4
cd ..
rm -rf input_img output_img input.mp4
```
