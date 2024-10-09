import os
from PIL import Image, ExifTags
import json


def main():
    dirs = os.listdir("./images")
    image_arr = []
    for i in dirs:
        img = Image.open(f"./images/{i}")
        exif = img._getexif()
        if exif is None:
            print("no exif")
        else:
            d = {}
            for tag_id, value in exif.items():
                tag = ExifTags.TAGS.get(tag_id, tag_id)
                d[tag] = value
            image_arr.append({
                "imageName": i,
                "camera": str(d.get("Model")),
                "date": str(d.get("DateTime").split(" ")[0].replace(":", "-")),
                "exposureTime": str(f'1/{round(1 / d.get("ExposureTime"))}'),
                "focalLength": str(d.get("FocalLength")),
                "aperture": str(d.get("FNumber")),
            })
        img.close()
    print(json.dumps({
        "images": image_arr,
    }))


main()
