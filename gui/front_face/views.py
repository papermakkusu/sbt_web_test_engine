#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Provides active contents view for every web page in GUI
"""

from front_face import ChooseForm, UrlForm, NameForm, XpathForm, csrf, check_data, save_data, render, DbContentsForm, \
    TestsContentsForm, StandsContentsForm, HashField, get_db_contents, run_scripts, get_db_urls, get_scripts_list, \
    get_stands_list, TextEditorWidget, os
from front_face.forms import ChooseType

__author__ = 'MGVasilev'


def go_page(request) -> object:
    """ /go page active contents

    :param request: incoming request
    :return: rendered web page
    """

    choose = ChooseForm()
    url_form = UrlForm()
    name = NameForm()
    xpath = XpathForm()
    status = 'Заполни все поля и нажми "Проверить"'

    service_di = {}
    service_di.update(csrf(request))
    service_di.update({'status': status, 'url': url_form, 'name': name, 'xpath': xpath, 'choose': choose})

    if request.method == 'POST':
        # url = UrlForm(request.POST, prefix="url")
        # choose = CooseForm(request.POST, prefix="choose")
        # name = NameForm(request.POST, prefix="name")
        # xpath = XpathForm(request.POST, prefix="xpath")
        body = request.body.decode('UTF-8')
        if 'btnform1' in body:
            status = check_data(url=request.POST.get('url', ''),
                                name="{marker} {name}".format(marker=request.POST.get('choose', ''),
                                                              name=request.POST.get('name', '')),
                                path=request.POST.get('xpath', ''))
            state = 'Успешная проверка.' if True in status else 'Всё плохо.'
        elif 'btnform2' in body:
            status = save_data(url=request.POST.get('url', ''),
                               name="{marker} {name}".format(marker=request.POST.get('choose', ''),
                                                             name=request.POST.get('name', '')),
                               path=request.POST.get('xpath', ''))
            state = 'Успешное сохранение.' if True in status else 'Не могу сохранить.'
        else:
            status, state = (False, '', ''), 'Что-то сломалось.'

        status = '{state} {page} {element}'.format(state=state, page=status[1], element=status[2])

        # if url.is_valid():
        choose.fields['choose'].initial = request.POST.get('choose', '')
        url_form.fields['url'].initial = request.POST.get('url', '')
        name.fields['name'].initial = request.POST.get('name', '')
        xpath.fields['xpath'].initial = request.POST.get('xpath', '')

        service_di.update({'status': status, 'url': url_form, 'name': name, 'xpath': xpath, 'choose': choose})
        request.method = 'GET'
        return render(request=request, template_name='go.html', context=service_di)

    return render(request=request, template_name='go.html', context=service_di)


def view_page(request):
    """ /view page active contents

    :param request: incoming request
    :return: rendered web page
    """
    from django import forms

    choose = DbContentsForm()
    status = ''

    service_di = {}

    choose.fields['choose'] = forms.ChoiceField(label='', required=False, choices=[(x, x) for x in get_db_urls()])

    name_el = NameForm()
    xpath_el = XpathForm()
    type_el = ChooseType()
    service_di.update(csrf(request))
    service_di.update({'choose': choose, 'status': status})

    if request.method == 'POST':
        body = request.body.decode('UTF-8')
        if 'btnform' in body:
            request.method = 'GET'
            type_el.fields['type_el'].initial = request.POST.get('type_el', '')
            name_el.fields['name'].initial = request.POST.get('name', '')
            xpath_el.fields['xpath'].initial = request.POST.get('xpath', '')
            choose.fields['choose'].initial = request.POST.get('choose', '')
            status = get_db_contents(url=request.POST.get('choose', ''), type_el= request.POST.get('type_el', ''),
                                     name_el=request.POST.get('name', ''),
                                     xpath_el=request.POST.get('xpath', ''))
            service_di.update({'status': status, 'choose': choose, 'type_el': type_el, 'name': name_el, 'xpath': xpath_el})
            return render(request=request, template_name='view.html', context=service_di)

        service_di.update({'status': status, 'choose': choose, 'type_el': type_el, 'name': name_el, 'xpath': xpath_el})
        return render(request=request, template_name='view.html', context=service_di)

    return render(request=request, template_name='view.html', context=service_di)

def run_page(request):
    """ /run page active contents

    :param request: incoming request
    :return: rendered web page
    """

    from django import forms

    choose_test = TestsContentsForm()
    choose_stand = StandsContentsForm()
    status = ''

    service_di = {}

    choose_test.fields['choose_test'] = forms.ChoiceField(label='', required=False,
                                                          choices=[(x, x) for x in get_scripts_list()])
    choose_stand.fields['choose_stand'] = forms.ChoiceField(label='', required=False,
                                                            choices=[(x, x) for x in get_stands_list()])

    service_di.update(csrf(request))
    service_di.update({'choose_test': choose_test, 'choose_stand': choose_stand, 'status': status})

    if request.method == 'POST':

        body = request.body.decode('UTF-8')
        if 'btnform' in body:
            # currently we return errors as the second list element
            status, _ = run_scripts(name=request.POST.get('choose_test', ''),
                                    url=request.POST.get('choose_stand', ''),
                                    user_ip=get_client_ip(request),)
            choose_test.fields['choose_test'].initial = request.POST.get('choose_test', '')
            choose_stand.fields['choose_stand'].initial = request.POST.get('choose_stand', '')
        service_di.update({'status': status, 'choose_test': choose_test, 'choose_stand': choose_stand})
        request.method = 'GET'
        return render(request=request, template_name='run.html', context=service_di)

    return render(request=request, template_name='run.html', context=service_di)


def text_page(request):
    """ /text page active contents

    :param request: incoming request
    :return: rendered web page
    """

    hidden = HashField()
    txt_area = TextEditorWidget()
    test_name = NameForm()
    status = ""

    service_di = {}
    service_di.update(csrf(request))
    service_di.update({'txt_area': txt_area, 'test_name': test_name, 'hidden': hidden, 'status': status})

    if request.method == 'POST':

        body = request.body.decode('UTF-8')
        file_name = request.POST.get('name', '')
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), r"..\..",
                                                 r"features\smart_vista_web_cases\{file}.feature".format(
                                                     file=file_name)))
        request.method = 'GET'

        test_name.fields['name'].initial = str(request.POST.get('name', ''))
        txt_area.fields['txt_area'].initial = str(request.POST.get('txt_area', ''))
        if test_name.fields['name'].initial == "" or len(test_name.fields['name'].initial) < 4:
            status = "Ничего не вышло. Неверное имя теста. Назовите тест по индексу из ALM."
            service_di.update({'txt_area': txt_area, 'test_name': test_name, 'hidden': hidden, 'status': status})
            return render(request=request, template_name='text.html', context=service_di)

        if 'btnform1' in body:
            txt_area.fields['txt_area'].initial = hidden.fields['hidden'].initial = read_text_data(f_path=file_path)
            status = "Такого теста пока никто не написал. У вас есть шанс." if hidden.fields['hidden'].initial == "" \
                else "Загружена свежая версия теста."
            service_di.update({'txt_area': txt_area, 'test_name': test_name, 'hidden': hidden, 'status': status})
            return render(request=request, template_name='text.html', context=service_di)

        elif 'btnform2' in body:
            txt_area.fields['txt_area'].initial = usr_text = str(request.POST.get('txt_area', ''))
            file_hash = read_text_data(f_path=file_path).encode('utf-8')
            keeped_hash = request.POST.get('hidden', '').encode('utf-8')
            if not usr_text:
                hidden.fields['hidden'].initial = usr_text
                status = "Нельзя сохранить пустой файл. Попробуйте написать что-нибудь замечательное."
                service_di.update({'txt_area': txt_area, 'test_name': test_name, 'hidden': hidden, 'status': status})
                return render(request=request, template_name='text.html', context=service_di)
            if file_hash == keeped_hash or file_hash == b"":
                write_text_data(f_path=file_path, data=usr_text)
                hidden.fields['hidden'].initial = usr_text
                status = "Тест успешно сохранился."
                service_di.update({'txt_area': txt_area, 'test_name': test_name, 'hidden': hidden, 'status': status})
            elif file_hash != b"" and keeped_hash == b"":
                hidden.fields['hidden'].initial = usr_text
                status = "Ничего не вышло. Вы не проверили обновления. Загрузите свежую версию теста."
                service_di.update({'txt_area': txt_area, 'test_name': test_name, 'hidden': hidden, 'status': status})
            else:
                status = "Ничего не вышло. Кто-то уже обновил тест. Загрузите свежую версию."
                service_di.update({'txt_area': txt_area, 'test_name': test_name, 'hidden': hidden, 'status': status})
            return render(request=request, template_name='text.html', context=service_di)
        else:
            test_name.fields['name'].initial = request.POST.get('name', '')
            service_di.update({'txt_area': txt_area, 'test_name': test_name, 'hidden': hidden, 'status': status})
            return render(request=request, template_name='text.html', context=service_di)

    return render(request=request, template_name='text.html', context=service_di)


def read_text_data(f_path) -> str:
    """ Reads text from test .feature file

    :param f_path: relative .feature test file path
    :return: str
    """
    if not os.path.exists(f_path):
        return ""
    with open(f_path, 'rb') as handle:
        try:
            return handle.read().decode('utf-8')
        except EOFError:
            return ""


def write_text_data(f_path, data) -> str:
    """ Writes to .feature test file

    :param f_path: relative .feature test file path
    :param data: data to write to file
    :return: str
    """
    if not os.path.exists(f_path):
        open(f_path, 'wb').close()
    with open(f_path, 'wb') as handle:
        handle.write(data.encode('utf-8'))
    return 'OK'


def get_client_ip(request) -> str:
    """ Reads client IP address

    :param request: incoming request
    :return: str with client IP address
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    return x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')


if __name__ == '__main__':
    # print(run_scripts(name=r"6333.feature", user_ip=127, url=r"http://10.68.194.117:9081"))
    pass
