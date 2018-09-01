#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-08-26
# @copyright by hoojo@2018
# @changelog Added Generator Copyright Information to file python


#===============================================================================
# Generator Copyright Information
#===============================================================================
# 描述：生成 copyright 信息，插入到文件中
#-------------------------------------------------------------------------------

import time
import os

#-------------------------------------------------------------------------------
# global env
#-------------------------------------------------------------------------------
'''
targetFolder="F:\\Example Exercise\\Python"
fiilter="py"

COPYRIGHT_INFORMATION = ''#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
%s
# @copyright by hoojo@2018
# @changelog %s
'''

targetFolder="F:\\Example Exercise\\Bash"
fiilter="sh"

COPYRIGHT_INFORMATION = '''#!/bin/bash
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: %s
# @copyright by hoojo@2018
# @changelog %s
'''


#-------------------------------------------------------------------------------
# fetch comment keyword
#-------------------------------------------------------------------------------
SKIP_PREFIXS = [ "#!/usr", "# -*-", "#-*-", "# encoding", "# @author", "#!/bin/" ]
def fetchCommentKeyword():
    
    for comment in COPYRIGHT_INFORMATION.splitlines():
        keywords = comment.split(" ")
        if len(keywords) >= 2:
            SKIP_PREFIXS.append(keywords[1])


#-------------------------------------------------------------------------------
# fetch file latest update date
#-------------------------------------------------------------------------------
def fetchUpdatedDate(file):
    st = os.stat(file)
    #print('st_ctime: ', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(st.st_ctime)))
    #print('st_mtime: ', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(st.st_mtime)))
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(st.st_ctime))
    
    
#-------------------------------------------------------------------------------
# skip comment line content
#-------------------------------------------------------------------------------
def skipLine(line):
    
    for item in SKIP_PREFIXS: 
        if line.find(item) != -1:
            return True
            
    return False
    
    
#-------------------------------------------------------------------------------
# Read a file content, filter comment
#-------------------------------------------------------------------------------
def read(targetFile):
    
    contentLines = []
    with open(targetFile, "r", encoding=u'utf-8') as file:
        text = file.readline()
        
        while text != "":
            if text.startswith("#"):
                if skipLine(text):
                    #print("remove text: %s" % text)
                    pass
                else:
                    contentLines.append(text)
                    
            else:
                contentLines.append(text)
        
            text = file.readline()   
        
        file.close()     

    return contentLines    


#-------------------------------------------------------------------------------
# Write transform content to file    
#-------------------------------------------------------------------------------
def write(targetFile, contentLines):
    
    with open(targetFile, "w", encoding=u'utf-8') as file:  
        file.writelines(contentLines)
        file.close()


#-------------------------------------------------------------------------------
# clean comment after empty line
#-----------------------------------------------------------------------------
def cleanEmptyLine(contentLines):
    emptyLine, skip = 0, False
    
    for line in contentLines:
        if (line == "\n" or line == "\r" or line == "\r\n") and skip == False:
            emptyLine = emptyLine + 1
        else:
            skip = True

    if emptyLine >= 3:     
        return contentLines[emptyLine - 3:]
    return contentLines

            
#-------------------------------------------------------------------------------
# insert comment to read file line arrays
#-------------------------------------------------------------------------------
def insertComment(targetFile, contentLines):
    
    updateDate = fetchUpdatedDate(targetFile)
    changelog = generatorChangelog(targetFile)
    
    copyright = COPYRIGHT_INFORMATION % (updateDate, changelog)
    contentLines.insert(0, copyright)
    
    return contentLines


#-------------------------------------------------------------------------------
# generator changelog to read file line arrays
#-------------------------------------------------------------------------------
def generatorChangelog(targetFile):
    changelog = "Added python3 `%s` example"
    
    latestName = "learn"
    if targetFile.find("examples_") != -1:
        latestName = targetFile.split("examples_")[1]
    elif targetFile.find("samples_") != -1:    
        latestName = targetFile.split("samples_")[1]
    else:
        latestName = targetFile
        
    latestName = latestName.replace("_", " ").replace("\/", "->").replace("\\", "->").replace(".py", "").replace(".sh", "")
    
    changelog = changelog % latestName
    return changelog      


#-------------------------------------------------------------------------------
# each target folder, add comment to python file
#-------------------------------------------------------------------------------
def eachFolder(targetFolder):
    
    for root, dirs, files in os.walk(targetFolder, topdown=False):
        print(root)
        
        for name in files:
            targetFile = os.path.join(root, name)
            
            if targetFile.find("samples_") == -1 and targetFile.find("example") == -1:
                continue
            
            if targetFile.find("pycache") != -1:
                continue
            
            if targetFile.endswith(fiilter) == False:
                continue
            
            print('files: %s' % targetFile)
            
            contentLines = read(targetFile)
            
            contentLines = cleanEmptyLine(contentLines)
            
            contentLines = insertComment(targetFile, contentLines)
            
            write(targetFile, contentLines)
            print("----------------------------------------------")       
            
        for name in dirs:
            folder = os.path.join(root, name)
            print('dirs: %s' % folder)
            
            eachFolder(folder) 
        


#-------------------------------------------------------------------------------
# run application
#-------------------------------------------------------------------------------
fetchCommentKeyword()
eachFolder(targetFolder)


