# add_text_watermark
A python script for adding text watermark on bottom right

# Environment
- OS : MacOS 10.13.6
- Language: Python 3.6.4
- pillow: 5.3.0

# Prerequisite
- Create a .py file `setting.py` within following lines
```python
text_watermark = 'Your text watermark(now only support English)'
```
along with the file README.md.

- solve dependency issue
```
$ pip3 install pillow==5.3.0
```

# Usage
```
usage: watermark.py [-h] -i IMAGES [IMAGES ...] [-o]

Add text watermark on the bottom right of the image.

optional arguments:
  -h, --help            show this help message and exit
  -i IMAGES [IMAGES ...], --images IMAGES [IMAGES ...]
                        The image file you wanna add text watermark(support
                        multiple files)
  -o, --override        Pass this option which means you want to override the
                        original image file
```
  
# Demo
```bash
$ python3 watermark.py -i 1.png -o
```
![](demo.jpeg)


# Reference
- [1](http://turboagram.com/FiEe)
- [2](http://turboagram.com/FiHD)
