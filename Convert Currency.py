# start 
 
import requests  # module requests
print ("Hello mr ") 
init_currency = str(input("Entre an initial currency : "))
target_currency =  str (input ("Entre an target currency : "))


while True :
    amount = float (input(   f"please amount currency you want from {init_currency}  to {target_currency}") )
    if (amount  <=0  ) :
         print("The amount must be greater than 0 ")
         continue
    else :
        break 

url = ("https://api.apilayer.com/fixer/convert?to="
       + target_currency + "&from=" + init_currency
       + "&amount=" + str(amount))

payload = {}
headers = {
    "apikey": "8juraaxZMK8Vf8AsZMKJyKZ7LF5lpmD9"
}

response = requests.request("GET", url, headers=headers, data=payload)
status_code = response.status_code
if (status_code  != 200) :
    print("Sorry, there was a problem. Please try again later.")
    quit()
else :
    result =  response.json() ;
    convert_currency= result["result"] 
    print(  f"this is  a  result operations conventions form {init_currency} to {target_currency}  amount is {amount }  equal {convert_currency} ")
        
        
