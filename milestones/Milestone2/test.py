import bot
import dbmodels
import database
import test_expectation_strings as exp

#Things to test
  #database.py
      #Database
          #connect
          #select
  #bot.py
      #BotResponse
          #__init__
          #parse_command
      #selected_user
      #all_properties
      #selected_property
      #all_applications
      #all_firms
      #all_ecommercesites
      #find_user_screenname
      #all_user_no_account
      #users_more_x_properties
      #user_bedrooms_under_monthly
      #property_same_rooms_cheaper
      #properties_pets_laundry
      #properties_firm
      #properties_stories
      #properties_space_between_yearly
      #properties_masterbedroom
      #properties_hoafees_monthly
      #property_saved_and_applied
      #properties_bedrooms_bathrooms
      #properties_same_user
      #properties_same_zipcode
      #properties_same_state_dif_zipcode
      #properties_cheaper_same_city
      #ecom_ads
      #user_applications
      #applications_lastname

  #dbmodels.py
      #DataHandler
          #__init__
          #runQuery
      #User
          #__init__
          #load
          #__str___
      #Property
          #__init__
          #loadQuick
          #loadDetails
          #quickDetails
          #__str__
      #Application
          #__init__
          #load
          #__str___
      #Advertisement
          #__init__
          #load
          #__str___
      #Firm
          #__init__
          #load
          #__str___
      #ECommerceSite
          #__init__
          #load
          #__str___

#How to test
  #Database - Basic
  #BotResponse
    #parse_command - Feed it every command. Compare it to Expected Output -> Compare it to all expected outputs.
  #All Functions would be tested for comparisons.
  #Pass all Versions of input to get all errors. 
  #Create a Feed Function.
  #Create a Compare function.
  #DataHandler - runQuery, run all models, and pass 1 item to get a response. Compare to expected
  #Models - Send in a an input, compare to expected
  #Models - Send in an non existent input, compare it to expected.

def Test_Compare(label,actual,expected):
  if actual == expected:
    print(f"[PASSED] => {label}")
  else:
    print(f"[FAILED] => {label}")

#Function to Inject the bot with the entered string
#Done to shorten the Test Compare Syntax
def inject(message):
  return bot.BotResponse(message).parse_command()

def Test_Parse_Command_All_Commands():

  #Test_Compare("", inject(""),"")
  Test_Compare("test", inject("test"), "test")
  Test_Compare("test 1 2 3", inject("test 1 2 3"), "test 1 2 3")
  Test_Compare("!", inject("!"), "ERROR - No command called")
  Test_Compare("!help", inject("!help"), "Please refer to the #commands channel to see the list of commands that are available for use")
  Test_Compare("!users", inject("!users"), exp.TEST_EXP_USERS)
  Test_Compare("!users Unnecessary Arguments", inject("!users 1"),"!users ERROR - Unnecessary Arguments")
  Test_Compare("!user", inject("!user poncho@gmail.com"),exp.TEST_EXP_USER)
  Test_Compare("!user Argument Integer", inject("!user 1"),"!user ERROR - Argument is an Integer")
  Test_Compare("!user Argument Required", inject("!user"),"!user ERROR - Argument Required")
  Test_Compare("!user Too Many Arguments", inject("!user 1 1"),"!user ERROR - Too Many Arguments")
  Test_Compare("!user Not Found", inject("!user slim"),"User not found")
  Test_Compare("!properties", inject("!properties"),exp.TEST_EXP_PROPERTIES)
  Test_Compare("!properties Unnecessary Arguments", inject("!properties 1"),"!properties ERROR - Unnecessary Arguments")
  Test_Compare("!property", inject("!property 1"),exp.TEST_EXP_PROPERTY)
  Test_Compare("!property Not an Integer", inject("!property a"),"!property ERROR - Argument is not an Integer")
  Test_Compare("!property Argument Required", inject("!property"),"!property ERROR - Argument Required")
  Test_Compare("!property Too Many Arguments", inject("!property a b"),"!property ERROR - Too Many Arguments")
  Test_Compare("!property No Property Found", inject("!property 10"),"No Property found")
  Test_Compare("!applications", inject("!applications"),exp.TEST_EXP_APPLICATIONS)
  Test_Compare("!applications Unnecessary Arguments", inject("!applications 1"),"!applications ERROR - Unnecessary Arguments")
  Test_Compare("!firms", inject("!firms "),exp.TEST_EXP_FIRMS)
  Test_Compare("!firms Unnecessary Arguments", inject("!firms 1"),"!firms ERROR - Unnecessary Arguments")
  Test_Compare("!ecommercesites", inject("!ecommercesites"),exp.TEST_EXP_ECOMSITES)
  Test_Compare("!ecommercesites Unnecessary Arguments", inject("!ecommercesites 1"),"!ecommercesites ERROR - Unnecessary Arguments")
  
  #print(inject("!ecommercesites"))