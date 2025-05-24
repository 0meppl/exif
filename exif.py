from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_exif_data(image_path):
    image = Image.open(image_path)
    exif_data_raw = image._getexif()
    exif_data = {}

    if not exif_data_raw:
        print("No EXIF-data found.")
        return exif_data

    for tag_id, value in exif_data_raw.items():
        tag = TAGS.get(tag_id, tag_id)
        if tag == "GPSInfo":
            gps_data = {}
            for t in value:
                sub_tag = GPSTAGS.get(t, t)
                gps_data[sub_tag] = value[t]
            exif_data["GPSInfo"] = gps_data
        else:
            exif_data[tag] = value

    return exif_data
image_path = ""  # image

exif = get_exif_data(image_path)

for tag, value in exif.items():
    print(f"{tag}: {value}")
