from flask import Flask, render_template, url_for, flash, redirect, request
import json
import os
import random
import string

app = Flask(__name__)

def generateRandomFiles():
    for n in range(3):
        filename = "D:\\IR\\project final\\project" + str(n) + ".txt"
        afile = open(filename, "w+" )
        for i in range(int(10)):
            line =''.join([random.choice(string.ascii_letters[26:32])])
        return afile.write(line)
      #  print(line)

def format_input(input_str):
    dict_input = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0}
    if input_str == "":
        return dict_input
    input_str = input_str.split(";")
    for i in input_str:
        x = i.replace(" ", "").split(":")
        dict_input[x[0]] = float(x[1])
        #print (dict_input)
    return dict_input

def project(path, query):
    f = open(path, 'r')
    str = f.read()
    lines = ''
    lines = str
    lines.upper()
    #print (lines)
    lines = [str.replace(' ', '') for str in lines]
   # number_of_characters = len(lines)
    count_freqOFEach =count_frequency(lines)
    
    #print(count_freqOFEach)
    return score(count_freqOFEach,query)
    # ------
 
def count_frequency(lines):
    d = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0}
   # print ("teeeeeeeeeeeeeeeeeeeeeeeeeeeeeeestttttttttttttttttttt",lines)

    for i in range(0, len(lines)):
        char = lines[i]
        d[char] += 1
        
    for i in d:
        d[i]/=len(lines)
    print (d)
    return d


def score(count_frequency,dict_input):
        score_dict = 0
       # print (count_frequency,dict_input)
        for i in dict_input:
            score_dict += float(float(dict_input[i]) * count_frequency[i])
           # print (score_dict)
        return score_dict


   # l = []
    #l.append(score)
   # l.append(path)
   # return l
    #f.close()

# def main(query_in={}, ):
#     list_of_scores = []
#     list_of_scores.append(project('D:\\IR\\project final\\project.txt', query=query_in))
#     list_of_scores.append(project('D:\\IR\\project final\\project1.txt', query=query_in))
#     list_of_scores.append(project('D:\\IR\\project final\\project2.txt', query=query_in))
#     list_of_scores.sort(reverse=True)
 
#     dict_out = {}
#     for i in range(0, 3):
#         dict_out[list_of_scores[i][1]] = list_of_scores[i][0] 
#     print('the list of ranked scores', list_of_scores)
#     return dict_out

@app.route('/')

def home():
    return render_template('index.html', show=False)

@app.route('/google', methods=['GET', 'POST'])

def my_form_post():
    if request.method == 'POST':
        text = request.form['query']
        scores= statisticalModel(text)    
    return scores
    
@app.route('/generate', methods=['GET', 'POST'])
def my_generate_post():
    if "generate" in request.form.keys():
        generateRandomFiles()
        return "file generated"
        


  #  if request.method == 'POST':
   #     if request.form['query'] == 'query':
    #        text = request.form['query']
     #       scores= statisticalModel(text)
      #  else: request.form['generate'] == 'generate':
       #     generateRandomFiles()

     #if request.method == "POST":
      #   if request.form.get("query"):
       #      text = request.form['query']
      #       scores= statisticalModel(text)
      #   elif request.form.get("Generate random files"):
       #      generateRandomFiles()

    
def statisticalModel(text):
    query=format_input(text)
    list_of_scores = []
    list_of_scores.append(project('D:\\IR\\project final\\project0.txt', query))
    list_of_scores.append(project('D:\\IR\\project final\\project1.txt', query))
    list_of_scores.append(project('D:\\IR\\project final\\project2.txt', query))
    list_of_scores.sort(reverse=True)
    return json.dumps(list_of_scores)

if __name__ == '__main__':
    app.debug = True
    app.run()