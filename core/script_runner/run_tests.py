#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MGVasilev'

from core.script_runner import *

basepath = path.join(dirname(abspath(__file__)), "..\\..\\features\\smart_vista_web_cases\\")


def get_scripts_list() -> list:
    """ Get list of all available tests from specified directory
    :return: list of tests names

    Doctest:
    >>> get_scripts_list()
    ['23.feature', '3056.feature', '3059.feature', '3077.feature', '4439.feature', '4447.feature']
    """
    number_name = []
    list_name_number = []
    letter_name = []
    name_without_feat = ([w[:-8] for w in [q for q in listdir(basepath) if isfile(join(basepath, q))
                                           if re.compile(r"([^\\,/,:,*,\",?,<,>,|,+,., ,]){2,12}.feature").search(q)]])
    [number_name.append(int(w)) for w in name_without_feat if w.isdigit()]
    sort_list_name = sorted(number_name)
    [list_name_number.append(str(w)+'.feature') for w in sort_list_name]
    [letter_name.append(w+'.feature') for w in name_without_feat if not w.isdigit()]
    sort_list_letter_name = sorted(letter_name)
    list_name_number.extend(sort_list_letter_name)
    return list_name_number


def get_stands_list() -> list:
    """ Get all stands URLs as a ist
    Doctest
    >>> get_stands_list()
    ['http://10.116.93.209:9080', '']
    """
    return [v.value for v in Constants.PROJECT]



# @log_it
def run_scripts(name, url, log=None, user_ip="", no_capture=True) -> tuple:
    nc = "--no-capture" if no_capture else ""
    output, err = Popen(["behave", "-D", "url={url}".format(url=url), "-D", "name={name}".format(name=name),
                         "-D", "user_ip={user_ip}".format(user_ip=user_ip),
                         "{bp}{name}".format(bp=basepath, name=name), nc],
                        stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True).communicate()
    return output.splitlines(), err.splitlines()


if __name__ == '__main__':
    run_scripts(name=r"test_5.feature", url="http://sbt-oafs-578:7001", user_ip='127')   # http://10.68.194.117:9081 http://10.116.93.209:9080
    import doctest
    doctest.testmod()
