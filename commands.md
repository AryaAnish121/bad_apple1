```bash
ffmpeg -i bad_apple.mp4 -c copy -t 10 input.mp4
python main.py
cd output_img
for f in $(ls *.jpg | sort -V); do echo "file '$f'" >> list.txt; done
ffmpeg -f concat -safe 0 -i list.txt -framerate 24 -c:v libx264 -pix_fmt yuv420p ../out.mp4
cd ..
rm -rf input_img output_img input.mp4
```
