#RUN pip install imagekit
#to install the SDK
#import it into your project like in the line below
from imagekitio import ImageKit


#initialize the module with your Keys
imagekit = ImageKit(
    private_key='private_BFhun5hz81oG3qs3thQP6WDqXAg=',
    public_key='public_gIFBuShSoi89fkHhYGGx2TyFsHM=',
    url_endpoint = 'https://ik.imagekit.io/epimage21/'
)


imagekit_url = imagekit.url({
            "path": "/default-image.jpg",
            "url_endpoint": "https://ik.imagekit.io/epimage21/",
            "transformation": [{"height": "300", "width": "400"}],
        }
)
#print(imagekit_url)

#list files in imagekit image library
listmyfiles = imagekit.list_files({})
print(listmyfiles)

#get file details
file_id = listmyfiles['response'][0]['fileId']

image_file_details = imagekit.get_file_details(file_id)
#print(image_file_details)

#get file metadata
file_metadata = imagekit.get_file_metadata(file_id=listmyfiles['response'][1]['fileId'])
#print(file_metadata)