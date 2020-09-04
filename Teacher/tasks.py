from __future__ import absolute_import

from celery import shared_task

from django.conf import settings



import subprocess
import os
from .models import *
import tempfile
import psutil
from Moderator.models import *
from Student.models import *
import filecmp 
import difflib


"""
def compile(id):
    os.chdir("D:\Developer\Practise Project\one\judge")
    if id == 6:
        cmd = "gcc ashik.c -o ashik.exe && ashik.exe"
    elif id == 7:
        cmd = "python ashik.py "
    elif id == 9:
        cmd = "g++ ashikcpul.cpp -o ashikcpul.exe && ashikcpul.exe"
    elif id == 8:
        cmd = "javac Ashik.java && java Ashik"
    elif id == 10:
        cmd = "gcc ashik1.c -o ashik1.exe && ashik1.exe"
    elif id == 11:
        cmd = "gcc ashik2.c -o ashik2.exe && ashik2.exe"
    elif id == 12:
        cmd = "python Simple.py"
    if id<=6 and id>=11:
        out = subprocess.Popen(cmd,shell=True,stdin = subprocess.PIPE,\
                    stdout=subprocess.PIPE,stderr=subprocess.PIPE,\
                        errors='st')
        output,error=out.communicate()
    
    with open("test_case.txt","r") as f:
        st = ""
        for _ in range(2):
            for _ in range(4):
                st += f.readline()
            #print(st)

        f.readline()
         
        proc = subprocess.Popen(cmd,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True,\
                 universal_newlines = True)
        output,error=proc.communicate(input=st)
        st = ""
    
    r = Result()
    r.id = id
    if error:
        r.result = "wrong"
        r.save()
        return error
    else:
        with open("produce_ouput.txt","w") as f:
            f.write(output)
        r.result = "Right"
        r.save()
"""
@shared_task
def compile(user_id,id):
    problem = Input.objects.get(id = id)

    time = problem.problem.Time_Limit

    testcase_range = problem.problem.Testcase_Number

    testcase_line = problem.problem.Testcase_Linenumber

    output = ""
    
    file_path = settings.MEDIA_ROOT+"\\"+"code_file"+"\\"+problem.title+"_"+str(problem.id)
     
    input_file_path = settings.MEDIA_ROOT+"\\"+"input"+"\\"+problem.title+".txt"
    
    if os.path.exists(input_file_path):
        in_f = open(input_file_path,"r")


    if problem.language_choices == 'C':
        
        codefile_path = file_path+".c"
        code_f = open(codefile_path,'w')
        code_f.write(problem.source_code)
        code_f.close()
    
        
        #filename = problem.title+"_"+str(problem.id)+".c"
        executable = settings.MEDIA_ROOT+"\\"+"output"+"\\"+problem.title+"_"+str(problem.id)+".exe"
        cmd = "gcc "+codefile_path+" -o "+executable+" && "+executable


        for _ in range(testcase_range):
            
            st = ""
            for _ in range(testcase_line):
                st += in_f.readline()
            out = subprocess.Popen(cmd,shell=True,stdin = subprocess.PIPE,\
                 stdout=subprocess.PIPE,stderr=subprocess.PIPE,\
                       errors='st')
            try:
                outcome,error=out.communicate(input=st,timeout=time)
            
            except subprocess.TimeoutExpired as e:
                process = psutil.Process(out.pid).children(recursive=True)
                for proc in process:
                    proc.kill()
                gone, alive = psutil.wait_procs(process,timeout=2)

            output = output + str(outcome)
        
         
    elif problem.language_choices =='C++':
        
        codefile_path = file_path+".cpp"
        code_f = open(codefile_path,'w')
        code_f.write(problem.source_code)
        code_f.close()
        
        #filename = problem.title+"_"+str(problem.id)+".c"
        executable = settings.MEDIA_ROOT+"\\"+"output"+"\\"+problem.title+"_"+str(problem.id)+".exe"
        cmd = "g++ "+codefile_path+" -o "+executable+" && "+executable

        
        for _ in range(testcase_range):
            
            st = ""
            for _ in range(testcase_line):
                st += in_f.readline()
            out = subprocess.Popen(cmd,shell=True,stdin = subprocess.PIPE,\
                 stdout=subprocess.PIPE,stderr=subprocess.PIPE,\
                       errors='st')
            try:
                outcome,error=out.communicate(input=st,timeout=time)
            
            except subprocess.TimeoutExpired as e:
                process = psutil.Process(out.pid).children(recursive=True)
                for proc in process:
                    proc.kill()
                gone, alive = psutil.wait_procs(process,timeout=2)

            output = output + str(outcome)

    
    
    elif problem.language_choices =='Java':

        codefile_path = file_path+".java"
        code_f = open(codefile_path,'w')
        code_f.write(problem.source_code)
        code_f.close()
        
        #filename = problem.title+"_"+str(problem.id)+".c"
        executable = settings.MEDIA_ROOT+"\\"+"output"+"\\"+problem.title+"_"+str(problem.id)
        directory = settings.MEDIA_ROOT+"\\"+"output"

        for _ in range(testcase_range):
            
            st = ""
            for _ in range(testcase_line):
                st += in_f.readline()
            cmd = "javac -d "+directory+" "+codefile_path+" && java "+executable

            out = subprocess.Popen(cmd,shell=True,stdin = subprocess.PIPE,\
                 stdout=subprocess.PIPE,stderr=subprocess.PIPE,\
                       errors='st')
            try:
                outcome,error=out.communicate(input= st,timeout=time)
            
            except subprocess.TimeoutExpired as e:
                process = psutil.Process(out.pid).children(recursive=True)
                for proc in process:
                    proc.kill()
                gone, alive = psutil.wait_procs(process,timeout=2)

            output = output + str(outcome)

    elif problem.language_choices == 'Python':
        codefile_path = file_path+".py"
        code_f = open(codefile_path,'w')
        code_f.write(problem.source_code)
        code_f.close()
    
        cmd = 'python '+codefile_path
        
        for _ in range(testcase_range):
            
            st = ""
            for _ in range(testcase_line):
                st += in_f.readline()
            out = subprocess.Popen(cmd,shell=True,stdin = subprocess.PIPE,\
                stdout=subprocess.PIPE,stderr=subprocess.PIPE,\
                    errors='st')
            try:
                outcome,error=out.communicate(input = st,timeout = time)
            
            except subprocess.TimeoutExpired as e:
                process = psutil.Process(out.pid).children(recursive=True)
                for proc in process:
                    proc.kill()
                gone, alive = psutil.wait_procs(process,timeout=2)

            output = output+str(outcome)
    
    elif problem.language_choices == 'Oracle':
        
        codefile_path = file_path+".sql"
        code_f = open(codefile_path,'w')
        code_f.write(problem.source_code)
        code_f.close()
        cmd = "sqlplus -S system/orcl"
        f = open(codefile_path,'r')
        out = subprocess.Popen(cmd,shell=True,stdin = f,\
            stdout=subprocess.PIPE,stderr=subprocess.PIPE,\
                errors='st')
        try:
            outcome,error=out.communicate(timeout = 10)
        
        except subprocess.TimeoutExpired as e:
            process = psutil.Process(out.pid).children(recursive=True)
            for proc in process:
                proc.kill()
            gone, alive = psutil.wait_procs(process,timeout=2)
        
        f.close()
        output = output+str(outcome)



    """
    with tempfile.TemporaryDirectory(prefix='Codes',dir=BASE_DIR) as f:

        with open(f+'/'+a.title,'w+') as d:
            d.write(a.source_code)
            d.seek(0)
            out = subprocess.Popen(cmd,shell=True,stdin = subprocess.PIPE,\
                 stdout=subprocess.PIPE,stderr=subprocess.PIPE,\
                       cwd =f,errors='st')
            try:
                if a.language_choices=='4':
                    output,error=out.communicate(input=a.given_input,timeout=a.time_limit)
                else:
                    out.communicate(timeout=a.time_limit)
            
            except subprocess.TimeoutExpired as e:
                process = psutil.Process(out.pid).children(recursive=True)
                for proc in process:
                    proc.kill()
                gone, alive = psutil.wait_procs(process,timeout=a.time_limit)
                return HttpResponse(e)
            else:
                if a.language_choices=='1' or a.language_choices=='2':
                    cmd ='out.exe'
                if a.language_choices=='3':
                    cmd = 'java '+name
                if a.language_choices=='1' or a.language_choices=='3':
                    out = subprocess.Popen(cmd,shell=True,cwd=f,stdin = subprocess.PIPE,\
                    stdout=subprocess.PIPE,stderr=subprocess.PIPE,errors='st')
                try:
                    output,error = out.communicate(timeout=30)               
                except subprocess.TimeoutExpired as e:
                    process = psutil.Process(out.pid).children(recursive=True)
                    for proc in process:
                        proc.kill()
                    gone, alive = psutil.wait_procs(process,timeout=a.time_limit)
                    output,error = out.communicate()
                    return HttpResponse(e)
    """
    if os.path.exists(input_file_path):
        in_f.close()
    
    r = Result()
    
    r.problem = problem

    if error:
        r.answer = "runtime error"
    elif output:
        outfile_path = settings.MEDIA_ROOT+"\\"+"output_file"+"\\"+problem.title+"_"+str(problem.id)+".txt"
        f = open(outfile_path,"w")
        f.write(output)
        f.close()
        testfile_path = settings.MEDIA_ROOT+"\\"+"testcase"+"\\"+problem.title+".txt"
        cmd = "fc "+outfile_path+" "+testfile_path
        out = subprocess.Popen(cmd,shell=True,stdin = subprocess.PIPE,\
                 stdout=subprocess.PIPE,stderr=subprocess.PIPE,\
                       errors='st')
        output,error=out.communicate()
        print("output2",output,"error2",error)
        comp = filecmp.cmp(outfile_path, testfile_path,shallow = False)
        if comp == True:
            r.answer = "accepted"
        else:
            r.answer = "Not accepted"

    elif e:
        r.answer = "Time limit"
    first_file = settings.MEDIA_ROOT+"\\"+"output_file"+"\\"+problem.title+"_"+str(problem.id)+".txt"
    second_file = settings.MEDIA_ROOT+"\\"+"testcase"+"\\"+problem.title+".txt"
    working_path = settings.BASE_DIR+"\\"+"templates"+"\\"+"reports"

    first_file_lines = open(first_file).readlines()
    second_file_lines = open(second_file).readlines()
    r.report = difflib.HtmlDiff().make_file(first_file_lines,second_file_lines,first_file,second_file)

    r.save()
def exam_paper_judge():
    q_set = Question_Set.objects.get(id=id)
