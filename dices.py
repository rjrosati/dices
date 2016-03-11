import itertools
import sys
import re
import matplotlib.pyplot as plt
import numpy as np

EXCLUDE_POWERS_OF_1 = False 
INCLUDE_LOGS = False 


q = float(sys.argv[1])
r = float(sys.argv[2])
s = float(sys.argv[3])
t = float(sys.argv[4])
u = float(sys.argv[5])



operations = ['+','-','*','/','**']
if INCLUDE_LOGS:
    operations.append('|')
    log_replace = re.compile(r"(\d\.\d?)\|(\d\.\d?)")

max_z = 300
counts = np.zeros((max_z))
for z in range(0,max_z):
    for a in operations:
        for b in operations:
            for c in operations:
                for d in operations:
                    for e in itertools.permutations([q,r,s,t,u]):
                        test_str1 = "({4}{0}{5}){1}{6}{2}{7}{3}{8}".format(a,b,c,d,e[0],e[1],e[2],e[3],e[4])
                        test_str2 = "({4}{0}{5}{1}{6}){2}{7}{3}{8}".format(a,b,c,d,e[0],e[1],e[2],e[3],e[4])
                        test_str3 = "({4}{0}{5}{1}{6}{2}{7}){3}{8}".format(a,b,c,d,e[0],e[1],e[2],e[3],e[4])
                        for test_str in (test_str1,test_str2,test_str3):
                            if INCLUDE_LOGS and '|' in test_str:
                                test_str = log_replace.sub(r"(np.log(\1)/np.log(\2))",test_str)
                            if EXCLUDE_POWERS_OF_1 and '1.0**' in test_str:
                                continue
                            try:
                                if eval(test_str) == z:
                                    #print(test_str)
                                    counts[z] += 1
                            except OverflowError:
                                pass
                            except MemoryError:
                                pass
plt.plot(counts)
plt.show()
