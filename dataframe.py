import pandas as pd
screen_time =[2,4,6]
sleep_hours = [3,7,8]
stu_name =["karthik","vivek","raju"]
dict1 = {
    "screen_time":screen_time,
     "sleep_hours":sleep_hours,
     "stu_name":stu_name
    }
print(dict1)
df = pd.DataFrame(dict1)
print(df)

import pandas as pd
name =["a","b","c"]
id = [1,2,3]
phone = [123,124,145]
dict1={
    "Name":name,
    "id": id,
    "phone_number":phone
    }
print(dict1)
df = pd.DataFrame(dict1)
print(df)
