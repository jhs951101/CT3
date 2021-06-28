inch = float(input('inch 입력  :  '))
cm = inch * 2.54

number = '201401793'
name = 'JiHoon Shim'

print('학번  :  %20s' %number)
print('성명  :  %20s' %name)

print('='*30)
print(' '*5 + '%s inch' %'{:08.2f}'.format(inch))
print(' '*5 + '%s cm' %'{:08.2f}'.format(cm))
print('='*30)
