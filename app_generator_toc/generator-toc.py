#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-08-26
# @copyright by hoojo @2018
# @changelog Generator Project makedown —— TOC 
import os


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
    
    
    # 保存文件
    def save(self):
    
        with open(self.__makedownFile, "w", encoding=u'utf-8') as file:  
            file.seek(0)
            file.truncate()   #清空文件
        
            file.writelines(self.__tableOfContents)
            file.close()
            
            
    #-------------------------------------------------------------------------------
    # generator makedown toc file
    #-------------------------------------------------------------------------------    
    def genMakedownTOC(self, suffix):
        self.scan(self.__rootDirectory, suffix)
        
        self.save()
    
    
    #-------------------------------------------------------------------------------
    # generator makedown readME file
    #-------------------------------------------------------------------------------    
    def genMakedownReadMe(self):
        pass
    
    
    
    def makeFolderChapter(self, path):
        path = path.replace(self.__rootDirectory, "").replace("\\", "/")
        
        return "+ [%s](%s)\n" % (path, "./" + path)
    
    def makeFileChapter(self, path, name):
        path = path.replace(self.__rootDirectory, "").replace("\\", "/")
        
        return "\t- [%s](%s)\n" % (name, "./" + path + "/" + name)
    
    
    def makeCommentChapter(self, path, name, line, comment):
        path = path.replace(self.__rootDirectory, "").replace("\\", "/")
        
        return "\t\t+ [%s#L%d](%s#L%d)\n" % (comment, line, "./" + path + "/" + name, line)
        
        
    def fetchContent(self, file):
        
        comments, lineNumber = {}, 0 
        with open(file, "r", encoding=u'utf-8') as file:  
            
            line = file.readline()
            lineNumber += 1
            
            while len(line) > 0: 
                if line.startswith("#") and not line.startswith("#-")  and not line.startswith("#=") and lineNumber >= 9:
                    
                    if lineNumber not in comments:
                        comments[lineNumber] = line.replace("#", "").replace("\n", "").strip()
                
                line = file.readline()
                lineNumber += 1    
                
        return comments        
        
    #-------------------------------------------------------------------------------
    # each target folder, add comment to python file
    #-------------------------------------------------------------------------------
    def scan(self, dir, suffix):
        
        for parent, dirs, files in os.walk(dir, topdown=False):
            
            if parent.find(".git") != -1:
                continue
            if parent.find(".settings") != -1:
                continue
            if parent.find("pycache") != -1:
                continue
            
            print('parent: %s' % parent)
            
            chapter = self.makeFolderChapter(parent)
            self.__tableOfContents.append(chapter)

            for name in files:
                file = os.path.join(parent, name)
                
                if file.endswith(suffix) == False:
                    continue
                
                print('files: %s' % name)
                
                chapter = self.makeFileChapter(parent, name)
                self.__tableOfContents.append(chapter)

                comments = self.fetchContent(file)
                for line, comment in comments.items():
                    content = self.makeCommentChapter(parent, name, line, comment)
                    print(content)
                    self.__tableOfContents.append(content)
                
    
    #-------------------------------------------------------------------------------
    # each target folder, add comment to python file
    #-------------------------------------------------------------------------------        
    def scanFile(self, dir, suffix):
        
        for root, dirs, files in os.walk(dir, topdown=False):
            
            for name in files:
                file = os.path.join(root, name)
                
                if file.endswith(suffix) == False:
                    continue
                if file.find(".git") != -1:
                    continue
                
                print('files: %s' % file)
                
                self.__tableOfContents.append(file + "\n")
                
    
    def scanFolder(self, dirs):
        
        for name in dirs:
            folder = os.path.join(root, name)
            
            if folder.find(".git") != -1:
                continue
            if folder.find(".settings") != -1:
                continue
            
            print('dirs: %s' % folder)
            #self.scanFile(folder, suffix)
    
util = GeneratorTOCUtils("F:\\Example Exercise\\Python\\", "F:\\Example Exercise\\Python\\toc.md")    
util.genMakedownTOC(".py") 
