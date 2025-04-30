from django import template


register = template.Library()

@register.filter
def model_name(obj):
    """ Фильтр для шаблона возвращает имя модели объекта либо None """
    try:
        return obj._meta.model_name
    except AttributeError:
        return None
    