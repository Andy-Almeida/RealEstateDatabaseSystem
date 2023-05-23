import bot_commands
import dbmodels

class BotResponse:

  def __init__(self, msg):
    self.responseData = str(None)
    self.msg = msg
    self.msg_data = self.msg.split()
    self.command = self.msg_data[0]
    self.arguments = self.msg_data[1:]

  def parse_command(self):
    #Test Command - Returns "test" + all arguments
    if self.command == "test":
      self.responseData = self.command
      for arg in self.arguments:
        self.responseData += ' ' + arg
    
    #! - Returns ERROR statement
    elif self.command == "!":
      return "ERROR - No command called"
      
    #!help - Returns Help statment
    elif self.command == "!help":
      return "Please refer to the #commands channel to see the list of commands that are available for use"

    #!users - Returns all users data
    elif self.command == bot_commands.ALL_USERS:
      self.responseData = all_users(self.arguments)

    #!user - Returns data on a single user using thier Email
    elif self.command == bot_commands.SELECTED_USER:
      self.responseData = selected_user(self.arguments)

    #!properties - Returns all properties data
    elif self.command == bot_commands.ALL_PROPERTIES:
      self.responseData = all_properties(self.arguments)

    #!property - Returns data on a single property using thier property_id
    elif self.command == bot_commands.SELECTED_PROPERTY:
      self.responseData = selected_property(self.arguments)

    #!applications - Returns all applications
    elif self.command == bot_commands.ALL_APPLICATIONS:
      self.responseData = all_applications(self.arguments)

    #!firms - Returns all applications
    elif self.command == bot_commands.ALL_FIRMS:
      self.responseData = all_firms(self.arguments)

    #!ecommercesites - Return all ECommerceSites
    elif self.command == bot_commands.ALL_ECOMMERCESITES:
      self.responseData = all_ecommercesites(self.arguments)

    #!user-screenname - Returns data on a single user using thier Screenname
    elif self.command == bot_commands.FIND_USER_SCREENNAME:
      self.responseData = find_user_screenname(self.arguments)

    #!users-no-account - Returns data on a single user that have an empty account
    elif self.command == bot_commands.ALL_USERS_NO_ACCOUNT:
      self.responseData = all_user_no_account(self.arguments)

    #!users-more-than-x-properties - Returns data on all users that have more than x properties
    elif self.command == bot_commands.USERS_MORE_X_PROPERTIES:
      self.responseData = users_more_x_properties(self.arguments)

    #!user-x-bedrooms-under-x-monthly #For a selected user, find the properties that they own that have <x> bedrooms and the monthly price range is below <x> monthly cost
    elif self.command == bot_commands.USER_BEDROOMS_UNDER_MONTHLY:
          self.responseData = user_bedrooms_under_monthly(self.arguments)

    #!properties-x-bedrooms-x-bathrooms Returns properties that have <x> bedrooms and <x> bathrooms
    elif self.command == bot_commands.PROPERTIES_BEDROOMS_BATHROOMS:
      self.responseData = properties_bedrooms_bathrooms(self.arguments)

    #!properties-allowspets-haslaundry Returns properties in a given city that allows pets and has laundry in-unit
    elif self.command == bot_commands.PROPERTIES_PETS_LAUNDRY:
      self.responseData = properties_pets_laundry(self.arguments)

    #!properties-firm - Return all properties that are linked to <x> firm
    elif self.command == bot_commands.PROPERTIES_FIRM:
      self.responseData = properties_firm(self.arguments)

    #!properties-x-stories - Return properties that have <x> stories
    elif self.command == bot_commands.PROPERTIES_STORIES:
      self.responseData = properties_stories(self.arguments)

    #!properties-x-space-and-between-x-and-x-yearlyprice Return properties that exceed <x> livable area and is between <x> and <x> yearly price
    elif self.command == bot_commands.PROPERTIES_SPACE_BETWEEN_YEARLY:
      self.responseData = properties_space_between_yearly(self.arguments)

    #!properties-masterbedroom-bigger-than-x Return properties that have a masterbedroom that is bigger than <x> area
    elif self.command == bot_commands.PROPERTIES_MASTERBEDROOM:
      self.responseData = properties_masterbedroom(self.arguments)

    #!properties-lessthan-x-hoa-and-morethan-x-monthly Return properties that have less than <x> hoafees but more than <x> monthlycost
    elif self.command == bot_commands.PROPERTIES_HOAFEES_MONTHLY:
      self.responseData = properties_hoafees_monthly(self.arguments)

    #!property-saved-and-applied Return the users that have saved it and sent an application given a property 
    elif self.command == bot_commands.PROPERTY_SAVED_AND_APPLIED:
      self.responseData = property_saved_and_applied(self.arguments)
     
    #!property-similar-room-count-but-cheaper Return all properties that have the same amount of rooms but cost less per month given a property
    elif self.command == bot_commands.PROPERTY_SAME_ROOMS_CHEAPER:
      self.responseData = property_same_rooms_cheaper(self.arguments)
      
    #!property-same-user Return properties listed by the same user, given a property
    elif self.command == bot_commands.PROPERTY_SAME_USER:
      self.responseData = properties_same_user(self.arguments)

    #!property-same-zipcode Return all properties in the same zipcode, given a property
    elif self.command == bot_commands.PROPERTY_SAME_ZIPCODE:
      self.responseData = properties_same_zipcode(self.arguments)

    #!property-same-state-different-zipcode Return properties in the same state but not in the same zipcode, given a property
    elif self.command == bot_commands.PROPERTY_SAME_STATE_DIF_ZIPCODE:
      self.responseData = properties_same_state_dif_zipcode(self.arguments)

    #!property-cost-less-same-city Return all properties that cost less but is in the same city, given a property
    elif self.command == bot_commands.PROPERTY_CHEAPER_SAME_CITY:
      self.responseData = properties_cheaper_same_city(self.arguments)

    #!ecommercesites-ads - Return all advertisements that that are linked to an External E-Commerce Website
    elif self.command == bot_commands.ECOM_ADS:
      self.responseData = ecom_ads(self.arguments)
    
    #!user-x-applications - Returns the applications that were sent to a property by a user 
    elif self.command == bot_commands.USER_APPLICATIONS:
      self.responseData = user_applications(self.arguments)

    #!applications-by-lastname - Return all applications made by users with <x> lastname
    elif self.command == bot_commands.APPLICATIONS_LASTNAME:
      self.responseData = applications_lastname(self.arguments)
      
    #Return the Data Collected
    if self.responseData:
      return self.responseData

def all_users(arguments):
  query = """SELECT RegisteredUser.email FROM `RegisteredUser`;"""
  if len(arguments) == 0:
    data = dbmodels.DataHandler("User", query).data
  else:
    return "!users ERROR - Unnecessary Arguments"  
  if data:
    return data
  data = "No Users found"
  return data

def selected_user(arguments):
  query = """SELECT * FROM `RegisteredUser` WHERE `email` = %s;"""
  if len(arguments) == 1:
    try:
      arguments = int(arguments[0])
      return "!user ERROR - Argument is an Integer"
    except ValueError:
      data = dbmodels.DataHandler("User", query, arguments).data
  elif len(arguments) == 0:
    return "!user ERROR - Argument Required"
  elif len(arguments) > 1:
    return "!user ERROR - Too Many Arguments"
  if data:
    return data
  data = "User not found"
  return data

def all_properties(arguments):
  query = """SELECT Property.property_id FROM Property;"""
  if len(arguments) == 0:
    data = dbmodels.DataHandler("PropertyQuick", query).data
  else:
    return "!properties ERROR - Unnecessary Arguments"  
  if data:
    return data
  data = "No Properties found"
  return data

def selected_property(arguments):
  query = """SELECT Property.property_id FROM `Property` WHERE `property_id` = %s;"""
  if len(arguments) == 1:
    try:
      arguments = int(arguments[0])
      data = dbmodels.DataHandler("PropertyFull", query, arguments).data
    except ValueError:
      return "!property ERROR - Argument is not an Integer"
  elif len(arguments) == 0:
    return "!property ERROR - Argument Required"
  elif len(arguments) > 1:
    return "!property ERROR - Too Many Arguments"
  if data:
    return data
  data = "No Property found"
  return data

def all_applications(arguments):
  query = """SELECT Application.app_id FROM `Application`;"""
  if len(arguments) == 0:
    data = dbmodels.DataHandler("Application", query).data
  else:
    return "!applications ERROR - Unnecessary Arguments"  
  if data:
    return data
  data = "No Applications found"
  return data

def all_firms(arguments):
  query = """SELECT Firm.firm_id FROM `Firm`;"""
  if len(arguments) == 0:
    data = dbmodels.DataHandler("Firm", query).data
  else:
    return "!firms ERROR - Unnecessary Arguments"  
  if data:
    return data
  data = "No Firms found"
  return data

def all_ecommercesites(arguments):
  query = """SELECT ExternalECommerceSites.name FROM `ExternalECommerceSites`;"""
  if len(arguments) == 0:
    data = dbmodels.DataHandler("EComSite", query).data
  else:
    return "!ecommercesites ERROR - Unnecessary Arguments"  
  if data:
    return data
  data = "No ECommerceSites found"
  return data

def find_user_screenname(arguments):
  query = """SELECT RegisteredUser.email FROM `RegisteredUser` JOIN `Profile` ON RegisteredUser.email = Profile.user WHERE Profile.screenname = %s;"""
  if len(arguments) == 1:
    try:
      arguments = int(arguments[0])
      return "!user-screenname ERROR - Argument is an Integer"
    except ValueError:
      data = dbmodels.DataHandler("User", query, arguments).data
  elif len(arguments) == 0:
    return "!user-screenname ERROR - Argument Required"
  elif len(arguments) > 1:
    return "!user-screenname ERROR - Too Many Arguments"
  if data:
    return data
  data = "User not found"
  return data

def all_user_no_account(arguments):
  query = """SELECT RegisteredUser.email FROM `RegisteredUser` JOIN `Account` ON RegisteredUser.email = Account.user WHERE Account.profession IS NULL AND Account.firstname IS NULL AND Account.lastname IS NULL AND Account.zipcode IS NULL AND Account.phonenumber IS NULL AND Account.firm IS NULL;"""
  if len(arguments) == 0:
    data = dbmodels.DataHandler("User", query).data
  else:
    return "!users-no-account ERROR - Unnecessary Arguments"  
  if data:
    return data
  data = "No Users found"
  return data

def users_more_x_properties(arguments):
  query = """SELECT ru.email FROM `RegisteredUser` ru INNER JOIN `Property` p ON ru.email = p.user GROUP BY ru.email HAVING COUNT(*) > %s;"""
  if len(arguments) == 1:
    try:
      arguments = int(arguments[0])
      data = dbmodels.DataHandler("User", query, arguments).data
    except ValueError:
      return "!users-more-than-x-properties ERROR - Argument is not an Integer"
  elif len(arguments) == 0:
    return "!users-more-than-x-properties ERROR - Argument Required"
  elif len(arguments) > 1:
    return "!users-more-than-x-properties ERROR - Too Many Arguments"
  if data:
    return data
  data = "No User found"
  return data

def user_bedrooms_under_monthly(arguments):
  query = """SELECT Property.property_id, Property.user 
             FROM Property 
             INNER JOIN HOAFinancials ON Property.property_id = HOAFinancials.property 
             INNER JOIN InteriorFactsandFeatures ON Property.property_id = InteriorFactsandFeatures.property 
             WHERE Property.user = %s 
              AND InteriorFactsandFeatures.bedrooms = %s
              AND HOAFinancials.monthprice < %s;"""
  if len(arguments) == 3:
    try:
      arguments[0] = int(arguments[0])
      return "!user-x-bedrooms-under-x-monthly ERROR - Argument 1 is an Integer"
    except ValueError:
      try:
        arguments[1] = int(arguments[1])
        try:
          arguments[2] = int(arguments[2])
          data = dbmodels.DataHandler("PropertyFull", query, arguments).data
        except ValueError:
          return "!user-x-bedrooms-under-x-monthly ERROR - Argument 3 is not an Integer"
      except ValueError:
          return "!user-x-bedrooms-under-x-monthly ERROR - Argument 2 is not an Integer"
  elif len(arguments) < 3:
    return "!user-x-bedrooms-under-x-monthly ERROR - Argument Required"
  elif len(arguments) > 3:
    return "!user-x-bedrooms-under-x-monthly ERROR - Too Many Arguments"
  if data:
    return data
  data = "No Proprety found"
  return data

def property_same_rooms_cheaper(arguments):
  query = """SELECT Property.property_id
              FROM Property
              JOIN InteriorFactsandFeatures ON Property.property_id = InteriorFactsandFeatures.property
              JOIN HOAFinancials ON Property.property_id = HOAFinancials.property
              WHERE (InteriorFactsandFeatures.bedrooms + InteriorFactsandFeatures.bathroom) = (SELECT (bedrooms + bathroom) FROM InteriorFactsandFeatures WHERE property = %s)
              AND HOAFinancials.monthprice < (SELECT monthprice FROM HOAFinancials WHERE property = %s);"""
  if len(arguments) == 1:
    try:
      arguments[0] = int(arguments[0])
      arguments.append(arguments[0])
      data = dbmodels.DataHandler("PropertyFull", query, arguments).data
    except ValueError:
      return "!properties-x-bedrooms-x-bathrooms  ERROR - Argument is not an Integer"
  elif len(arguments) ==0 :
    return "!properties-x-bedrooms-x-bathrooms  ERROR - Argument Required"
  elif len(arguments) > 1:
    return "!properties-x-bedrooms-x-bathrooms  ERROR - Too Many Arguments"
  if data:
    return data
  data = "No Properties found"
  return data

def properties_pets_laundry(arguments):
  query = """SELECT Property.property_id, Property.user 
             FROM Property
             INNER JOIN Location ON Property.location = Location.loc_id
             INNER JOIN InteriorFactsandFeatures ON Property.property_id = InteriorFactsandFeatures.property
             WHERE Location.city = %s
              AND InteriorFactsandFeatures.pets != 'Not Allowed'
              AND InteriorFactsandFeatures.laundry != 'Not Included';"""
  if len(arguments) == 1:
    try:
      arguments = int(arguments[0])
      return "!properties-allowspets-haslaundry ERROR - Argument is an Integer"
    except ValueError:
      data = dbmodels.DataHandler("PropertyFull", query, arguments).data
  elif len(arguments) == 0:
    return "!properties-allowspets-haslaundry ERROR - Argument Required"
  elif len(arguments) > 1:
    return "!properties-allowspets-haslaundry ERROR - Too Many Arguments"
  if data:
    return data
  data = "No Properties found"
  return data

def properties_firm(arguments):
  query = """SELECT Property.property_id, Property.user, Firm.name
             FROM Property
             INNER JOIN RegisteredUser ON Property.user = RegisteredUser.email
             INNER JOIN Account ON RegisteredUser.email = Account.user
             INNER JOIN Firm ON Account.firm = Firm.firm_id
             WHERE Firm.firm_id = %s;"""
  if len(arguments) == 1:
    try:
      arguments = int(arguments[0])
      data = dbmodels.DataHandler("PropertyQuick", query, arguments).data
    except ValueError:
      return "!properties-firm ERROR - Argument is not an Integer"
  elif len(arguments) == 0:
    return "!properties-firm ERROR - Argument Required"
  elif len(arguments) > 1:
    return "!properties-firm ERROR - Too Many Arguments"
  if data:
    return data
  data = "No Properties found"
  return data

def properties_stories(arguments):
  query = """SELECT Property.property_id, Property.user, PropertyFactsandFeatures.stories 
             FROM Property
             INNER JOIN PropertyFactsandFeatures ON Property.property_id = PropertyFactsandFeatures.property 
             WHERE PropertyFactsandFeatures.stories = %s;"""
  if len(arguments) == 1:
    try:
      arguments = int(arguments[0])
      data = dbmodels.DataHandler("PropertyFull", query, arguments).data
    except ValueError:
      return "!properties-x-stories ERROR - Argument is not an Integer"
  elif len(arguments) == 0:
    return "!properties-x-stories ERROR - Argument Required"
  elif len(arguments) > 1:
    return "!properties-x-stories ERROR - Too Many Arguments"
  if data:
    return data
  data = "No Properties found"
  return data

def properties_space_between_yearly(arguments):
  query = """SELECT Property.property_id
             FROM Property 
             INNER JOIN HOAFinancials ON Property.property_id = HOAFinancials.property 
             INNER JOIN InteriorFactsandFeatures ON Property.property_id = InteriorFactsandFeatures.property 
             WHERE InteriorFactsandFeatures.totallivablearea > %s 
              AND HOAFinancials.pricerangehigh < %s 
              OR HOAFinancials.pricerangehigh IS NULL
              AND HOAFinancials.pricerangelow > %s;"""
  if len(arguments) == 3:
    try:
      arguments[0] = int(arguments[0])
      arguments[1] = int(arguments[1])
      arguments[2] = int(arguments[2])
      data = dbmodels.DataHandler("PropertyFull", query, arguments).data
    except ValueError:
      return "!properties-x-space-and-between-x-and-x-yearlyprice  ERROR - Argument is not an Integer"
  elif len(arguments) < 3:
    return "!properties-x-space-and-between-x-and-x-yearlyprice  ERROR - Argument Required"
  elif len(arguments) > 3:
    return "!properties-x-space-and-between-x-and-x-yearlyprice  ERROR - Too Many Arguments"
  if data:
    return data
  data = "No Properties found"
  return data

def properties_masterbedroom(arguments):
  query = """SELECT Property.property_id, Property.user, Room.name, Room.area
             FROM Property 
             INNER JOIN Room ON Property.property_id = Room.property 
             WHERE Room.area > %s
             AND Room.name = 'Master Bedroom';"""
  if len(arguments) == 1:
    try:
      arguments = int(arguments[0])
      data = dbmodels.DataHandler("PropertyFull", query, arguments).data
    except ValueError:
      return "!properties-masterbedroom-bigger-than-x ERROR - Argument is not an Integer"
  elif len(arguments) == 0:
    return "!properties-masterbedroom-bigger-than-x ERROR - Argument Required"
  elif len(arguments) > 1:
    return "!properties-masterbedroom-bigger-than-x ERROR - Too Many Arguments"
  if data:
    return data
  data = "No Properties found"
  return data

def properties_hoafees_monthly(arguments):
  query = """SELECT Property.property_id, Property.user, HOAFinancials.hoafee, HOAFinancials.monthprice
             FROM Property 
             INNER JOIN HOAFinancials ON Property.property_id = HOAFinancials.property 
             WHERE HOAFinancials.hoafee < %s 
              AND HOAFinancials.monthprice > %s;"""
  if len(arguments) == 2:
    try:
      arguments[0] = int(arguments[0])
      arguments[1] = int(arguments[1])
      data = dbmodels.DataHandler("PropertyFull", query, arguments).data
    except ValueError:
      return "!properties-lessthan-x-hoa-and-morethan-x-monthly  ERROR - Argument is not an Integer"
  elif len(arguments) < 2:
    return "!properties-lessthan-x-hoa-and-morethan-x-monthly  ERROR - Argument Required"
  elif len(arguments) > 2:
    return "!properties-lessthan-x-hoa-and-morethan-x-monthly  ERROR - Too Many Arguments"
  if data:
    return data
  data = "No Properties found"
  return data

def property_saved_and_applied(arguments):
  query = """SELECT RegisteredUser.email
              FROM RegisteredUser
              INNER JOIN SavedProperty ON RegisteredUser.email = SavedProperty.user
              INNER JOIN Application ON SavedProperty.property = Application.property
              WHERE SavedProperty.property = %s
                AND Application.user = SavedProperty.user;"""
  if len(arguments) == 1:
    try:
      arguments = int(arguments[0])
      data = dbmodels.DataHandler("User", query, arguments).data
    except ValueError:
      return "!property-saved-and-applied ERROR - Argument is not an Integer"
  elif len(arguments) == 0:
    return "!property-saved-and-applied ERROR - Argument Required"
  elif len(arguments) > 1:
    return "!property-saved-and-applied ERROR - Too Many Arguments"
  if data:
    return data
  data = "No Users found"
  return data

def properties_bedrooms_bathrooms(arguments):
  query = """SELECT Property.property_id
             FROM Property
             INNER JOIN InteriorFactsandFeatures ON Property.property_id = InteriorFactsandFeatures.property 
             WHERE InteriorFactsandFeatures.bedrooms = %s
              AND InteriorFactsandFeatures.bathroom = %s;"""
  if len(arguments) == 2:
    try:
      arguments[0] = int(arguments[0])
      arguments[1] = int(arguments[1])
      data = dbmodels.DataHandler("PropertyFull", query, arguments).data
    except ValueError:
      return "!properties-x-bedrooms-x-bathrooms  ERROR - Argument is not an Integer"
  elif len(arguments) < 2:
    return "!properties-x-bedrooms-x-bathrooms  ERROR - Argument Required"
  elif len(arguments) > 2:
    return "!properties-x-bedrooms-x-bathrooms  ERROR - Too Many Arguments"
  if data:
    return data
  data = "No Properties found"
  return data

def properties_same_user(arguments):
  query = """SELECT p.property_id, p.user 
             FROM Property p
             JOIN RegisteredUser u ON p.user = u.email
             WHERE u.email = (SELECT user FROM Property WHERE property_id = %s)
             AND p.property_id <> %s;"""
  if len(arguments) == 1:
    try:
      arguments[0] = int(arguments[0])
      arguments.append(arguments[0])
      data = dbmodels.DataHandler("PropertyQuick", query, arguments).data
    except ValueError:
      return "!property-same-user ERROR - Argument is not an Integer"
  elif len(arguments) == 0:
    return "!property-same-user ERROR - Argument Required"
  elif len(arguments) > 1:
    return "!property-same-user ERROR - Too Many Arguments"
  if data:
    return data
  data = "No Properties found"
  return data

def properties_same_zipcode(arguments):
  query = """SELECT p.property_id, p.user, l.address, l.state, l.city, l.zipcode
            FROM Property p
            JOIN Location l ON p.location = l.loc_id
            WHERE l.zipcode = (SELECT zipcode FROM Location WHERE loc_id = %s);"""
  if len(arguments) == 1:
    try:
      arguments[0] = int(arguments[0])
      data = dbmodels.DataHandler("PropertyQuick", query, arguments).data
    except ValueError:
      return "!property-same-zipcode ERROR - Argument is not an Integer"
  elif len(arguments) == 0:
    return "!property-same-zipcode ERROR - Argument Required"
  elif len(arguments) > 1:
    return "!property-same-zipcode ERROR - Too Many Arguments"
  if data:
    return data
  data = "!property-same-zipcode No Properties found"
  return data

def properties_same_state_dif_zipcode(arguments):
  query = """SELECT p.property_id, p.location, l.address, l.state, l.city, l.zipcode
             FROM Property p
             JOIN Location l ON p.location = l.loc_id
             WHERE l.state = (SELECT state FROM Location WHERE loc_id = %s)
              AND l.zipcode <> (SELECT zipcode FROM Location WHERE loc_id = %s);"""
  if len(arguments) == 1:
    try:
      arguments[0] = int(arguments[0])
      arguments.append(arguments[0])
      data = dbmodels.DataHandler("PropertyQuick", query, arguments).data
    except ValueError:
      return "!property-same-state-different-zipcode ERROR - Argument is not an Integer"
  elif len(arguments) == 0:
    return "!property-same-state-different-zipcode ERROR - Argument Required"
  elif len(arguments) > 1:
    return "!property-same-state-different-zipcode ERROR - Too Many Arguments"
  if data:
    return data
  data = "!property-same-state-different-zipcode No Properties found"
  return data

def properties_cheaper_same_city(arguments):
  query = """SELECT p2.property_id
             FROM Property p1
             JOIN Location l1 ON p1.location = l1.loc_id
             JOIN Location l2 ON l1.city = l2.city
             JOIN Property p2 ON l2.loc_id = p2.location
             LEFT JOIN HOAFinancials h ON p2.property_id = h.property
             WHERE p1.property_id = %s
              AND h.yrprice < (SELECT yrprice FROM HOAFinancials WHERE property = %s);"""
  if len(arguments) == 1:
    try:
      arguments[0] = int(arguments[0])
      arguments.append(arguments[0])
      data = dbmodels.DataHandler("PropertyQuick", query, arguments).data
    except ValueError:
      return "!property-cost-less-same-city ERROR - Argument is not an Integer"
  elif len(arguments) == 0:
    return "!property-cost-less-same-city ERROR - Argument Required"
  elif len(arguments) > 1:
    return "!property-cost-less-same-city ERROR - Too Many Arguments"
  if data:
    return data
  data = "!property-cost-less-same-city No Properties found"
  return data

def ecom_ads(arguments):
  query = """SELECT Advertisement.ad_id
             FROM Advertisement
             JOIN ExternalECommerceSites ON Advertisement.ecommercesite = ExternalECommerceSites.name
             WHERE ExternalECommerceSites.name = %s;"""
  if len(arguments) == 1:
    try:
      arguments = int(arguments[0])
      return "!ecommercesites-ads ERROR - Argument is an Integer"
    except ValueError:
      data = dbmodels.DataHandler("Advertisment", query, arguments).data
  elif len(arguments) == 0:
    return "!ecommercesites-ads ERROR - Argument Required"
  elif len(arguments) > 1:
    return "!ecommercesites-ads ERROR - Too Many Arguments"
  if data:
    return data
  data = "No Ads found"
  return data
  
def user_applications(arguments):
  query = """SELECT Application.app_id FROM `Application` JOIN `RegisteredUser` ON Application.user = RegisteredUser.email WHERE Application.user = %s AND Application.property = %s;"""
  if len(arguments) == 2:
    try:
      arguments[0] = int(arguments[0])
      arguments[1] = int(arguments[1])
      return "!user-x-applications ERROR - Argument is an Integer"
    except ValueError:
      data = dbmodels.DataHandler("Application", query, arguments).data
  elif len(arguments) < 2:
    return "!user-x-applications ERROR - Argument Required"
  elif len(arguments) > 2:
    return "!user-x-applications ERROR - Too Many Arguments"
  if data:
    return data
  data = "Application not found"
  return data

def applications_lastname(arguments):
  query = """SELECT Application.app_id
             FROM Application
             JOIN Account ON Application.user = Account.user
             WHERE Account.lastname = %s;"""
  if len(arguments) == 1:
    try:
      arguments = int(arguments[0])
      return "!applications-by-lastname ERROR - Argument is an Integer"
    except ValueError:
      data = dbmodels.DataHandler("Application", query, arguments).data
  elif len(arguments) == 0:
    return "!applications-by-lastname ERROR - Argument Required"
  elif len(arguments) > 1:
    return "!applications-by-lastname ERROR - Too Many Arguments"
  if data:
    return data
  data = "No Applications found"
  return data
