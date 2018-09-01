#!/usr/bin/env python3
# encoding: utf-8
# @author:   hoojo
# @email:    hoojo_@126.com
# @github:   https://github.com/hooj0
# @create date: 2018-09-01
# @copyright by hoojo @2018
# @changelog YAML file convert JSON strings

#===============================================================================
# title: YAML file convert JSON strings
#===============================================================================
# use：ruamel.yaml 0.15.64
#        pip install ruamel.yaml
# https://yaml.readthedocs.io/en/latest/example.html
#-------------------------------------------------------------------------------
# description: ruamel.yaml是一个YAML解析器/转换器，支持往返保留注释，seq / map flow style,和映射键顺序
#-------------------------------------------------------------------------------
import sys
from ruamel.yaml import YAML
import os
import json
from ruamel.yaml.compat import ordereddict

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
    
    yaml = YAML()
    yaml_json = yaml.load(yaml_bytes)
    print(yaml_json)
    
    #yaml.dump(yaml_json, sys.stdout)
    
    # 排序并且缩进两个字符输出
    #print('%s convert formatter json: %s' % (file, json.dumps(dict(yaml_json), sort_keys=True, indent=2))) 

#-------------------------------------------------------------------------------
# yaml Object converter Json Object
#------------------------------------------------------------------------------- 
print("------------------------------yaml Object ==> Json Object------------------------------")   
convter('yaml/3.1_objects.yaml') 

# output
#-------------------------------------------------------------------------------
# ordereddict([('languages', ordereddict([('Ruby', 'The simplest language'), ('Perl', 'Ultra-simple language')])), ('This is a key\nthat has multiple lines\n', 'and this is its value'), ('json_map', ordereddict([('key', 'value')])), ('json_seq', [3, 2, 1, 'takeoff']), ('and quotes are optional', ordereddict([('key', [3, 2, 1, 'takeoff'])]))])

#-------------------------------------------------------------------------------
# yaml complex type converter Json Object
#------------------------------------------------------------------------------- 
print("------------------------------yaml complex type ==> Json Object------------------------------")   
convter('yaml/5_complex_type.yaml')  

# output
#-------------------------------------------------------------------------------
# ordereddict([('explicit_string', '0.5'), ('python_complex_number', <ruamel.yaml.comments.TaggedScalar object at 0x0000000002AF1908>), ((5, 7), 'Fifty Seven')])