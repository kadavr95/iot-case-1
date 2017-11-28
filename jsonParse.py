import json

while 1:
    data = input()
    data_d = json.dumps(data)
    data_l = json.loads(data_d)
    temp = data_l['data']['temperature']
    humi = data_l['data']['humidity']
    print("Temperature=" + str(temp) + "C; Humidity=" + str(humi))
    if temp > 30:
        print("Temperature is too high!")
    if temp < 20:
        print("Temperature is too low")
    if humi > 50:
        print("Humidity is too high")
    if temp > 100 or temp < -100:
        print("OMAE WA MOU SHINDEIRU")