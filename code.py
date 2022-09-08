class MiniCurrencyConverter(object):
    """This program calculates the exchange rate from a currency to another"""
    def CalcRate():
        #ECHO is on.
        # This program converts between two currencys
        # written by Mahmud Shuaib 
        # 09/08/2022        
        # Declaring Variables 
        aud_rate = 286.95 # 1 AUD = 286.95 Naira 
        us_rate = 422.0 # 1 USD = 422 Naira 
        naira_rate = 0
        # get user input 
        print("******************************")
        try:
            aud_input = float(input("Enter Amount in AUD: ")) # casting the input to float 
        except ValueError:
            print("Enter Numbers only eg 2")
        finally:
            print("")
        naira_rate = aud_input * aud_rate # store the multiplication of aud rate to naira rate
        
        print(f"AUD ${aud_input:,.2f} is: NGN N{naira_rate:,.2f} @{aud_rate} aud/n") # storing our result here
        # simple printing 
        #print(naira_rate) 
        print("******************************")
# creating an instance of the class so we can use the CalcRate() method 
# also calling the method from the main class 
# using __name__ == "__main__" is a good way to do this 
if __name__ == "__main__":      
    obj_calc = MiniCurrencyConverter.CalcRate()
    # note: we could call the method by creating the instance first
    # using 
    # obj_calc = MiniCurrencyConverter()
    # then we use 
    # obj_calc.CalcRate() to call the method 


