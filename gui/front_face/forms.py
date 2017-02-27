#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MGVasilev'

from front_face import *
import datetime


class HashField(forms.Form):
    hidden = forms.CharField(label='', widget=forms.HiddenInput())

    class Meta:
        # model = Post
        fields = ('hidden', )


class TextEditorWidget(forms.Form):
    txt_area = forms.CharField(label='', required=False, widget=forms.Textarea(
        attrs={'label': '', 'cols': 90, 'rows': 20, 'placeholder': "начинайте писать здесь"}))

    class Meta:
        # model = Post
        fields = ('txt_area', )


class UrlForm(forms.Form):
    url = forms.CharField(label='', max_length=128, required=False, widget=forms.TextInput(attrs={'placeholder': 'адрес'}))

    class Meta:
        # model = Post
        fields = ('url', )


class TestName(forms.Form):
    name = forms.CharField(label='', max_length=64, required=False, widget=forms.TextInput(attrs={'placeholder': 'название теста'}))

    class Meta:
        # model = Post
        fields = ('name', )


class NameForm(forms.Form):
    name = forms.CharField(label='', max_length=64, required=False, widget=forms.TextInput(attrs={'placeholder': 'имя'}))

    class Meta:
        # model = Post
        fields = ('name', )


class ChooseType(forms.Form):
    type_el = forms.CharField(label='', max_length=64, required=False, widget=forms.TextInput(attrs={'placeholder': 'тип'}))

    class Meta:
        # model = Post
        fields = ('type_el', )

class XpathForm(forms.Form):
    xpath = forms.CharField(label='', max_length=128, required=False, widget=forms.TextInput(attrs={'placeholder': 'локатор'}))

    class Meta:
        # model = Post
        fields = ('xpath',)


ArticleFormSet = formset_factory(NameForm, extra=3)
formset = ArticleFormSet(initial=[{'title': 'Django is now open source', 'pub_date': datetime.date.today(),} ])


class ChooseForm(forms.Form):
    choose = forms.ChoiceField(label='', required=False, choices=[(x, x) for x in tip_list])
    widgets = {
        'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
    }
    class Meta:
        fields = ('choose', )


class DbContentsForm(forms.Form):
    choose = forms.ChoiceField(label='', required=False, choices=[(x, x) for x in get_db_urls()])
    widgets = {
        'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
    }
    class Meta:
        fields = ('choose',)


class TestsContentsForm(forms.Form):
    choose_test = forms.ChoiceField(label='', required=False, choices=[(x, x) for x in get_scripts_list()])
    widgets = {
        'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
    }
    class Meta:
        fields = ('choose_test',)


class StandsContentsForm(forms.Form):
    choose_stand = forms.ChoiceField(label='', required=False, choices=[(x, x) for x in get_stands_list()])
    widgets = {
        'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
    }
    class Meta:
        fields = ('choose_stand',)


if __name__ == '__main__':
    # print(get_db_contents('http://10.116.93.209:9080/SVFE2/'))
    # print(get_db_urls())
    pass