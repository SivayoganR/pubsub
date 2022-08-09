import json

attributes={'name':'sivayogan','mail_id':'sivayogan@ngpwebsmmart.com','fromEmail':'Northern Gas and Power <trading@ngpltd.co.uk>','domain':'domain','html':'html','pdf':'pdf'}
data=json.dumps(attributes).encode("utf-8")
print('data',data)
# print(data['name'])
decode=data.decode("utf-8")
decode_string=json.loads(decode)
print(decode_string['name'])
print('decode',decode)