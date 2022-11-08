from django.utils.html import format_html


def show_image(self, obj):
    """Возвращает html строку с данными для изображения."""
    image_proportion = obj.image.width / obj.image.height
    image_data = {
        'width': obj.image.width,
        'height': obj.image.height,
        'image_url': obj.image.url,
        'max_height': 200,
        'max_width': 200 * image_proportion,
    }

    formatted_image = format_html(
        '<img src="{image_url}" width="{width}" height="{height}" '
        'style="max-height:{max_height}px; max-width:{max_width}px" />',
        **image_data,
    )
    return formatted_image
