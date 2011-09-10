# Copyright (c) 2010-2011 Robin Jarry
# 
# This file is part of EVE Corporation Management.
# 
# EVE Corporation Management is free software: you can redistribute it and/or 
# modify it under the terms of the GNU General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at your 
# option) any later version.
# 
# EVE Corporation Management is distributed in the hope that it will be useful, 
# but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY 
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for 
# more details.
# 
# You should have received a copy of the GNU General Public License along with 
# EVE Corporation Management. If not, see <http://www.gnu.org/licenses/>.

import re

SPECIAL_CHAR_RE = re.compile(r'\\x\w\w')

def fix_encoding(s):
    """
    Replace UTF-8 character codes by their actual value.
    
    example: '\\xE9' is replaced by unicode character '\xE9' 
    """
    new_str, _ = SPECIAL_CHAR_RE.subn(repl_func, s)
    return unicode(new_str)

def repl_func(match):
    m = match.group(0)
    if m in ('\\xa1', '\\xA1'): return u'\xA1'
    elif m in ('\\xa2', '\\xA2'): return u'\xA2'
    elif m in ('\\xa3', '\\xA3'): return u'\xA3'
    elif m in ('\\xa4', '\\xA4'): return u'\xA4'
    elif m in ('\\xa5', '\\xA5'): return u'\xA5'
    elif m in ('\\xa6', '\\xA6'): return u'\xA6'
    elif m in ('\\xa7', '\\xA7'): return u'\xA7'
    elif m in ('\\xa8', '\\xA8'): return u'\xA8'
    elif m in ('\\xa9', '\\xA9'): return u'\xA9'
    elif m in ('\\xaa', '\\xAA'): return u'\xAA'
    elif m in ('\\xab', '\\xAB'): return u'\xAB'
    elif m in ('\\xac', '\\xAC'): return u'\xAC'
    elif m in ('\\xad', '\\xAD'): return u'\xAD'
    elif m in ('\\xae', '\\xAE'): return u'\xAE'
    elif m in ('\\xaf', '\\xAF'): return u'\xAF'
    elif m in ('\\xb0', '\\xB0'): return u'\xB0'
    elif m in ('\\xb1', '\\xB1'): return u'\xB1'
    elif m in ('\\xb2', '\\xB2'): return u'\xB2'
    elif m in ('\\xb3', '\\xB3'): return u'\xB3'
    elif m in ('\\xb4', '\\xB4'): return u'\xB4'
    elif m in ('\\xb5', '\\xB5'): return u'\xB5'
    elif m in ('\\xb6', '\\xB6'): return u'\xB6'
    elif m in ('\\xb7', '\\xB7'): return u'\xB7'
    elif m in ('\\xb8', '\\xB8'): return u'\xB8'
    elif m in ('\\xb9', '\\xB9'): return u'\xB9'
    elif m in ('\\xba', '\\xBA'): return u'\xBA'
    elif m in ('\\xbb', '\\xBB'): return u'\xBB'
    elif m in ('\\xbc', '\\xBC'): return u'\xBC'
    elif m in ('\\xbd', '\\xBD'): return u'\xBD'
    elif m in ('\\xbe', '\\xBE'): return u'\xBE'
    elif m in ('\\xbf', '\\xBF'): return u'\xBF'
    elif m in ('\\xc0', '\\xC0'): return u'\xC0'
    elif m in ('\\xc1', '\\xC1'): return u'\xC1'
    elif m in ('\\xc2', '\\xC2'): return u'\xC2'
    elif m in ('\\xc3', '\\xC3'): return u'\xC3'
    elif m in ('\\xc4', '\\xC4'): return u'\xC4'
    elif m in ('\\xc5', '\\xC5'): return u'\xC5'
    elif m in ('\\xc6', '\\xC6'): return u'\xC6'
    elif m in ('\\xc7', '\\xC7'): return u'\xC7'
    elif m in ('\\xc8', '\\xC8'): return u'\xC8'
    elif m in ('\\xc9', '\\xC9'): return u'\xC9'
    elif m in ('\\xca', '\\xCA'): return u'\xCA'
    elif m in ('\\xcb', '\\xCB'): return u'\xCB'
    elif m in ('\\xcc', '\\xCC'): return u'\xCC'
    elif m in ('\\xcd', '\\xCD'): return u'\xCD'
    elif m in ('\\xce', '\\xCE'): return u'\xCE'
    elif m in ('\\xcf', '\\xCF'): return u'\xCF'
    elif m in ('\\xd0', '\\xD0'): return u'\xD0'
    elif m in ('\\xd1', '\\xD1'): return u'\xD1'
    elif m in ('\\xd2', '\\xD2'): return u'\xD2'
    elif m in ('\\xd3', '\\xD3'): return u'\xD3'
    elif m in ('\\xd4', '\\xD4'): return u'\xD4'
    elif m in ('\\xd5', '\\xD5'): return u'\xD5'
    elif m in ('\\xd6', '\\xD6'): return u'\xD6'
    elif m in ('\\xd7', '\\xD7'): return u'\xD7'
    elif m in ('\\xd8', '\\xD8'): return u'\xD8'
    elif m in ('\\xd9', '\\xD9'): return u'\xD9'
    elif m in ('\\xda', '\\xDA'): return u'\xDA'
    elif m in ('\\xdb', '\\xDB'): return u'\xDB'
    elif m in ('\\xdc', '\\xDC'): return u'\xDC'
    elif m in ('\\xdd', '\\xDD'): return u'\xDD'
    elif m in ('\\xde', '\\xDE'): return u'\xDE'
    elif m in ('\\xdf', '\\xDF'): return u'\xDF'
    elif m in ('\\xe0', '\\xE0'): return u'\xE0'
    elif m in ('\\xe1', '\\xE1'): return u'\xE1'
    elif m in ('\\xe2', '\\xE2'): return u'\xE2'
    elif m in ('\\xe3', '\\xE3'): return u'\xE3'
    elif m in ('\\xe4', '\\xE4'): return u'\xE4'
    elif m in ('\\xe5', '\\xE5'): return u'\xE5'
    elif m in ('\\xe6', '\\xE6'): return u'\xE6'
    elif m in ('\\xe7', '\\xE7'): return u'\xE7'
    elif m in ('\\xe8', '\\xE8'): return u'\xE8'
    elif m in ('\\xe9', '\\xE9'): return u'\xE9'
    elif m in ('\\xea', '\\xEA'): return u'\xEA'
    elif m in ('\\xeb', '\\xEB'): return u'\xEB'
    elif m in ('\\xec', '\\xEC'): return u'\xEC'
    elif m in ('\\xed', '\\xED'): return u'\xED'
    elif m in ('\\xee', '\\xEE'): return u'\xEE'
    elif m in ('\\xef', '\\xEF'): return u'\xEF'
    elif m in ('\\xf0', '\\xF0'): return u'\xF0'
    elif m in ('\\xf1', '\\xF1'): return u'\xF1'
    elif m in ('\\xf2', '\\xF2'): return u'\xF2'
    elif m in ('\\xf3', '\\xF3'): return u'\xF3'
    elif m in ('\\xf4', '\\xF4'): return u'\xF4'
    elif m in ('\\xf5', '\\xF5'): return u'\xF5'
    elif m in ('\\xf6', '\\xF6'): return u'\xF6'
    elif m in ('\\xf7', '\\xF7'): return u'\xF7'
    elif m in ('\\xf8', '\\xF8'): return u'\xF8'
    elif m in ('\\xf9', '\\xF9'): return u'\xF9'
    elif m in ('\\xfa', '\\xFA'): return u'\xFA'
    elif m in ('\\xfb', '\\xFB'): return u'\xFB'
    elif m in ('\\xfc', '\\xFC'): return u'\xFC'
    elif m in ('\\xfd', '\\xFD'): return u'\xFD'
    elif m in ('\\xfe', '\\xFE'): return u'\xFE'
    elif m in ('\\xff', '\\xFF'): return u'\xFF'
    else: return m
