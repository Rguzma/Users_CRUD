from flask import Flask, render_template, request, redirect      #FIRST STEP
from users import User                                      #4TH STEP
app = Flask(__name__)
@app.route('/')                                             #FIRST STEP
def index():                                                #FIRST STEP 
    return redirect('/users') 
    

@app.route('/users')                                        #4TH STEP
def users():
    return render_template("users.html", users=User.get_all())

# @app.route('/create_friend', methods=["POST"])
# def create_friend():
#     # First we make a data dictionary from our request.form coming from our template.
#     # The keys in data need to line up exactly with the variables in our query string.
#     data = {
#         "fname": request.form["fname"],
#         "lname" : request.form["lname"],
#         "occ" : request.form["occ"]
#     }
#     # We pass the data dictionary into the save method from the Friend class.
#     Friend.save(data)
#     # Don't forget to redirect after saving to the database.
#     return redirect('/')

if __name__ == "__main__":                                     #FIRST STEP
    app.run(debug=True)                                        #FIRST STEP