from backend import create_app  #importingt the factory function
print ("creating application")
app= create_app()  #creating aninstance for the app
print("Application created!")
if __name__=="__main__":  
    print("Running application...") 
    app.run(debug=True)    #Running the app with debug mode on