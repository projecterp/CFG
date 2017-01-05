import os
import scandir
import time
import thread
import fileOpener as fo
import funcScanner
import blockScanner
import sample
folder_path=fo.open()

print(folder_path)

fileList=scandir.walk(folder_path)
count=0
file_list=[]
start=time.time()
data=[[],{},{},{}]
for root,dirs,files in fileList:
    for f in files:
        if ".c" in f[-2:]:
            fp=open(root+os.sep+f,"r")
            data[0].append(fp.name)
            print("*****scanning file:"+root+os.sep+f+"*****")
            data[1][fp.name]=funcScanner.scan(fp)
            data[2][fp.name]=funcScanner.func_call_list
            #t=thread.start_new_thread(funcScanner.scan,(fp,))
            fp.close()
            fp=open(root+os.sep+f,"r")
            data[3][fp.name]=blockScanner.scan(fp)
            fp.close()
            count+=1
            
end=time.time()
#print(data[3])
print("\n\nTime consumed= %f"%(end-start))
sample.main(data)

