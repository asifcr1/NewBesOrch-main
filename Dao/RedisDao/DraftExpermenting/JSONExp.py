import redis
from DataModels.SSGModels import SSGSession,SSGVenue
from redis.commands.search.field import TextField, NumericField, TagField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
r = redis.Redis(host='redis-16395.c78.eu-west-1-2.ec2.cloud.redislabs.com', port=16395, password="7B8TRG2SbyenKFc5O7j97cnpbZGPKvil")




obj = [SSGSession(id='Fuchun 019-41618-S1', startDate='20190814', endDate='20190814', startTime='15:30', endTime='17:30',
                  modeOfTraining='1', venue=SSGVenue(block='112A', street='Street ABC', floor='15', unit='001', building='Building ABC',
                                                     postalCode='123455', room='24', wheelChairAccess=True), attendanceTaken=False, deleted=False),
       SSGSession(id='Fuchun 019-41618-S1', startDate='20190814', endDate='20190814', startTime='15:30', endTime='17:30',
                  modeOfTraining='1',
                  venue=SSGVenue(block='112A', street='Street ABC', floor='18', unit='001', building='Building ABC',
                                 postalCode='123455', room='24', wheelChairAccess=True), attendanceTaken=False, deleted=False)
       ]

dictionary_of_list = {}
obj2 = [sess.dict() for sess in obj]
# for item in obj2:
#     name = item['id']
#     dictionary_of_list[name] = item
# print(dictionary_of_list)
r.json().set("mykey", "$", obj2, xx=True)
# schema = (TextField("$.mykey.id", as_name="id"))
# r.ft().create_index(schema, definition=IndexDefinition(prefix=["mykey"], index_type=IndexType.JSON))
#
# print(r.json().get("mykey" , '.'))

# print(obj2)

