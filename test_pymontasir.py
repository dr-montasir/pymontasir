from pymontasir import say_hello

def test_helloworld_no_params(name=None):
	assert say_hello() == "Hello, World!"

def test_helloworld_with_params(name=None):
	assert say_hello("Everyone") == "Hello, Everyone!"