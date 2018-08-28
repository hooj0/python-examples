#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-08-26
# @copyright by hoojo @2018
# @changelog Generator Project makedown —— TOC 
import os
import re


#===============================================================================
#     Generator Project makedown —— TOC  table of Contents
#===============================================================================
# 描述：生成项目工程的 makedown 格式的 目录索引 TOC 的文档
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
# 生成 目录索引 TOC 的文档 工具类
#-------------------------------------------------------------------------------
class GeneratorTOCUtils:
    
    __rootDirectory = ".";
    __makedownFile = ""
    
    __tableOfContents = []
    
    def __init__(self, rootDirectory, makedownFile):
        self.__rootDirectory = rootDirectory
        self.__makedownFile = makedownFile
        
        print("目标工程位置：%s，生成文件保存位置：%s" % (rootDirectory, makedownFile))
    
    #-------------------------------------------------------------------------------
    # generator makedown toc file
    #-------------------------------------------------------------------------------    
    def genMakedownTOC(self, suffix):
        self.__scan(self.__rootDirectory, suffix)
        self.__save()
    
    
    #-------------------------------------------------------------------------------
    # generator makedown readME file
    #-------------------------------------------------------------------------------    
    def genMakedownReadMe(self, suffix):
        self.__scan(self.__rootDirectory, suffix, isReadMe=True)
        self.__save()
    
    # 保存文件
    def __save(self):
        with open(self.__makedownFile, "w", encoding=u'utf-8') as file:  
            file.seek(0)
            file.truncate()   #清空文件
        
            file.writelines(self.__tableOfContents)
            file.close()
            
    def is_chinese(self, uchar):
        #zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')
        #global zh_pattern
        return re.compile(u'[\u4e00-\u9fa5]+').search(uchar)
    
        """判断一个unicode是否是汉字
        if uchar >= u'/u4e00' and uchar <= u'/u9fa5':
            return True
        else:
            return False
        """    
                    
    def __makeFolderChapter(self, path, isReadMe=False):
        
        path = path.replace(self.__rootDirectory, "").replace("\\", "/")

        if isReadMe:
            return "# %s \n[**%s**](%s)\n" % (path, path, "./" + path)
        else:
            return "+ [**%s**](%s)\n" % (path, "./" + path)
    
    
    def __makeFileChapter(self, path, name, isReadMe=False):
        path = path.replace(self.__rootDirectory, "").replace("\\", "/")
        
        if isReadMe:
            return "## %s \n[`%s`](%s)\n" % (name, name, "./" + path + "/" + name)
        else:
            return "\t- [`%s`](%s)\n" % (name, "./" + path + "/" + name)
    
    
    def __makeCommentChapter(self, path, name, line, comment):
        path = path.replace(self.__rootDirectory, "").replace("\\", "/")
        
        return "\t\t+ [%s#L%d](%s#L%d)\n" % (comment, line, "./" + path + "/" + name, line)

    def __makeContentChapter(self, contents):
        
        data = ""
        for content in contents:
            data += content
            
        return "\n\r```python \n\r%s \r\n```\n\r" % data
        
        
    def __fetchContent(self, file):
        contents, lineNumber = [], 0
        
        with open(file, "r", encoding=u'utf-8') as file:  
            
            line = file.readline()
            lineNumber += 1
            while len(line) > 0:
                
                if lineNumber >= 10: 
                    contents.append(line)
                if lineNumber >= 50:
                    break
                    
                line = file.readline()
                lineNumber += 1
                
        return contents
    
    
    def __fetchComments(self, file):
        
        comments, lineNumber = {}, 0 
        with open(file, "r", encoding=u'utf-8') as file:  
            
            line = file.readline()
            lineNumber += 1
            
            while len(line) > 0: 
                if line.startswith("#") and not line.startswith("#-") and not line.startswith("# -") and not line.startswith("#=") and not line.startswith("# =") and lineNumber >= 9:
                    
                    if lineNumber not in comments and (lineNumber - 1) not in comments:
                        line = line.replace("#", "").replace("\n", "").strip()
                        
                        first, last = line[0:1], line[len(line) - 1:]
                        if self.is_chinese(first) or self.is_chinese(last):
                            comments[lineNumber] = line
                
                line = file.readline()
                lineNumber += 1    
                
        return comments      
        
    #-------------------------------------------------------------------------------
    # each target folder, add comment to python file
    #-------------------------------------------------------------------------------
    def __scan(self, dir, suffix, isReadMe=False):
        
        for parent, dirs, files in os.walk(dir, topdown=False):
            
            if parent.find(".git") != -1:
                continue
            if parent.find(".settings") != -1:
                continue
            if parent.find("pycache") != -1:
                continue
            
            print('parent: %s' % parent)
            
            chapter = self.__makeFolderChapter(parent, isReadMe)
            self.__tableOfContents.append(chapter)

            for name in files:
                file = os.path.join(parent, name)
                
                if file.endswith(suffix) == False:
                    continue
                
                print('files: %s' % name)
                
                chapter = self.__makeFileChapter(parent, name.replace(suffix, ""), isReadMe)
                self.__tableOfContents.append(chapter)

                if isReadMe:
                    contents = self.__fetchContent(file)
                    content = self.__makeContentChapter(contents)
                    self.__tableOfContents.append(content)

                else:
                    comments = self.__fetchComments(file)
                    for line, comment in comments.items():
                        content = self.__makeCommentChapter(parent, name, line, comment)
                        print(content)
                        self.__tableOfContents.append(content)
                
    
    #-------------------------------------------------------------------------------
    # each target folder, add comment to python file
    #-------------------------------------------------------------------------------        
    def __scanFile(self, dir, suffix):
        
        for root, dirs, files in os.walk(dir, topdown=False):
            
            for name in files:
                file = os.path.join(root, name)
                
                if file.endswith(suffix) == False:
                    continue
                if file.find(".git") != -1:
                    continue
                
                print('files: %s' % file)
                
                self.__tableOfContents.append(file + "\n")
                
    
    def __scanFolder(self, dirs):
        
        for name in dirs:
            folder = os.path.join(root, name)
            
            if folder.find(".git") != -1:
                continue
            if folder.find(".settings") != -1:
                continue
            
            print('dirs: %s' % folder)
            #self.scanFile(folder, suffix)
    
util = GeneratorTOCUtils("F:\\Example Exercise\\Python\\", "F:\\Example Exercise\\Python\\tutorial.md")    
#util.genMakedownTOC(".py") 
util.genMakedownReadMe(".py")

#util = GeneratorTOCUtils("F:\\Example Exercise\\Bash", "F:\\Example Exercise\\Bash\\readme.md")    
#util.genMakedownTOC(".sh") 
