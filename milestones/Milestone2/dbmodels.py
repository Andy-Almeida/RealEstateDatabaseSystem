from database import Database

# Your code to model your objects to handle the data from your database goes here.

#queryHandler
#1. recieve the query and outputType
#2. Conduct the query
#3. Recieve the response from the database
#4. Check the response to see if it is just one or multiple outputs
#5. One -> Query the one item using the model, and return the model
#5. Mult-> Create an array of models and query and fill for each entry, Return the array of models

class DataHandler:
  def __init__(self, queryType, query, arguments = None):
    self.database = Database()
    self.queryType = queryType
    self.query = query
    self.arguments = arguments
    self.data = self.runQuery()

  def runQuery(self):
    dbDataArray = self.database.select(self.query, self.arguments)
    dbDataString = ""
    if self.queryType == "User":
      for row in dbDataArray:
        dbDataString += str(User(row['email']))
        dbDataString += "\n"

    elif self.queryType == "Application":
      for row in dbDataArray:
        dbDataString += str(Application(row['app_id']))
        dbDataString += "\n"

    elif self.queryType == "Advertisment":
      for row in dbDataArray:
        dbDataString += str(Advertisment(row['ad_id']))
        dbDataString += "\n"
        
    elif self.queryType == "Firm":
      for row in dbDataArray:
        dbDataString += str(Firm(row['firm_id']))
        dbDataString += "\n"

    elif self.queryType == "PropertyQuick":
      for row in dbDataArray:
        dbDataString += Property(row['property_id']).quickInfo()
        dbDataString += "\n"

    elif self.queryType == "PropertyFull":
      for row in dbDataArray:
        property = Property(row['property_id'])
        property.loadDetails()
        dbDataString += str(property)
        dbDataString += "\n"

    elif self.queryType == "EComSite":
      for row in dbDataArray:
        dbDataString += str(ECommerceSite(row['name']))
        dbDataString += "\n"
        
    return dbDataString

class User:
  def __init__(self, email):
    self.database = Database()
    self.email = email
    self.accountId = None
    self.profession = None
    self.firstName = None
    self.lastName = None
    self.zipcode = None
    self.phoneNumber = None
    self.profileId = None
    self.screenName = None
    self.load()

  def load(self):
    query = """SELECT RegisteredUser.email as Email, 
	                    Account.account_id as AccountId, 
                      Account.profession as Profession, 
                      Account.firstname as FirstName,
                      Account.lastname as LastName,
                      Account.zipcode as ZipCode,
                      Account.firm as FirmId,
                      Account.phonenumber as PhoneNumber,
                      Profile.profile_id as ProfileId,
                      Profile.screenname as ScreenName
               FROM RegisteredUser
               JOIN Account ON RegisteredUser.email = Account.user
               JOIN Profile ON RegisteredUser.email = Profile.user
               WHERE RegisteredUser.email = %s;"""
    arguments = (self.email)
    data = self.database.select(query, arguments)
    if data:
      data = data[0]
      self.accountId = data['AccountId']
      self.profession = data['Profession']
      self.firstName = data['FirstName']
      self.lastName = data['LastName']
      self.zipcode = data['ZipCode']
      self.phoneNumber = data['PhoneNumber']
      self.profileId = data['ProfileId']
      self.screenName = data['ScreenName']
  
  def __str__(self):
    string = f'__**RegisteredUser Email = {self.email}**__\n'
    string += f'**AccountId = {self.accountId}**\n'
    string += f'FirstName = {self.firstName}\n'
    string += f'LastName = {self.lastName}\n'
    string += f'Profession = {self.profession}\n'
    string += f'ZipCode = {self.zipcode}\n'
    string += f'PhoneNumber = {self.phoneNumber}\n'
    string += f'ProfileId = {self.profileId}\n'
    string += f'ScreenName = {self.screenName}\n'
    return string

class Property:
  def __init__(self, propertyId):
    self.database = Database()
    self.propertyId = propertyId
    self.user = None
    self.listed = None
    self.locationId = None
    self.state = None
    self.city = None
    self.zipcode = None
    self.address = None
    self.constructionDetails = {'Type':None,'ArchitectualStyle':None,'Subtype':None,'Materials':None,'Roof':None,'BuildCondition':None,'New':None,'YearBuilt':None}
    self.hoaFinancials = {'YearPrice':None,'MonthPrice':None,'PriceRangeHigh':None,'PriceRangeLow':None,'HOAFee':None,'Amenities':None,'Services':None,'AssociationName':None,'BuyerAgencyComp':None}
    self.interiorFactsAndFeatures = {'Bedrooms':None,'Bathrooms':None,'FullBathrooms':None,'HalfBathrooms':None,'Flooring':None,'Heating':None,'Cooling':None,'Appliances':None,'Parking':None,'Laundry':None,'Pets':None,'TotalStructureArea':None,'TotalLiveableArea':None}
    self.propertyFactsAndFeatures = {'Accessibility':None,'Levels':None,'Stories':None,'Viewdescription':None,'Lotfeatures':None,'Attatchedtoanother':None,'Specialcond':None}
    self.rooms = None
    self.utilitiesAndEnergyDetails = {'Info':None,'Sewage':None,'Utilities':None,'Energyefficient':None,'Security':None}
    self.loadQuick()

  def loadQuick(self):
    query = """SELECT Property.property_id as PropertyID,
		                  Property.user as User,
                      Property.listed as Listed,
                      Property.location as LocationID,
		                  Location.state as State,
                      Location.city as City,
                      Location.zipcode as Zipcode,
                      Location.address as Address
               FROM Property
               JOIN Location ON Property.location = Location.loc_id
               WHERE Property.property_id = %s;"""
    arguments = (self.propertyId)
    data = self.database.select(query, arguments)
    if data:
      data = data[0]
      self.user = data['User']
      self.listed = data['Listed']
      self.locationId = data['LocationID']
      self.state = data['State']
      self.city = data['City']
      self.zipcode = data['Zipcode']
      self.address = data['Address']

  def loadDetails(self):
    query = """SELECT ConstructionDetails.type as Type,
                		  ConstructionDetails.archstyle as ArchitectualStyle,
                		  ConstructionDetails.subtype as Subtype,
                		  ConstructionDetails.materials as Materials,
                		  ConstructionDetails.roof as Roof,
                		  ConstructionDetails.condition as BuildCondition,
                		  ConstructionDetails.new as New,
                		  ConstructionDetails.yearbuilt as YearBuilt,
                      HOAFinancials.yrprice as YearPrice,
                		  HOAFinancials.monthprice as MonthPrice,
                		  HOAFinancials.pricerangehigh as PriceRangeHigh,
                		  HOAFinancials.pricerangelow as PriceRangeLow,
                		  HOAFinancials.hoafee as HOAFee,
                		  HOAFinancials.amenities as Amenities,
                		  HOAFinancials.services as Services,
                		  HOAFinancials.associationname as AssociationName,
                		  HOAFinancials.buyeragencycomp as BuyerAgencyComp,
                      InteriorFactsandFeatures.bedrooms as Bedrooms,
                		  InteriorFactsandFeatures.bathroom as Bathrooms,
                		  InteriorFactsandFeatures.fullbathrooms as FullBathrooms,
                		  InteriorFactsandFeatures.halfbathrooms as HalfBathrooms,
                		  InteriorFactsandFeatures.flooring as Flooring,
                		  InteriorFactsandFeatures.heating as Heating,
                		  InteriorFactsandFeatures.cooling as Cooling,
                		  InteriorFactsandFeatures.appliances as Appliances,
                		  InteriorFactsandFeatures.parking as Parking,
                		  InteriorFactsandFeatures.laundry as Laundry,
                		  InteriorFactsandFeatures.pets as Pets,
                		  InteriorFactsandFeatures.totalstructurearea as TotalStructureArea,
                		  InteriorFactsandFeatures.totallivablearea as TotalLiveableArea,
                      PropertyFactsandFeatures.accessibility as Accessibility,
                		  PropertyFactsandFeatures.levels as Levels,
                		  PropertyFactsandFeatures.stories as Stories,
                		  PropertyFactsandFeatures.viewdescription as Viewdescription,
                		  PropertyFactsandFeatures.lotfeatures as Lotfeatures,
                		  PropertyFactsandFeatures.attatchedtoanother as Attatchedtoanother,
                		  PropertyFactsandFeatures.specialcond as Specialcond,
                      UtilitiesandEnergyDetails.info as Info,
                		  UtilitiesandEnergyDetails.sewage as Sewage,
                		  UtilitiesandEnergyDetails.utilities as Utilities,
                		  UtilitiesandEnergyDetails.energyefficient as Energyefficient,
                		  UtilitiesandEnergyDetails.security as Security
               FROM Property
               LEFT JOIN ConstructionDetails ON Property.property_id = ConstructionDetails.property
               LEFT JOIN HOAFinancials ON Property.property_id = HOAFinancials.property
               LEFT JOIN InteriorFactsandFeatures ON Property.property_id = InteriorFactsandFeatures.property
               LEFT JOIN PropertyFactsandFeatures ON Property.property_id = PropertyFactsandFeatures.property
               LEFT JOIN UtilitiesandEnergyDetails ON Property.property_id = UtilitiesandEnergyDetails.property
               WHERE Property.property_id = %s;"""
    arguments = (self.propertyId)
    data = self.database.select(query, arguments)
    if data:
      self.constructionDetails = {'Type':data[0]['Type'],'ArchitectualStyle':data[0]['ArchitectualStyle'],'Subtype':data[0]['Subtype'],'Materials':data[0]['Materials'],'Roof':data[0]['Roof'],'BuildCondition':data[0]['BuildCondition'],'New':data[0]['New'],'YearBuilt':data[0]['YearBuilt']}
      self.hoaFinancials = {'YearPrice':data[0]['YearPrice'],'MonthPrice':data[0]['MonthPrice'],'PriceRangeHigh':data[0]['PriceRangeHigh'],'PriceRangeLow':data[0]['PriceRangeLow'],'HOAFee':data[0]['HOAFee'],'Amenities':data[0]['Amenities'],'Services':data[0]['Services'],'AssociationName':data[0]['AssociationName'],'BuyerAgencyComp':data[0]['BuyerAgencyComp']}
      self.interiorFactsAndFeatures = {'Bedrooms':data[0]['Bedrooms'],'Bathrooms':data[0]['Bathrooms'],'FullBathrooms':data[0]['FullBathrooms'],'HalfBathrooms':data[0]['HalfBathrooms'],'Flooring':data[0]['Flooring'],'Heating':data[0]['Heating'],'Cooling':data[0]['Cooling'],'Appliances':data[0]['Appliances'],'Parking':data[0]['Parking'],'Laundry':data[0]['Laundry'],'Pets':data[0]['Pets'],'TotalStructureArea':data[0]['TotalStructureArea'],'TotalLiveableArea':data[0]['TotalLiveableArea']}
      self.propertyFactsAndFeatures = {'Accessibility':data[0]['Accessibility'],'Levels':data[0]['Levels'],'Stories':data[0]['Stories'],'Viewdescription':data[0]['Viewdescription'],'Lotfeatures':data[0]['Lotfeatures'],'Attatchedtoanother':data[0]['Attatchedtoanother'],'Specialcond':data[0]['Specialcond']}
      self.utilitiesAndEnergyDetails = {'Info':data[0]['Info'],'Sewage':data[0]['Sewage'],'Utilities':data[0]['Utilities'],'Energyefficient':data[0]['Energyefficient'],'Security':data[0]['Security']}

  def quickInfo(self):
    string = f'__**Property ID = {self.propertyId}**__\n'
    string += f'**User = {self.user}**\n'
    string += f'Listed = {self.listed}\n'
    string += f'Location ID = {self.locationId}\n'
    string += f'State = {self.state}\n'
    string += f'City = {self.city}\n'
    string += f'Zipcode = {self.zipcode}\n'
    string += f'Address = {self.address}\n'
    return string

  def __str__(self):
    string = f'__**Property ID = {self.propertyId}**__\n'
    string += f'**User = {self.user}**\n'
    string += f'Listed = {self.listed}\n'
    string += f'Location ID = {self.locationId}\n'
    string += f'State = {self.state}\n'
    string += f'City = {self.city}\n'
    string += f'Zipcode = {self.zipcode}\n'
    string += f'Address = {self.address}\n'
    string += '__ConstructionDetails__\n'
    string += f'Type = {self.constructionDetails["Type"]}\n'
    string += f'Architectual Style = {self.constructionDetails["ArchitectualStyle"]}\n'
    string += f'Subtype = {self.constructionDetails["Subtype"]}\n'
    string += f'Materials = {self.constructionDetails["Materials"]}\n'
    string += f'Roof = {self.constructionDetails["Roof"]}\n'
    string += f'BuildCondition = {self.constructionDetails["BuildCondition"]}\n'
    string += f'New = {self.constructionDetails["New"]}\n'
    string += f'YearBuilt = {self.constructionDetails["YearBuilt"]}\n'
    string += '__HOA/Financials__\n'
    string += f'YearPrice = {self.hoaFinancials["YearPrice"]}\n'
    string += f'MonthPrice = {self.hoaFinancials["MonthPrice"]}\n'
    string += f'PriceRangeHigh = {self.hoaFinancials["PriceRangeHigh"]}\n'
    string += f'PriceRangeLow = {self.hoaFinancials["PriceRangeLow"]}\n'
    string += f'HOAFee = {self.hoaFinancials["HOAFee"]}\n'
    string += f'Amenities = {self.hoaFinancials["Amenities"]}\n'
    string += f'Services = {self.hoaFinancials["Services"]}\n'
    string += f'AssociationName = {self.hoaFinancials["AssociationName"]}\n'
    string += f'BuyerAgencyComp = {self.hoaFinancials["BuyerAgencyComp"]}\n'
    string += '__InteriorFactsandFeatures__\n'
    string += f'Bedrooms = {self.interiorFactsAndFeatures["Bedrooms"]}\n'
    string += f'Bathrooms = {self.interiorFactsAndFeatures["Bathrooms"]}\n'
    string += f'FullBathrooms = {self.interiorFactsAndFeatures["FullBathrooms"]}\n'
    string += f'HalfBathrooms = {self.interiorFactsAndFeatures["HalfBathrooms"]}\n'
    string += f'Flooring = {self.interiorFactsAndFeatures["Flooring"]}\n'
    string += f'Heating = {self.interiorFactsAndFeatures["Heating"]}\n'
    string += f'Cooling = {self.interiorFactsAndFeatures["Cooling"]}\n'
    string += f'Appliances = {self.interiorFactsAndFeatures["Appliances"]}\n'
    string += f'Parking = {self.interiorFactsAndFeatures["Parking"]}\n'
    string += f'Laundry = {self.interiorFactsAndFeatures["Laundry"]}\n'
    string += f'Pets = {self.interiorFactsAndFeatures["Pets"]}\n'
    string += f'TotalStructureArea = {self.interiorFactsAndFeatures["TotalStructureArea"]}\n'
    string += f'TotalLiveableArea = {self.interiorFactsAndFeatures["TotalLiveableArea"]}\n'
    string += '__PropertyFactsandFeatures__\n'
    string += f'Accessibility = {self.propertyFactsAndFeatures["Accessibility"]}\n'
    string += f'Levels = {self.propertyFactsAndFeatures["Levels"]}\n'
    string += f'Stories = {self.propertyFactsAndFeatures["Stories"]}\n'
    string += f'ViewDescription = {self.propertyFactsAndFeatures["Viewdescription"]}\n'
    string += f'LotFeatures = {self.propertyFactsAndFeatures["Lotfeatures"]}\n'
    string += f'AttatchedtoAnother = {self.propertyFactsAndFeatures["Attatchedtoanother"]}\n'
    string += f'SpecialConditions = {self.propertyFactsAndFeatures["Specialcond"]}\n'
    string += '__UtilitiesandEnergyDetails__\n'
    string += f'Info = {self.utilitiesAndEnergyDetails["Info"]}\n'
    string += f'Sewage = {self.utilitiesAndEnergyDetails["Sewage"]}\n'
    string += f'Utilities = {self.utilitiesAndEnergyDetails["Utilities"]}\n'
    string += f'Energyefficient = {self.utilitiesAndEnergyDetails["Energyefficient"]}\n'
    string += f'Security = {self.utilitiesAndEnergyDetails["Security"]}\n'
    return string
    
class Application:
  def __init__(self, app_id):
    self.database = Database()
    self.app_id = app_id
    self.property = None
    self.user = None
    self.message = None
    self.load()
    
  def load(self):
    query = """SELECT Application.app_id as ID, 
	                    Application.property as PropertyId, 
                      Application.user as Email, 
                      Application.message as Message
               FROM Application
               WHERE Application.app_id = %s;"""
    arguments = (self.app_id)
    data = self.database.select(query, arguments)
    if data:
      data = data[0]
      self.property = data['PropertyId']
      self.user = data['Email']
      self.message = data['Message']

  def __str__(self):
    string = f'__**Application ID = {self.app_id}**__\n'
    string += f'Property = {self.property}\n'
    string += f'User = {self.user}\n'
    string += f'message = *{self.message}*\n'
    return string

class Advertisment:
  def __init__(self, ad_id):
    self.database = Database()
    self.ad_id = ad_id
    self.property = None
    self.ecommercesite = None
    self.message = None
    self.load()
    
  def load(self):
    query = """SELECT Advertisement.property as PropertyId, 
                      Advertisement.ecommercesite as EComSite,
                      Advertisement.message as Message 
               FROM Advertisement
               WHERE Advertisement.ad_id = %s;"""
    arguments = (self.ad_id)
    data = self.database.select(query, arguments)
    if data:
      data = data[0]
      self.property = data['PropertyId']
      self.user = data['EComSite']
      self.message = data['Message']

  def __str__(self):
    string = f'__**Advertisement ID = {self.ad_id}**__\n'
    string += f'Property = {self.property}\n'
    string += f'ECommerceSite = {self.ecommercesite}\n'
    string += f'message = *{self.message}*\n'
    return string

class Firm:
  def __init__(self, firm_id):
    self.database = Database()
    self.firm_id = firm_id
    self.name = None
    self.locationId = None
    self.state = None
    self.city = None
    self.zipcode = None
    self.address = None
    self.load()
    
  def load(self):
    query = """SELECT Firm.firm_id as FirmID,
		                  Firm.name as Name,
                      Firm.location as LocationID,
                      Location.state as State,
                      Location.city as City,
                      Location.zipcode as Zipcode,
                      Location.address as Address
               FROM Firm
               JOIN Location ON Firm.location = Location.loc_id
               WHERE Firm.firm_id = %s;"""
    arguments = (self.firm_id)
    data = self.database.select(query, arguments)
    if data:
      data = data[0]
      self.firm_id = data['FirmID']
      self.name = data['Name']
      self.locationId = data['LocationID']
      self.state = data['State']
      self.city = data['City']
      self.zipcode = data['Zipcode']
      self.address = data['Address']
  
  def __str__(self):
    string = f'__**Firm ID = {self.firm_id}**__\n'
    string += f'Name = {self.name}\n'
    string += f'Location ID = {self.locationId}\n'
    string += f'State = {self.state}\n'
    string += f'City = {self.city}\n'
    string += f'Zipcode = {self.zipcode}\n'
    string += f'Address = {self.address}\n'
    return string

class ECommerceSite:
  def __init__(self, name):
    self.database = Database()
    self.name = name
    self.webLink = None
    self.load()
    
  def load(self):
    query = """SELECT `ExternalECommerceSites`.`name`,
                      `ExternalECommerceSites`.`websitelink`
               FROM `RealEstateManagementDatabaseSystem`.`ExternalECommerceSites`
               WHERE `ExternalECommerceSites`.`name` = %s;"""
    arguments = (self.name)
    data = self.database.select(query, arguments)
    if data:
      data = data[0]
      self.name = data['name']
      self.webLink = data['websitelink']
  
  def __str__(self):
    string = f'__**Name = {self.name}**__\n'
    string += f'Website Link = {self.webLink}\n'
    return string