#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email:    hoojo_@126.com
# @github:   https://github.com/hooj0
# @create date: 2018-07-03
# @copyright by hoojo @2018
# @changelog YAML file convert JSON strings

#===============================================================================
# title: YAML file convert JSON strings
#===============================================================================
# use：PyYAML 3.12
#        pip install PyYAML
#-------------------------------------------------------------------------------
# description: 将YAML 转换成 Json 字符串对象
#-------------------------------------------------------------------------------

import os
import yaml
import json

#-------------------------------------------------------------------------------
# 将yaml文件转换Json输出
#-------------------------------------------------------------------------------
def convter(file):

    # 获取文件路径
    config_path = os.path.join(os.path.dirname(__file__), file)
    #print('convert yaml: %s' % config_path)
    
    # 加载文件
    with open(config_path, 'rb') as yaml_file:
        yaml_bytes = yaml_file.read()
    
    yaml_json = yaml.load(yaml_bytes)
    
    print('%s yaml convert json: %s' % (file, yaml_json))
    #print('---------------------------------------------------------------')
    # 排序并且缩进两个字符输出
    #print('%s convert formatter json: %s' % (file, json.dumps(yaml_json, sort_keys=True, indent=2))) 
    
    

def converter(file):
    
    # 获取文件路径
    config_path = os.path.join(os.path.dirname(__file__), file)
    
    with open(config_path, encoding=u'utf-8') as stream:
        yaml_data = yaml.safe_load(stream)
        
    # 排序并且缩进两个字符输出
    print('%s convert formatter json: %s' % (file, json.dumps(yaml_data, sort_keys=True, indent=2))) 


#-------------------------------------------------------------------------------
# yaml Object converter Json Array
#------------------------------------------------------------------------------- 
print("------------------------------yaml basic Type ==> Json Object------------------------------")   
convter('yaml/1_basic.yaml')

# output
#------------------------------------------------------------------------------- 
'''
yaml/1_basic.yaml convert formatter json: {
  "name": "jack",
  "sex": true,
  "age": 23,
  "class": "3 grade 1 class",
  "null_value": null,
  "scientific_notation": "1e+12",

  "another_key": "Another value goes here.",
  "however": "A string, enclosed in quotes.",

  "key with spaces": "value",
  "Keys can be quoted too.": "Useful if you want to put a ':' in your key.",
  
  "single quotes": "have 'one' escape pattern"
  "double quotes": "have many: \", \u0000, \t, \u263a, \r\n == \r\n, and more.",
  
  "literal_block": "This entire block of text will be the value of the 'literal_block' key,\nwith line breaks being preserved.\n\nThe literal continues until de-dented, and the leading indentation is\nstripped.\n\n    Any lines that are 'more-indented' keep the rest of their indentation -\n    these lines will be indented by 4 spaces.\n",
  "folded_style": "This entire block of text will be the value of 'folded_style', but this time, all newlines will be replaced with a single space.\nBlank lines, like above, are converted to a newline character.\n\n    'More-indented' lines keep their newlines, too -\n    this text will appear over two lines.        \n",
}
'''


#-------------------------------------------------------------------------------
# yaml Array converter Json Array
#------------------------------------------------------------------------------- 
print("------------------------------yaml Array ==> Json Array------------------------------")   
convter('yaml/2_array.yaml') 

# output
#------------------------------------------------------------------------------- 
'''
yaml/2_array.yaml convert formatter json: {
  "frameworks": [
    "spring",
    "struts",
    "mybatis"
  ],
  "languages": [
    "Ruby",
    "Perl",
    "Python"
  ],
  "websites": [
    "yaml.org",
    "ruby-lang.org",
    "python.org",
    "use.perl.org"
  ]
}
'''


#-------------------------------------------------------------------------------
# yaml Arrays converter Json Array
#------------------------------------------------------------------------------- 
print("------------------------------yaml Arrays ==> Json Array------------------------------")   
convter('yaml/2.1_arrays.yaml') 

# output
#------------------------------------------------------------------------------- 
'''
yaml/2.1_arrays.yaml convert formatter json: {
  "a_sequence": [
    "Item 1",
    "Item 2",
    0.5,
    "Item 4",
    {
      "another_key": "another_value",
      "key": "value"
    },
    {
      "another_key": "another_value",
      "key": "value"
    },
    [
      "This is a sequence",
      "inside another sequence"
    ],
    [
      [
        "Nested sequence indicators",
        "can be collapsed"
      ]
    ]
  ]
}
'''


#-------------------------------------------------------------------------------
# yaml Object converter Json Object
#------------------------------------------------------------------------------- 
print("------------------------------yaml Object ==> Json Object------------------------------")   
convter('yaml/3_object.yaml') 

# output
#------------------------------------------------------------------------------- 
'''
yaml/3_object.yaml convert formatter json: {
  "languages": {
    "Perl": "Ultra-simple language",
    "Python": "Best language",
    "Ruby": "The simplest language"
  },
  "websites": {
    "Java": {
      "desc": "Best language",
      "spring": "java framework"
    },
    "Perl": "use.perl.orgF",
    "Python": "python.org",
    "Ruby": "ruby-lang.org",
    "YAML": "yaml.org"
  }
}
'''


#-------------------------------------------------------------------------------
# yaml Object converter Json Object
#------------------------------------------------------------------------------- 
print("------------------------------yaml Object ==> Json Object------------------------------")   
converter('yaml/3.1_objects.yaml') 

# output
#-------------------------------------------------------------------------------
'''
yaml/3.1_objects.yaml convert formatter json: {
  "This is a key\nthat has multiple lines\n": "and this is its value",
  "and quotes are optional": {
    "key": [
      3,
      2,
      1,
      "takeoff"
    ]
  },
  "json_map": {
    "key": "value"
  },
  "json_seq": [
    3,
    2,
    1,
    "takeoff"
  ],
  "languages": {
    "Perl": "Ultra-simple language",
    "Ruby": "The simplest language"
  }
}
'''


#-------------------------------------------------------------------------------
# yaml anchor Object converter Json Object
#------------------------------------------------------------------------------- 
print("------------------------------yaml anchor Object ==> Json Object------------------------------")   
convter('yaml/4_anchor.yaml')  

# output
#-------------------------------------------------------------------------------
'''
yaml/4_anchor.yaml convert formatter json: {
  "anchored_content": "This string will appear as the value of two keys.",
  "other_anchor": "This string will appear as the value of two keys.",
  "bar": {
    "age": 20,
    "name": "Everyone has same name"
  },
  "base": {
    "name": "Everyone has same name"
  },
  "custom": {
    "age": 20,
    "name": "Everyone has same name",
    "foo-key": {
      "age": 10,
      "name": "Everyone has same name"
    },
    "names": [
      "This string will appear as the value of two keys.",
      "This string will appear as the value of two keys."
    ]
  },
  "foo": {
    "age": 10,
    "name": "Everyone has same name"
  }
}
'''


#-------------------------------------------------------------------------------
# yaml complex type converter Json Object
#------------------------------------------------------------------------------- 
print("------------------------------yaml complex type ==> Json Object------------------------------")   
convter('yaml/5_complex_type.yaml')  

# output
#-------------------------------------------------------------------------------
'''
yaml/5_complex_type.yaml yaml convert json: {
    'explicit_string': '0.5', 
    'python_complex_number': (1+2j), 
    (5, 7): 'Fifty Seven'
}
'''


#-------------------------------------------------------------------------------
# yaml complex type converter Json Object
#------------------------------------------------------------------------------- 
print("------------------------------yaml complex type ==> Json Object------------------------------")   
convter('yaml/6_extra_type.yaml')  

# output
#-------------------------------------------------------------------------------
'''
yaml/6_extra_type.yaml yaml convert json:
{
    'datetime': datetime.datetime(2001, 12, 15, 2, 59, 43, 100000),
    'datetime_with_spaces': datetime.datetime(2001, 12, 15, 2, 59, 43, 100000),
    'date': datetime.date(2002, 12, 14),
    'gif_file': b "GIF89a\x0c\x00\x0c\x00\x84\x00\x00\xff\xff\xf7\xf5\xf5\xee\xe9\xe9\xe5fff\x00\x00\x00\xe7\xe7\xe7^^^\xf3\xf3\xed\x8e\x8e\x8e\xe0\xe0\xe0\x9f\x9f\x9f\x93\x93\x93\xa7\xa7\xa7\x9e\x9e\x9eiiiccc\xa3\xa3\xa3\x84\x84\x84\xff\xfe\xf9\xff\xfe\xf9\xff\xfe\xf9\xff\xfe\xf9\xff\xfe\xf9\xff\xfe\xf9\xff\xfe\xf9\xff\xfe\xf9\xff\xfe\xf9\xff\xfe\xf9\xff\xfe\xf9\xff\xfe\xf9\xff\xfe\xf9\xff\xfe\xf9!\xfe\x0eMade with GIMP\x00,\x00\x00\x00\x00\x0c\x00\x0c\x00\x00\x05,  \x8e\x810\x9e\xe3@\x14\xe8i\x10\xc4\xd1\x8a\x08\x1c\xcf\x80M$z\xef\xff0\x85p\xb8\xb01f\r\x1b\xce\x01\xc3\x01\x1e\x10' \x82\n\x01\x00;",
    'set': {
        'item1': None,
        'item2': None,
        'item3': None
    },
    'or-set': {
        'item1': None,
        'item2': None,
        'item3': None
    },
    'set2': {
        'item1': None,
        'item2': None,
        'item3': None
    }
}
'''