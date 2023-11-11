import os
from PIL import Image

sprites_folder = "E:\\sprites to merge\\"
output_file_name = "output"
maximal_row_len = 10

files = os.listdir(sprites_folder)

x_max_size = 0
y_max_size = 0

for i in files:
    with Image.open(sprites_folder + i) as img:
        if img.size[0] > x_max_size:
            x_max_size = img.size[0]
        if img.size[1] > y_max_size:
            y_max_size = img.size[1]

result = Image.new('RGBA',
                   (min(maximal_row_len, len(files)) * x_max_size, (len(files) // maximal_row_len + 1) * y_max_size),
                   (0, 0, 0, 0))

for i in range(len(files)):
    with Image.open(sprites_folder + files[i]) as img:
        result.paste(img,
                     (i % maximal_row_len * x_max_size + (x_max_size - img.size[0]) // 2,
                      i//maximal_row_len * y_max_size + (y_max_size - img.size[1]) // 2))

result.save(output_file_name + ".png")
