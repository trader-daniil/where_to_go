from django.utils.safestring import mark_safe
import traceback


def show_image(self, obj):
    """Отображает изображение объекта."""
    width = obj.image.width
    height = obj.image.height
    try:
        return mark_safe(
            f'<img src="{obj.image.url}" width="{width}" height="{height}" '
            'style="max-height:200px; max-width:300px" />',
        )
    except Exception:
        print(traceback.format_exc())