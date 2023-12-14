from flask import Flask,request,render_template

obj=Flask(__name__)                        # Create a object of module

@obj.route('/')                 #create the url
def welcome():
    return "Welcome to the flask"


@obj.route('/cal',methods=["GET"])
def math_operator():
    operation=request.json["operation"]
    number1=request.json["number1"]
    number2=request.json["number2"]

    if operation=="add"
        result=number1+number2
    elif operation=="multiply":
        result=number1*number2
    elif operation=="Division":
        result=number1/number2
    else:
        result=number1-number2

    return result



print(__name__)

if __name__=='__main__':
    obj.run(debug=True)
