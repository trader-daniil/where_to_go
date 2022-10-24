from django.utils.html import format_html


def show_image(self, obj):
    """Возвращает html строку с данными для изображения."""
    image_data = {
        'width': obj.image.width,
        'height': obj.image.height,
        'image_url': obj.image.url,
    }
 
    formated_image = format_html(
        '<img src="{image_url}" width="{width}" height="{height}" '
        'style="max-height:200px; max-width:300px" />',
        **image_data,
    )
    return formated_image
