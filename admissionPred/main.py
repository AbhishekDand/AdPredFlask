
# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle

#this are the libraries you will have to install for your flask app

app = Flask(__name__) # initializing a flask app
# we give name to our app

@app.route('/',methods=['GET'])  # route to display the home page. @app.route() takes the user to the page which we want to
# here '/' means we are sending user to the default route.
@cross_origin()
def homePage():
    return render_template("index.html")
	#index.html is our deafult route. render_template is a function in flask which calls the requested html page on route
	#In index.html we have a html form which takes input from our user which we will use in next route for prediction.
@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
#this is our second route as we want data from our form we have used methods POST and GET
@cross_origin()
def index():
    if request.method == 'POST':
        try:
			#This block of code takes the input from the html form and then we store it in a variable.
            #  reading the inputs given by the user
            gre_score=float(request.form['gre_score']) #we will see soon the html file from where we have taken this values
            toefl_score = float(request.form['toefl_score'])
            university_rating = float(request.form['university_rating'])
            sop = float(request.form['sop'])
            lor = float(request.form['lor'])
            cgpa = float(request.form['cgpa'])
            is_research = request.form['research']
            if(is_research=='yes'):
                research=1
            else:
                research=0
				#till this point we have read and stored all the data
				# now its simple we load our pickle file and then use predict() functions to make predictions
            filename = 'finalized_model.sav'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            prediction=loaded_model.predict([[gre_score,toefl_score,university_rating,sop,lor,cgpa,research]])
            print('prediction is', prediction)
			
			#we have made our predictions and saved in prediction variable.
			
            # showing the prediction results in a UI
			# we with rendering results.html template, send our prediction value which we will show in the results.html
            return render_template('results.html',prediction=round(100*prediction[0]))
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) # running the app
	#this lines are for running our flask apps. we can run our apps on localhost with specifying port.
	#By deafult it will runn on port 5000
	
	#now lets see html files
	
	
	
	