from django.utils.html import format_html


def show_image(self, obj):
    """Возвращает html строку с данными для изображения."""
    image_data = {
        'image_url': obj.image.url,
        'max_height': 200,
        'max_width': 200,
    }

    formatted_image = format_html(
        '<img src="{image_url}" width="auto" height="auto" '
        'style="max-height:{max_height}px; max-width:{max_width}px" />',
        **image_data,
    )
    return formatted_image
