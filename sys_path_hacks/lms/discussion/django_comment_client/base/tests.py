from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('lms.djangoapps', 'discussion.django_comment_client.base.tests')

from lms.djangoapps.discussion.django_comment_client.base.tests import *
