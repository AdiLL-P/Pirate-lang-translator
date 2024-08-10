import requests                                                                            
global repeat                                                                             
repeat = "y"                                                                                 
class translator:                                                                          
    def translate(self):                                                                  
        value = repeat
        while value == 'y':                                                               
            url = "https://api.funtranslations.com/translate/pirate.json"                
            text = input("Enter text in English to Translate into Pirate language : ")     
            send_request = requests.get(f'{url}?text={text}')                              
            recieved_json = send_request.json()                                            
            slicing_json_1 = recieved_json["contents"]                                     
            slicing_json_2 = slicing_json_1["translated"]                             
            print(f"""Your text : {text}                                                    
Translated Text : {slicing_json_2}""")                                                    
            value = input("Enter y to try again or any key to stop : ")                  
        if value != "y":                                                                   
            print("Thanks for using my program!!!")
 
                                                                        
translator_instance = translator()                                                      
translator_instance.translate()                                                           