from os import error
from flask import Flask, request, jsonify, abort,render_template,abort
from datetime import datetime
import random
# from flask_cors import CORS

#Init

app = Flask(__name__)
# enable CORS
# CORS(app, resources={r'/*': {'origins': '*'}})

class Validators:

    def creditCardValidator(self,cardNumber):
        return True

    def ExpirationDateValidator(self,given_date_string):
        curr_date_str = datetime.now().strftime("%Y-%m-%d")
        curr_date_obj = datetime.strptime(curr_date_str,"%Y-%m-%d")
    
        given_date_obj = datetime.strptime(given_date_string,"%Y-%m-%d")
        res = False
        if( given_date_obj.date() != curr_date_obj.date() ):#can compare diffferent params, there should be some time limit
            res = False
        else:
            res = True
        return res

    def AmountValidator(self,given_amount):
        if( isinstance(given_amount,float) and given_amount > 0.00 ):
            return True
        else:
            return False

    def Is_valid(self,cardNumber,given_date,given_amount):
        if( self.creditCardValidator(cardNumber) and self.ExpirationDateValidator(str(given_date)) and self.AmountValidator(given_amount) ):
            return True
        else:
            return False



class PaymentGateway:

    def PremiumPaymentGateway(self):
        rand_number = random.randint(1,10)
        print(rand_number)
        if( rand_number > 7 ):
            print("PremiunPaymentGateway used")
            return True
        else:
            return False
            

    def ExpensivePaymentGateway(self):
        print("ExpensivePaymentGateway used")
        return True
    
    def CheapPaymentGateway(self):
        print("CheapGateway used")
        return True
        
    
    def PaymentHandler(self,amount):

        if( amount < 20.00 ):
            self.CheapPaymentGateway()
            return True

        if ( amount >20.00 and amount <=500.00 ):
            if(self.ExpensivePaymentGateway() ):
                return True
            else:
                return self.CheapPaymentGateway()

        if( amount > 500.00 ):
            success = False
            for tries in  range(0,3):
                    if( self.PremiumPaymentGateway() ):
                        success = True
                        return True
                    else:
                        pass

            return success

#api route
@app.route("/",methods = ['GET','POST'])
def ProcessPayment():
    if request.method == 'POST':
    
        req  = request.get_json()
        resp = {}
        if (len(req)) != 5:
            abort(400,"Invalid request")

        payment_object  = PaymentGateway()
        validator_object= Validators()
        if( validator_object.Is_valid(req['CreditCardNumber'], req['ExpirationDate'], req['Amount']) ):
            if(payment_object.PaymentHandler(req["Amount"])):
                resp.update({"200":"OK"})
            else:
                abort(500,"Internal Error")
        else:
            abort(400,"Invalid request")
    


        return jsonify(resp)


    elif request.method == 'GET':
        print("GET request")
        return (f"<h1>hello!</h1>")


if __name__ == '__main__':
    app.run(debug=True,port=5000)