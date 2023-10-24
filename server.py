from flask import Flask, render_template, request
from search import search
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def search_box():
    if request.method == 'POST':

        query = request.form['searchTerm']
        
        type_of_query = request.form['typequeery']
        res = search(query,type_of_query)

        hits = res['hits']['hits']
        aggs = res['aggregations']
        print(aggs)
        num_results = len(hits)
        
        return render_template('index.html',query=query,hits=hits,num_results=num_results,aggs=aggs)
    
    if request.method == 'GET':
        return render_template('index.html',init='True')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=3000,debug=True)