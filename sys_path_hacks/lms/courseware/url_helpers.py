from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('lms.djangoapps', 'courseware.url_helpers')

from lms.djangoapps.courseware.url_helpers import *
