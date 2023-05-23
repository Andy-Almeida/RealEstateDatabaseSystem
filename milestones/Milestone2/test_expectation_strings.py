TEST_EXP_USERS = """__**RegisteredUser Email = benito@gmail.com**__
**AccountId = 3**
FirstName = Benito
LastName = Slim
Profession = Renter
ZipCode = 91123
PhoneNumber = 9494177744
ProfileId = 3
ScreenName = BadBunny

__**RegisteredUser Email = deaduser@gmail.com**__
**AccountId = 5**
FirstName = None
LastName = None
Profession = None
ZipCode = None
PhoneNumber = None
ProfileId = 5
ScreenName = None

__**RegisteredUser Email = maria@gmail.com**__
**AccountId = 4**
FirstName = Maria
LastName = Palacios
Profession = None
ZipCode = 92606
PhoneNumber = 9491919191
ProfileId = 4
ScreenName = bokitaspintadas

__**RegisteredUser Email = poncho@gmail.com**__
**AccountId = 1**
FirstName = Poncho
LastName = Slim
Profession = None
ZipCode = 94112
PhoneNumber = 9498366192
ProfileId = 1
ScreenName = Poncho

__**RegisteredUser Email = reah@gmail.com**__
**AccountId = 2**
FirstName = Reah
LastName = Mehta
Profession = Private
ZipCode = 92606
PhoneNumber = 9494444444
ProfileId = 2
ScreenName = reahm

"""

TEST_EXP_USER = """__**RegisteredUser Email = poncho@gmail.com**__
**AccountId = 1**
FirstName = Poncho
LastName = Slim
Profession = None
ZipCode = 94112
PhoneNumber = 9498366192
ProfileId = 1
ScreenName = Poncho

"""

TEST_EXP_PROPERTIES = """__**Property ID = 1**__
**User = poncho@gmail.com**
Listed = 1
Location ID = 1
State = California
City = Irvine
Zipcode = 92606
Address = 667 Santa Maria

__**Property ID = 2**__
**User = reah@gmail.com**
Listed = 0
Location ID = 2
State = California
City = San Francisco
Zipcode = 94112
Address = 170 Lobos

__**Property ID = 3**__
**User = benito@gmail.com**
Listed = 1
Location ID = 3
State = New York
City = New York
Zipcode = 10007
Address = 10 Murray St

__**Property ID = 4**__
**User = benito@gmail.com**
Listed = 1
Location ID = 7
State = California
City = Bakersfield
Zipcode = 93304
Address = 15590 Heitor Dr.

__**Property ID = 5**__
**User = poncho@gmail.com**
Listed = 1
Location ID = 8
State = California
City = Fresno
Zipcode = 94134
Address = 41 Waller St

__**Property ID = 6**__
**User = poncho@gmail.com**
Listed = 1
Location ID = 9
State = California
City = Irvine
Zipcode = 92606
Address = 12 Tortoise Shell

"""

TEST_EXP_PROPERTY = """__**Property ID = 1**__
**User = poncho@gmail.com**
Listed = 1
Location ID = 1
State = California
City = Irvine
Zipcode = 92606
Address = 667 Santa Maria
__ConstructionDetails__
Type = House
Architectual Style = Rustic
Subtype = None
Materials = Brick and Wood
Roof = Mansard
BuildCondition = None
New = 0
YearBuilt = 1994
__HOA/Financials__
YearPrice = 1300000
MonthPrice = 8399
PriceRangeHigh = 1800000
PriceRangeLow = 1300000
HOAFee = None
Amenities = No Amenities
Services = Trash collection comes by weekly
AssociationName = None
BuyerAgencyComp = 3
__InteriorFactsandFeatures__
Bedrooms = 3
Bathrooms = 1
FullBathrooms = 1
HalfBathrooms = 0
Flooring = Wooden
Heating = Air Conditioning
Cooling = Air Conditioning
Appliances = Full Kitchen
Parking = Driveway parking 2
Laundry = Washer and Dry in the Garage
Pets = Allowed
TotalStructureArea = 1500
TotalLiveableArea = 1399
__PropertyFactsandFeatures__
Accessibility = None
Levels = Two
Stories = 2
ViewDescription = Forest
LotFeatures = Large Backyard
AttatchedtoAnother = 0
SpecialConditions = None
__UtilitiesandEnergyDetails__
Info = Updated Recently
Sewage = Public Sewer
Utilities = Natural Gas Connected
Energyefficient = Not
Security = Gated

"""

TEST_EXP_APPLICATIONS = """__**Application ID = 1**__
Property = 1
User = None
message = *Hello, my name is Charlie.*

__**Application ID = 2**__
Property = 1
User = maria@gmail.com
message = *Yo vi tu apartamento y quiero saber mas.*

__**Application ID = 3**__
Property = 2
User = maria@gmail.com
message = *I would like to learn more, Thank you*

"""

TEST_EXP_FIRMS = """__**Firm ID = 1**__
Name = Ponchos Realtor
Location ID = 4
State = Washington
City = DC
Zipcode = 20004
Address = 1101 Pennsylvania Ave NW

__**Firm ID = 2**__
Name = Innova
Location ID = 5
State = Oregon
City = Portland
Zipcode = 97201
Address = 1526 SW 10th Ave

__**Firm ID = 3**__
Name = Benito Inc.
Location ID = 6
State = California
City = Bakersfield
Zipcode = 93304
Address = 700 Oak St

"""

TEST_EXP_USERS_NO_ACCOUNT = """__**RegisteredUser Email = deaduser@gmail.com**__
**AccountId = 5**
FirstName = None
LastName = None
Profession = None
ZipCode = None
PhoneNumber = None
ProfileId = 5
ScreenName = None

"""
TEST_EXP_USER_SCREENNAME = """__**RegisteredUser Email = poncho@gmail.com**__
**AccountId = 1**
FirstName = Poncho
LastName = Slim
Profession = None
ZipCode = 94112
PhoneNumber = 9498366192
ProfileId = 1
ScreenName = Poncho

"""

TEST_EXP_ECOMSITES = """__**Name = Craigslist**__
Website Link = https://post.craigslist.org/

__**Name = Facebook Marketplace**__
Website Link = https://www.facebook.com/marketplace/create

__**Name = OfferUp**__
Website Link = https://offerup.com/

"""

