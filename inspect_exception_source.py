source = open('src/exception.py').read()
print('source:\n', source)
code = compile(source, 'src/exception.py', 'exec')
ns = {}
exec(code, ns)
print('\nnamespace keys:', sorted(k for k in ns.keys() if not k.startswith('__')))
