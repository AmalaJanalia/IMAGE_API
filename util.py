# def url_to_image(url):
#     pass
# def image_to_base64(image):
#     pass

import os
import base64
base_path = "/Users/fariq/Desktop/data_prj/image_api/image/renamed_images"
def get_image_as_binary(image_number):
    image_path = os.path.join(
        base_path,
        f"{image_number}.jpg"
    )

    with open(image_path, "rb") as image_file:
        image_binary = image_file.read()

    return image_binary



def convert_to_base64(data):
   
    base64_bytes = base64.b64encode(data)

    return base64_bytes.decode("utf-8")