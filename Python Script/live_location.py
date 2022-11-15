import wiotp.sdk.device
import time
import random
myConfig = {
  "identity": {
    "orgId": "nybqe1",
    "typeId": "Jeeva_Yovan",
    "deviceId": "Watson"
  },
  "auth": {
    "token": "12345678"
  }
}

def myCommandCallback(cmd):
  print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
  m=cmd.data['command']

def pub(data):
  client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
  print("Published data Successfully:%s",myData)

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
  myData={'name':'Train1','lat':10.184363,'lon': 77.922702}
  pub(myData)
  time.sleep(3)
  myData={'name':'Train1','lat':10.213225,'lon': 77.898765}
  pub(myData)
  time.sleep(3)
  myData={'name':'Train1','lat':10.285035,'lon': 77.921569}
  pub(myData)
  time.sleep(3)
  myData={'name':'Train1','lat':10.343369,'lon': 77.958056}
  pub(myData)
  time.sleep(3)
  myData={'name':'Train1','lat':10.356829,'lon': 77.980861}
  pub(myData)
  time.sleep(3)
  client.commandCallback = myCommandCallback
client.disconnect()
