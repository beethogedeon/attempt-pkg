from __future__ import annotations

from {{cookiecutter.pkg_name}}.hello_world import hello_world

def hello_test():
    hello_world()
    

def test_hello(unit_tests_mocks: None):
    hello_test()
 
    
def test_init_hello():
    hello_test()
    
