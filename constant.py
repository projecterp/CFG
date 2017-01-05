macro=r'#define|#include|#undef|#ifdef|#ifndef|#if|#else|#elif|#endif|#error|#pragma'
keyword=r'auto|double|int|struct|break|else|else if|long|switch|case|enum|register|typedef|char|extern|return|union|const|float|short|unsigned|continue|for|signed|void|default|goto|sizeof|volatile|do|if|static|while'
id=r'[A-Za-z][\w]*'
func_def=r'[A-Za-z]{1,}[\s]+[A-Za-z][\w]*[\s]*\(.*\)'
func_call=id+r'[\s]*\(.*\)'
skip_call=r'^(\s|\()*('+keyword+r')[\s]*\(.*\)'
macro_func=r'^[\s]*('+macro+r')[\s]+'+func_call

"""
p=re.search(func_call,"funifz()")
if p is not None:
    q=re.search(skip_call,p.group())
    if q is None:
       print("yo:"+p.group())
    else:
       print("no:"+q.group())   
        
"""
