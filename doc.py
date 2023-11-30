s=input()
if s.endswith('.jpeg'):
    print('Photo Document')
elif s.endswith('.doc'):
    print('Word Document')
elif s.endswith('xls'):
    print('Excel Document')
elif s.endswith('ppt'):
    print('Powerpoint Document')
else:
    print('Invalid Document')
