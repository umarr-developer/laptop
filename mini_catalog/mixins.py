class TitleMixin:
    title: str

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context
