from imagekitio import ImageKit
import base64

imagekit = ImageKit(
    private_key='private_BFhun5hz81oG3qs3thQP6WDqXAg=',
    public_key='public_gIFBuShSoi89fkHhYGGx2TyFsHM=',
    url_endpoint = 'https://ik.imagekit.io/epimage21/'
)

with open("C:/Users/Abitol 18/Pictures/coverimage.jpg", "rb") as img:
    imgstr = base64.b64encode(img.read())

upload_result = imagekit.upload_file(
    file= imgstr, 
    file_name= "coverimage.jpg", 
    options= {
        "folder" : "/example-folder/",
        "tags": ["sample-tag"],
        "is_private_file": False,
        "use_unique_file_name": True,
        "response_fields": ["is_private_file", "tags"],
    }
)

print(upload_result)
