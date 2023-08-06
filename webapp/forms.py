from django import forms
from .models import ArticleRequestAnswer, CatalogItemImage, CatalogItem, Factory, JeweleryType, ArticleRequest
from .widgets import PictureWidget


class ArticleRequestAnswerForm(forms.ModelForm):
    ArticleRequestId = forms.IntegerField(widget=forms.TextInput(attrs={'style': 'display: none'}), label="")

    class Meta:
        model = ArticleRequestAnswer
        fields = ["amount"]

    def __init__(self, *args, **kwargs):
        super(ArticleRequestAnswerForm, self).__init__(*args, **kwargs)
        self.fields['amount'].label = "Количество:"


class ArticleRequestAnswerShowForm(forms.ModelForm):
    ArticleRequestAnswerId = forms.IntegerField(widget=forms.TextInput(attrs={'style': 'display: none'}), label="")

    class Meta:
        model = ArticleRequestAnswer
        fields = ["amount"]

    def __init__(self, *args, **kwargs):
        super(ArticleRequestAnswerShowForm, self).__init__(*args, **kwargs)
        self.fields['amount'].label = "В наличии:"
        self.fields['amount'].widget.attrs['class'] = 'answer-amount'

    def show(self, model=None):
        for field in self.fields:
            self.fields[field].widget.attrs['readonly'] = True

        if model:
            self.initial['amount'] = model.amount
            self.initial['ArticleRequestAnswerId'] = model.id

        else:
            self.fields['amount'].label = ""
            self.fields['amount'].widget.attrs.update({'style': 'display: none'})


class ArticleRequestForm(forms.Form):
    field_order = ["factory", "article", "type", "size", "amount"]

    article = forms.CharField(label="Артикул:")
    size = forms.RegexField(regex=r'^([0-9,.\-/\\]+)+$',
                            label="Размер изделий:",
                            error_messages={'invalid': "Неправильный размер."}, required=False)
    amount = forms.IntegerField(label="Количество изделий:")
    factory = forms.ChoiceField(
        choices=([('', '----')] + list((i, Factory.objects.all()[i].name) for i in range(len(Factory.objects.all())))),
        label="Завод изготовитель")
    type = forms.ChoiceField(
        choices=([('', '----')] + list(
            (i, JeweleryType.objects.all()[i].name) for i in range(len(JeweleryType.objects.all())))),
        label="Тип изделия")

    def __init__(self, *args, **kwargs):
        super(ArticleRequestForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].error_messages['required'] = "Заполните это поле"

    def lock(self):
        for field in self.fields:
            self.fields[field].widget.attrs['readonly'] = True

        self.fields['factory'].choices = ((int(self.cleaned_data.get('factory')),
                                           Factory.objects.all()[int(self.cleaned_data.get('factory'))]),)
        self.fields['type'].choices = ((int(self.cleaned_data.get('type')),
                                        JeweleryType.objects.all()[int(self.cleaned_data.get('type'))]),)


class ArticleRequestShowForm(forms.ModelForm):
    field_order = ["factory", "user", "article", "type", "size", "amount"]
    user = forms.CharField()
    request_time = forms.CharField()
    answer_time = forms.CharField()
    ArticleRequestId = forms.IntegerField(widget=forms.TextInput(attrs={'style': 'display: none'}), label="")
    factory = forms.CharField()
    type = forms.CharField()

    class Meta:
        model = ArticleRequest
        fields = ["article", "size", "amount"]

    def hide_for_user(self):
        self.fields['user'].widget.attrs.update({'style': 'display: none'})
        self.fields['user'].label = ""
        self.fields['request_time'].widget.attrs.update({'style': 'display: none'})
        self.fields['request_time'].label = ""

    def hide_user(self):
        self.fields['user'].widget.attrs.update({'style': 'display: none'})
        self.fields['user'].label = ""

    def get_answer(self):
        request = ArticleRequest.objects.get(id=self.data['ArticleRequestId'])
        return request.get_answer()

    def show(self, model=None):
        if model:
            self.initial['user'] = model.user
            self.initial['article'] = model.article
            self.initial['size'] = model.size
            self.initial['amount'] = model.amount
            self.initial['factory'] = model.factory
            self.initial['type'] = model.type
            self.initial['request_time'] = str(model.created_at).split('.')[0]
            if ArticleRequestAnswer.objects.filter(request=ArticleRequest.objects.get(id=model.id)):
                last_answer = model.get_answer()
                self.initial['answer_time'] = str(last_answer.created_at).split('.')[0]
            else:
                self.initial['answer_time'] = "Ещё в обработке"
            self.initial['ArticleRequestId'] = model.id

        self.fields['user'].label = "Ник:"
        self.fields['article'].label = "Артикул:"
        self.fields['size'].label = "Размер:"
        self.fields['amount'].label = "Количество:"
        self.fields['factory'].label = "Завод изготовитель:"
        self.fields['type'].label = "Тип изделия:"
        self.fields['request_time'].label = "Время создания"
        self.fields['answer_time'].label = "Время ответа"

        for field in self.fields:
            self.fields[field].widget.attrs['readonly'] = True

        if not self.initial['size']:
            self.fields['size'].widget.attrs.update({'style': 'display: none'})
            self.fields['size'].label = ""


class CatalogItemImageForm(forms.ModelForm):
    CatalogItemImage_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    image = forms.ImageField(label='', widget=PictureWidget, required=False)

    def set_image(self, image=None, model=None):
        if image:
            self.fields['image'].initial = image
        if model:
            self.fields['image'].initial = model.image
            self.fields['CatalogItemImage_id'].initial = model.id
        return self

    class Meta:
        model = CatalogItemImage
        fields = ('image',)


class CatalogItemForm(forms.ModelForm):
    CatalogItem_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = CatalogItem
        exclude = []

    def get_images(self, model=None):
        if self.model:
            self.image_forms = list(
                    CatalogItemImageForm().set_image(model=image_model) for image_model in self.model.
                    get_images())
        if model:
            self.image_forms = list(
                CatalogItemImageForm().set_image(model=image_model) for image_model in model.
                get_images())

    image_forms = None

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields["article"].label = "Артикул"
        self.fields["size"].label = "Размер"
        self.fields["amount"].label = "Количество"

    model = None

    def show(self, model=None):
        for field in self.fields:
            self.fields[field].widget.attrs['readonly'] = True

        if model:
            self.model = model
            self.get_images()

            for field in self.fields:
                if field == 'CatalogItem_id':
                    self.initial[field] = model.__getattribute__('id')
                else:
                    self.initial[field] = model.__getattribute__(field)

            if self.initial["article"]:
                self.fields["article"].label = "Артикул"
            else:
                self.fields["article"].label = ""
            if self.initial["size"]:
                self.fields["size"].label = "Размер"
            else:
                self.fields["size"].label = ""
            if self.initial["amount"]:
                self.fields["amount"].label = "Количество"
            else:
                self.fields["amount"].label = ""

        else:
            for field in self.fields:
                self.fields[field].label = ""
                self.fields[field].widget.attrs.update({'style': 'display: none'})
