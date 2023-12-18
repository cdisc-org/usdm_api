from model.syntax_template import SyntaxTemplate
from model.condition import Condition

a = SyntaxTemplate(id='1', name='1', text='text1')
b = Condition(id='2', name='2', text='text2')

print(f"A: {a.instanceType}")
print(f"B: {b.instanceType}")
