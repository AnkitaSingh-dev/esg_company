from flask import Flask, jsonify, request
import os
from flask_restful import Api, Resource
from flask_cors import CORS
import pandas as pd
app = Flask(__name__)
api = Api(app)
CORS(app)
wiki = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
class Company(Resource):
    def get(self):
        wiki = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
        first_table = wiki[0]
        second_table = wiki[1]
        df = first_table
        df_date_filter = df[df['Date added'] < '2023-01-01'].copy()
        company=[]
        for i in range(df_date_filter.shape[0]):
            try:
                company.append({"Symbol":df_date_filter['Symbol'][i],"Security":df_date_filter['Security'][i],"GICS Sector":df_date_filter['GICS Sector'][i],"GICS Sub-Industry":df_date_filter['GICS Sub-Industry'][i]})
            except:
                pass

        return jsonify(company)
        
    




api.add_resource(Company, '/company')

if __name__=="__main__":
     port = int(os.environ.get('PORT', 33507))
     app.run( port=port, debug=True)