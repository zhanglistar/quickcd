import os
import sys
import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:8000')
# Print list of available methods
#print s.system.listMethods()

result = s.get(sys.argv[1])
if len(result) == 0:
    print ""
print ' '.join([item + '/' + sys.argv[1] for item in result])

'''
if len(result) == 1:
    print result[0]
index = 0
for item in result:
    print "%d: %s" % (index, item)
    index = index + 1
select = raw_input("Input number: ")
if int(select) >= 0 and int(select) < len(result):
    #print result[int(select)] + '/' + input_str
    print "change to directory:%s" % result[int(select)] + '/' + input_str
    os.chdir(result[int(select)] + '/' + input_str)

'''
