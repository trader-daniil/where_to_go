html_image_link = '<img src="{image_url}" width="{width}" height="{height}" style="max-height:200px; max-width:300px" />'
image_data = {
    'width': 150,
    'height': 200,
    'image_url': '/media/image.png',
}
print(html_image_link.format(**image_data))