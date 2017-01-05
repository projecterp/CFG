__author__ = 'Pranav'

import re;
from constant import *
func_def_list=[]
func_call_list=[]


def findCalls(fp,line,i):
    global func_def_list,func_call_list
    p=re.search("\(.*\)",line)
    line=p.group()[1:-1]
    stack=[]
    for c in line:
        stack.append(c)
        if c==')':
           flag=0
           temp=""
           while 1:
             #print(stack)
             if stack==[]:
                #print("yo:"+temp[::-1])
                func_call_list.append((temp[::-1],"%d"%(i+1),"%d"%i))
                stack.append(temp)
                break
             s=stack[-1]
             if flag==1 and (s==',' or s=='?' or s==':' or s=='['or s=='+' or s=='-' or s=='*' or s=='/' or s=='%' or s=='^' or s=='&' or s=='=' or s=='>' or s=='<' or s=='~' or s=='|' or s=='('):
                #print("yo:"+temp[::-1])
                func_call_list.append((temp[::-1],"%d"%(i+1),"%d"%i))
                stack.append(temp)
                break
             elif s=='(' and flag==0:
                temp+=stack.pop()
                flag=1
             else:
                temp+=stack.pop()
               
def scan(fp):
    #wr=open("count"+str(i)+".txt","w")
    global func_def_list,func_call_list
    func_def_list=[]
    func_call_list=[]
    count=0
    lines=fp.readlines()
    for i in range(len(lines)):
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
        #print(lines[i])            
        p=re.search(func_def,lines[i])
        if p is not None:
              #print("line :%d"%(i+1))
              #print(p.group())
                 q=re.search(skip_call,p.group())
                 r=re.search(macro_func,p.group())
                 if q is None and r is None:
                       if func_def_list!=[]:
                           temp=func_def_list[-1]
                           x=temp[0]
                           y=temp[1]
                           func_def_list[-1]=(x,y,"%d"%i)
                       func_def_list.append((p.group(),"%d"%(i+1),"-1"))
                 elif q is not None:
                       findCalls(fp,q.group(),i)
                 else:
                       findCalls(fp,r.group(),i)
              #wr.write(p.group()+"\tline no. %d \n"%(i+1))  
        else:
              p=re.search("main[\s]*\(.*\)",lines[i])
              if p is not None:
                 #print("line :%d"%(i+1))
                 #print(p.group())
                 if func_def_list!=[]:
                           temp=func_def_list[-1]
                           x=temp[0]
                           y=temp[1]
                           func_def_list[-1]=(x,y,i)                  
                 func_def_list.append((p.group(),"%d"%(i+1),"-1"))
                 
                #wr.write(p.group()+"\tline no. %d\n"%(i+1))
                    
              #Determining Function Calls
              else:
                 p=re.search(func_call,lines[i])
                 if p is not None:
                    q=re.search(skip_call,p.group())
                    r=re.search(macro_func,p.group())
                    if q is None and r is None:
                       #print("call:"+p.group())
                       findCalls(fp,p.group(),i)
                       func_call_list.append((p.group(),"%d"%(i+1),"%d"%i))     
                    elif q is not None:
                       #print("keyword:"+q.group())
                       findCalls(fp,q.group(),i)
                    else:
                       #print("macro:"+r.group())
                       findCalls(fp,r.group(),i)
    #   wr.close()
    #fp.close()
    print(func_def_list)
    return func_def_list

