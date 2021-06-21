from flask import Flask, render_template, url_for, flash, redirect, request
import json
import math

app = Flask(__name__)

def project(path):
    f = open(path, 'r')
    str = f.read()
    lines = ''
    lines = str
    lines.upper()
    # lines = [str.replace(' ', '') for str in lines]
    #  number_of_characters = len(lines)
    return lines
    # termfrequency(lines)
    # ------
 
def termfrequency(lines):
    d = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}
    for i in lines:
        if i == " " :continue
        char = i
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    max = 0
    for i in d:
        if d[i] > max:
            max = d[i]
    for i in d:
        d[i] = d[i] / max
    print (d)
    return d


def idf(A={}, B={}, C={}, D={}, E={}, F={}):
    characters = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}
    for i in characters:
        count = 0
        if i in A:
            count += 1
        if i in B:
            count += 1
        if i in C:
            count += 1
        if i in D:
            count += 1
        if i in E:
            count += 1
        if i in F:
            count += 1
        if count == 0:
            characters[i] = 0
        else:
            characters[i] = math.log((3 / count), 2)
           # print (characters)
    return characters


def idftf(tf={}, idf={}):
    for i in tf:
        if i in idf:
            tf[i] = tf[i] * idf[i]
    return tf


def innerproduct(tf1={}, tf2={}):
    d = 0
    for i in tf1:
        if i in tf2:
            d += tf1[i] * tf2[i]
    return d


def sigmamul(tf1={}):
    d = 0
    for i in tf1:
        d += math.pow(tf1[i], 2)
    return d


def cossim(innerproduct1, multi1, multi2):
    d = (innerproduct1 / (math.sqrt(multi1 * multi2)))
    return d

@app.route('/')

def home():
    return render_template('index.html', show=False)

@app.route('/google', methods=['GET', 'POST'])

def my_form_post():
    if request.method == 'POST':
        query = request.form['query']
        return vectorSpaceModel(query)
    
def vectorSpaceModel(query):
    d1=project('D:\\IR\\project final\\project0.txt')
    d2=project('D:\\IR\\project final\\project1.txt')
    d3= project('D:\\IR\\project final\\project2.txt')

    d1 = termfrequency(d1)
    d2 = termfrequency(d2)
    d3 = termfrequency(d3)
    query = termfrequency(query)
    #print(d1,d2,d3,query)
    idfd = idf(d1, d2, d3, query)

    d1 = idftf(d1, idfd)
    d2 = idftf(d2, idfd)
    d3 = idftf(d3, idfd)
    query = idftf(query, idfd)
    results = {"project0": cossim(innerproduct(d1, query), sigmamul(d1), sigmamul(d1)),
               "project1": cossim(innerproduct(d2, query), sigmamul(d2), sigmamul(d2)),
               "project2": cossim(innerproduct(d3, query), sigmamul(d3), sigmamul(d3))}
    sorted_score = sorted(results.items(), key=lambda kv: kv[1], reverse=True)
    return json.dumps(sorted_score)

if __name__ == '__main__':
    app.debug = True
    app.run()

    