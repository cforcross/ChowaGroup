
import bleach
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
import random
import os

def bleach_validator(text):
    cleaned_text = bleach.clean(text, strip=True, strip_comments=True, tags=[], attributes=[], styles=[])
    text = re.sub('[\r]','',text)
    cleaned_text = re.sub('&amp;','&',cleaned_text)
    if cleaned_text != text: #\r : \n , &amp : &
        raise ValidationError(
            gettext('Field cannot contain html tags.'),
            code='invalid'
        )

def email_validator(text):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if not re.search(regex, text):
        raise ValidationError(
            gettext('Invalid email structure.'),
            code='invalid'
        )

# # Enables checking for inclusion of a symbol in user passwords
# # (called in settings).
# class SymbolValidator(object):

#     def validate(self, password, user=None):

#         if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
#             raise ValidationError(
#                 gettext("The password must contain at least 1 symbol: " +
#                   "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?."),
#                 code='password_no_symbol',)

#     def get_help_text(self):

#         return gettext(
#             "Your password must contain at least 1 symbol: " +
#             "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?.")

class CustomPasswordValidator():
    
    def __init__(self, min_length=1):
        self.min_length = min_length

    def validate(self, password, user=None):
        special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
        if not any(char.isdigit() for char in password):
            raise ValidationError(_('Password must contain at least %(min_length)d digit.') % {'min_length': self.min_length})
        if not any(char.isalpha() for char in password):
            raise ValidationError(_('Password must contain at least %(min_length)d letter.') % {'min_length': self.min_length})
        if not any(char in special_characters for char in password):
            raise ValidationError(_('Password must contain at least %(min_length)d special character.') % {'min_length': self.min_length})

    def get_help_text(self):
        return ""

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    # print(instance)
    #print(filename)
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
            new_filename=new_filename, 
            final_filename=final_filename
            )

def category_upload_image_path(instance, filename):
    # print(instance)
    #print(filename)
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "category/{new_filename}/{final_filename}".format(
            new_filename=new_filename, 
            final_filename=final_filename
            )