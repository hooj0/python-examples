import keyword

module_name = 'module_center'

print('module name：', __name__)

def say(content):
    print('you say:', content)
    
def kw():
    print('key word:', keyword.kwlist)   
    
def min_value(*args):
    print('min:', min(args))    