from configparser import ConfigParser


# path to vocabulary base
VOC_PATH = 'vocabulary.txt'
# path to repeat log
REPEAT_LOG_PATH = 'repeat_log.json'
# path to self examples base
SELF_EX_PATH = 'self_examples.txt'
# path to irregular verbs base
IRREGULAR_VERBS_PATH = '..\\..\\data\\user_data\\Irregular_verbs.txt'

# Word-docs path
DOC_FOLDER = '..\\..\\data\\user_data\\docx'
# Excel-docs path
TABLE_FOLDER = '..\\..\\data\\user_data\\\\xlsx'
# PDF-docs path
PDF_FOLDER = '..\\..\\data\\user_data\\\\pdf'
# restore files path
RESTORE_FOLDER_PATH = '..\\..\\data\\user_data\\\\restore'

# standard date output format
DATEFORMAT = '%d.%m.%Y'

# divider for output WordsPerDay items
DIVIDER = '_' * 50

# отступ в поиске при нескольких айтемах из одного дня
S_TAB = '\n\t\t\t'

# path to GUI of repeat module
MAIN_WINDOW_PATH = 'E:\\Files\\Python\\PythonProjects\\Vocabulary\\src\\repeat\\ui\\MainWindow.ui'
EXAMPLES_WINDOW_PATH = 'E:\\Files\\Python\\PythonProjects\\Vocabulary\\src\\repeat\\\\ui\\ExamplesWindow.ui'
MESSAGE_WINDOW_PATH = 'E:\\Files\\Python\\PythonProjects\\Vocabulary\\src\\repeat\\\\ui\\MessageWindow.ui'
SHOW_WINDOW_PATH = 'E:\\Files\\Python\\PythonProjects\\Vocabulary\\src\\repeat\\\\ui\\ShowWindow.ui'

# repeating mods for eng
ENG_REPEAT_MODS = {
    'original_word_to_native_defs': 1,
    'native_def_to_original_words': 2,
    'original_def_to_native_defs': 3,
    'native_def_to_original_defs': 4
}

# repeating mods for rus
RUS_REPEAT_MODS = {
    'word_to_defs': 1,
    'defs_to_word': 2
}

# URL and model of synonyms searching
SYNONYMS_SEARCH_URL = 'https://rusvectores.org/{model}/{word}/api/json/'
SYNONYMS_SEARCH_MODEL = 'tayga_upos_skipgram_300_2_2019'

ID_LENGTH = 16

# If modifying these scopes, delete the file token.pickle
SCOPES = ['https://www.googleapis.com/auth/drive']
# path to token to Drive
TOKEN_PATH = 'E:\\Files\\Python\\PythonProjects\\Vocabulary\\data\\program_data\\token.pickle'
# path to credentials to log in to Drive
CREDS_PATH = 'E:\\Files\\Python\\PythonProjects\\Vocabulary\\data\\program_data\\credentials.json'
# folder name in Drive to backup
BACKUP_FOLDER_NAME = 'backup'

# URL of National Corpus of Russian Language
CORPUS_URL = "http://processing.ruscorpora.ru/search.xml"

# English prepositions
ENG_PREPS = [
    'of', 'by', 'with', 'in', 'on', 'for', 'at', 'per', 'as',
    'about', 'into', 'from', 'under', 'over', 'around', 'towards'
]

# demanded to Drive types
mimeTypes = {
    'txt': 'text/',
    'json': 'application/json',
    'folder': 'application/vnd.google-apps.folder',
    'pdf': 'application/pdf'
}

# TODO: fix via Pathlib
_ini = ConfigParser()
_ini.read('E:\\Files\\Python\\PythonProjects\\Vocabulary\\INIT.ini')

__LANGUAGE__ = _ini['settings']['__LANGUAGE__']
__NATIVE__ = _ini['settings']['__NATIVE__']

VOC_PATH = f"E:\\Files\\Python\\PythonProjects\\Vocabulary\\data\\user_data\\\\{__LANGUAGE__}_{VOC_PATH}"
REPEAT_LOG_PATH = f"E:\\Files\\Python\\PythonProjects\\Vocabulary\\data\\user_data\\{__LANGUAGE__}_{REPEAT_LOG_PATH}"
SELF_EX_PATH = f"E:\\Files\\Python\\PythonProjects\\Vocabulary\\data\\user_data\\{__LANGUAGE__}_{SELF_EX_PATH}"