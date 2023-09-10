from mini_catalog.models import Categories


class BaseMixin:

    def get_context_data(self, **kwargs) -> dict[str, any]:
        return {'categories': Categories.objects.all()}
