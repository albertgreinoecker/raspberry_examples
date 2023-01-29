import json

data1 = {}
data1['key1'] = 'value1'
data1['key2'] = 'value2'
j1 = json.dumps(data1)
print(j1)
#ergibt: {"key1": "value1", "key2": "value2"}


data2 = {}
sub1 = {}

sub1['k1'] = 'v1'
data2['simple'] = 'a value'
data2['sub'] = sub1;

j2 = json.dumps(data2, indent=3)
print(j2)
#ergibt
'''
{
   "simple": "a value",
   "sub": {
      "k1": "v1"
   }
}
'''

# Dieser JSON-String wird so in eine Datei geschrieben
with open("data/test.json", "w") as outfile:
    outfile.write(j2)



