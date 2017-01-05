__author__='Pranav'

import re
from constant import *

lines=[]

def findBlocks(fp,lines,i):
    #global block_list,sub_block_list
    block_list=[]
    sub_block_list=[]
    stack=[]
    #lines=lines[i-1:]
    k=i-1
    for i in range(k,len(lines)): 
        #print(lines[i]) 
        if "//" in lines[i]:
           lines[i]=lines[i][:lines[i].index("//")]
        if "/*" in lines[i]:
            if "*/" in lines[i]:
                lines[i]=lines[i][:lines[i].index("/*")]+lines[i][lines[i].index("*/")+2:]
            else:
                lines[i]=lines[i][:lines[i].index("/*")]
                j=i+1
                flag=0
                while j < len(lines) and "*/" not in lines[j]:
                    lines[j]=""
                    j=j+1
                    flag=1
                if j<len(lines) and "*/" in lines[j]:
                   lines[j]=lines[j][lines[j].index("*/")+2:]
        line=lines[i]
        #print(line)
        t=""
        if line.strip()!="\n":
         #print("line no:"+str(i))
          for c in line:
            t+=c
            if c=='{':
              #print(stack)
              stack.append(t[::-1])
              #stack.append(c)
              t=""
            if c=='}':  
              stack.append(t[::-1])
              #stack.append(c)
              t=""
              temp=c
              z=stack.pop()
              while 1:
               #print(stack)
               while stack[-1].strip()=="":
                   stack.pop()
               s=stack[-1]
               s=s[0]
               if s=='{':
                  s=stack.pop()
                  temp+=s+stack.pop()
                  #print("yup:"+temp[::-1])
                  sub_block_list.append((temp[::-1],"%d"%(i),"-1"))
                  if stack==[] and sub_block_list!=[]:
                     #print("yo:")
                     block_list.append(sub_block_list.pop())
                     break
                  elif stack==[]:
                     #print("yppp:")
                     break
                  stack.append(temp)
                  break
               else:
                  temp+=stack.pop()
        stack.append(t[::-1])
        i+=1
    return sub_block_list+block_list    

def scan(fp):
    #global block_list,sub_block_list
    global lines 
    sub_block_list=[]
    lines=[]
    i=0
    for line in fp:
        lines.append(line)
    for line in lines:
        p=re.search(func_def,line)
        if p is not None:
           sub_block_list+=findBlocks(fp,lines,i+1)
           break
        else:
           p=re.search("main[\s]*\(.*\)",line)
           if p is not None:
              sub_block_list+=findBlocks(fp,lines,i+1)
              break 
           else:
              i+=1
    print("file = "+fp.name)
    #print(sub_block_list)
    print("****************************************************************")
    return sub_block_list

#fp=open("MAX_FLOW\\FF.c","r")
#print(scan(fp))



