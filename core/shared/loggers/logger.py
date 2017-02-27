#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MGVasilev'

from core.shared.loggers import *


ERROR_COLOR = Fore.RED + Style.BRIGHT
WRITE = 25
STEP = 28
SECTION = 29
SUCCESS = 55
NONE = 255


colors = {
    'DEBUG': Fore.BLACK + Style.BRIGHT,  # Dark text
    'SECTION': Style.RESET_ALL,  # Normal text
    'INFO': Style.RESET_ALL,  # Normal text
    'WRITE': Fore.WHITE + Style.BRIGHT,  # Bright text
    'STEP': Fore.CYAN + Style.BRIGHT,  # Bright text
    'WARNING': Fore.YELLOW + Style.BRIGHT,  # Bright yellow
    'ERROR': Fore.RED + Style.BRIGHT,  # Bright red
    'CRITICAL': Back.RED + Fore.WHITE,  # red on white
    'SUCCESS': Fore.GREEN + Style.BRIGHT  # bright green
}

levels = {
    'CRITICAL': logging.CRITICAL,
    'ERROR': logging.ERROR,
    'WARNING': logging.WARNING,
    'INFO': logging.INFO,
    'DEBUG': logging.DEBUG,
    'SECTION': SECTION,
    'WRITE': WRITE,
    'STEP': STEP,
    'SUCCESS': SUCCESS,
}


class ColoredStreamHandler(logging.StreamHandler):
    """ StreamHandler with colorama support """

    def emit(self, record):
        # noinspection PyBroadException
        try:
            message = self.format(record)
            if not record.levelname not in colors: self.stream.write(message)
            else: self.stream.write(colors[record.levelname] + message + Style.RESET_ALL)
            self.stream.write(getattr(self, 'terminator', '\n'))
            self.flush()
        except (KeyboardInterrupt, SystemExit): raise
        except: self.handleError(record)


class TestsFileHandler(logging.FileHandler):
    """ Works with log files
    """
    listener = None

    def __init__(self, filename='', mode='a', encoding=None, delay=True):
        super().__init__(filename=filename, mode=mode, encoding=encoding, delay=delay)
        if filename: os.makedirs(os.path.dirname(filename), exist_ok=True)
        else: self.baseFilename = ''

    def set_file(self, new_file):
        self.wait_for_flush()
        self.close()
        self.baseFilename = new_file

    def wait_for_flush(self):
        if self.listener is not None:
            self.listener.queue.join()

    def get_file(self):
        return self.baseFilename

    def emit(self, record):
        try:
            os.makedirs(os.path.dirname(self.baseFilename), exist_ok=True)
            super().emit(record)
        except (FileNotFoundError, NameError): pass


class TestsLogger(logging.Logger):
    """ Main logger class
    """

    buffer = []
    detailed_recording_enabled = False
    global_debug_level = None

    def make_record(self, level, msg, args, exc_info=None, extra=None, stack_info=False):
        fn, lno, func, s_info = self.findCaller(stack_info)
        if exc_info and not isinstance(exc_info, tuple):
            exc_info = sys.exc_info()
        return self.makeRecord(self.name, level, fn, lno, msg, args,
                               exc_info, func, extra, s_info)

    def log(self, level, msg, *args, **kwargs):
        if not isinstance(level, int):
            if logging.raiseExceptions: raise TypeError("level must be an integer")
            else: return
        if self.isEnabledFor(level):
            self._log(level, msg, args, **kwargs)
        elif self.detailed_recording_enabled:
            record = self.make_record(level, msg, args, **kwargs)
            self.buffer.append(record)

    def _log(self, level, msg, args, exc_info=None, extra=None, stack_info=False):
        record = self.make_record(level, msg, args, exc_info=exc_info, extra=extra, stack_info=stack_info)
        if self.detailed_recording_enabled:
            self.buffer.append(record)
        self.handle(record)

    def debug(self, msg, *args, **kwargs):
        self.log(logging.DEBUG, msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.log(logging.INFO, msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.log(logging.WARNING, msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.log(logging.ERROR, msg, *args, **kwargs)

    def exception(self, msg, *args, **kwargs):
        kwargs['exc_info'] = True
        self.log(logging.ERROR, msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        self.log(logging.CRITICAL, msg, *args, **kwargs)

    def success(self, message):
        self.log(SUCCESS, message)

    def step(self, message):
        self.log(STEP, message)

    def write(self, message):
        self.log(WRITE, message)

    @classmethod
    def set_file(cls, filename):
        try:
            cls.file_handler.set_file(filename)
        except AttributeError:
            pass

    @classmethod
    def wait_for_flush(cls):
        try:
            cls.file_handler.wait_for_flush()
        except AttributeError:
            pass

    @classmethod
    def get_file(cls):
        try:
            return cls.file_handler.get_file()
        except AttributeError:
            return ''

    @classmethod
    def start_detailed_log(cls):
        if cls.detailed_recording_enabled:
            return
        cls.buffer = []
        if cls.global_debug_level != 'full':
            cls.detailed_recording_enabled = True

    @classmethod
    def flush_detailed_log(cls, write_to_log: bool):
        """

        :param write_to_log:
        :return:
        """
        if not cls.detailed_recording_enabled:
            return
        cls.detailed_recording_enabled = False
        if not write_to_log:
            cls.buffer = []
            cls.wait_for_flush()
            return
        try:
            original_log_file = cls.file_handler.get_file()
        except AttributeError:
            cls.buffer = []
            cls.wait_for_flush()
            return
        debug_log_file = '{}.log'.format(os.path.splitext(original_log_file)[0])    # .debug.log
        cls.set_file(debug_log_file)
        for record in cls.buffer:
            cls.file_handler.emit(record)
        cls.buffer = []
        cls.set_file(original_log_file)

LOGGING_CONFIGURED = False


def set_up_logging(options=None, log_root_dir=''):
    """

    :param options:
    :param log_root_dir:
    :return:
    """

    global LOGGING_CONFIGURED
    if LOGGING_CONFIGURED:
        return

    init_colors(autoreset=True)

    logging.addLevelName(STEP, 'STEP')
    logging.addLevelName(SUCCESS, 'SUCCESS')
    logging.addLevelName(SECTION, 'SECTION')
    logging.addLevelName(WRITE, 'WRITE')

    logging.setLoggerClass(TestsLogger)

    log_fmt = '{asctime}:{levelname}:{name}> {message}'
    console_formatter = logging.Formatter(fmt=log_fmt,
                                          datefmt='%H:%M:%S',
                                          style='{')
    console_handler = ColoredStreamHandler()
    console_handler.setFormatter(console_formatter)
    console_handler.setLevel('DEBUG')

    file_formatter = logging.Formatter(fmt=log_fmt,
                                       datefmt='%Y.%m.%d %H:%M:%S',
                                       style='{')
    file_handler = TestsFileHandler()
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel('DEBUG')

    que = Queue(-1)
    queue_handler = logging.handlers.QueueHandler(que)
    TestsLogger.file_handler = file_handler
    listener = logging.handlers.QueueListener(que, file_handler, console_handler)
    TestsFileHandler.listener = listener
    listener.start()

    logger = logging.getLogger('SWTE')
    logger.addHandler(queue_handler)
    # logger.setLevel('INFO')
    # logging.getLogger('SWTE').setLevel('DEBUG')
    # logging.getLogger('SWTE').setLevel('INFO')
    # logging.getLogger('SWTE').setLevel('ERROR')
    # logging.getLogger('SWTE').setLevel('CRITICAL')

    LOGGING_CONFIGURED = True


def get_log_dir(log_root=None):
    """

    :param log_root:
    :return:
    """
    python_tests_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    root = join(python_tests_path, '../../logs')

    if log_root is not None:
        root = log_root
    return join(root, str(date.today()))


def construct_logger(test_name, alias):
    """

    :param test_name:
    :return:
    """

    set_up_logging()
    log = getLogger('SWTE.{}__{}'.format(test_name, alias))
    log_file = '{}__{}__{}.log'.format(test_name, alias, str(date.today()))
    current_log_file = log.get_file()
    log_dir = os.path.dirname(current_log_file) if current_log_file else get_log_dir()
    log_path = os.path.join(log_dir, "", log_file)
    log.set_file(log_path)
    log.start_detailed_log()
    return log


def destruct_logger(log):
    """

    :param log:
    :return:
    """
    log.flush_detailed_log(write_to_log=True)






