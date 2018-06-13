#!/usr/bin/env python
# encoding: utf-8
# @author: hoojo

class Person:
    ''' 定义基本属性 '''
    name = 'lucy'
    age = 22
    
    ''' 定义私有属性，外部无法访问 '''
    __height = 166
    
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.__height = height
        
    ''' 定义方法，访问私有属性和基本属性 '''    
    def info(self):
        print('I am name is %s, age %s , height %s' % (self.name, self.age, self.__height)) 
        

# 继承Person 对象
class Student(Person):
    # 新的属性
    grade = ''     
    
    def __init__(self, name, age, height, grade):
        # 为父类属性赋值   
        Person.__init__(self, name, age, height)
        
        # 为当前类属性赋值
        self.grade = grade
        
    # 覆盖父类方法
    def info(self):
        # 子类无法访问父类私有方法
        # print('I am name is %s, age %s , height %s, grade: %s' % (self.name, self.age, self.__height, self.grade))    
        print('I am name is %s, age %s, grade: %s' % (self.name, self.age, self.grade))    
        
    # 自定义的其他方法        
    def getMyGrade(self):
        print('my grade: %s' % self.grade)    
        
        
#######################################################        
stu = Student('jackson', 21, 178, '3年级')

stu.info()
stu.getMyGrade()
        
#######################################################        
        

class Classes:
    
    className = ''
    classNo = ''
    
    def __init__(self, name, no):        
        self.className = name
        self.classNo = no
        
    def info(self):
        print('I am is %s class, class No %s' % (self.className, self.classNo))    
        
    def getClass(self):
        print('your class %s' % self.className)   
        
    
# 继承多个类        
class ClassStudent(Classes, Student):
    
    classStudentNo = ''
    
    def __init__(self, name, age, height, grade, className, no, classStudentNo):
        # 调用父类构造函数
        Classes.__init__(self, className, no)
        # 调用父类构造
        Student.__init__(self, name, age, height, grade)
        
        # 为当前类属性赋值
        self.classStudentNo = classStudentNo
       
    # 覆盖父类方法    
    def info(self):
        Classes.info(self)
        Student.info(self)
    
    # 其他方法    
    def other(self):
        Classes.getClass(self)
        Student.getMyGrade(self)    
        
        
##################################################################
cs = ClassStudent('jack', 25, 199, '3班', 'C301', '三年级', 'C301030303')        

cs.info()         

cs.other()

# 访问 父类属性
print(cs.className)
print(cs.name)
# 私有属性无法方法
#print(cs.__height)
##################################################################
             