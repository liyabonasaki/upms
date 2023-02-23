from upms.members.models import Members

members = Members.objects.all()

member1 = members(title = 'Mr', first_name = 'liyabona', last_name = 'saki'    , position = 'Developer', phone = '', mobile = '0783508357'   , email1 = 'liyabonasaki@gmail.com')
member2 = Members(title = 'Mr', first_name = 'Bongisa' , last_name = 'Mpahleni', position = 'Developer', phone = '', mobile = '07835596884'  , email1 = 'bongisampahleni@gmail.com')
member3 = Members(title = 'Ms', first_name = 'emihle'  , last_name = 'menzo'   , position = 'Developer', phone = '', mobile = '0699856624'   , email1 = 'emihlemenzo@gmail.com')
member4 = Members(title = 'Ms', first_name = 'asiphiwe', last_name = 'hanjiwe' , position = 'Developer', phone = '', mobile = '0699858357'   , email1 = 'asiphiwehanjiwe@gmail.com')
member5 = Members(title = 'Mr', first_name = 'joe'     , last_name = 'doe'     , position = 'Developer', phone = '', mobile = '0699583364458', email1 = 'joedoe@gmail.com')
member6 = Members(title = 'Mr', first_name = 'linus'   , last_name = 'tovalds' , position = 'Developer', phone = '', mobile = '03683508357'  , email1 = 'linustovalds@gmail.com')

member_list = [member2, member3, member4, member5, member6]

for i in member_list:
    i.save()

# returning the data from the db
members.objects.all().values()
