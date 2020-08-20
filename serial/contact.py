import re
import phonenumbers as ph
# print('(%s) %s-%s' % tuple(re.findall(r'\d{4}$|\d{3}', '0123456789')))
#
# print(re.findall(r'\d{4}$|\d{4}|\d{1}', '15104494723'))

# print('+ %s (%s) %s-%s' % list(re.findall(r'\d{0}|\d{4}$|\d{3}', '15104494723')))

def phoneFormat(string):
    newString = "".join(x for x in string if x in '0123456789')
    # if newString.len() >= 11:

    return newString

# print(phoneFormat('+44 7911 123456'))
phone = "+15104494723"
phone2 = "+6433456789"
x = ph.parse(phone2, None)
y = ph.format_number(x, ph.PhoneNumberFormat.NATIONAL)
print(y)
