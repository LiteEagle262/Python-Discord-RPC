from pypresence import Presence

def rpc():
  client_id = '850115504878256152' #your client id here
  RPC = Presence(client_id)
  RPC.connect()
  RPC.update(
      large_image="logo", #your image here that you make on your dev discord aplication
      large_text="Eagle Customs",
      state="dsc.gg/EagleCustoms",
      details="Auto Advertising", 
      buttons=[{"label": "Join Our Discord", "url": "https://discord.gg/EuAzC2pWnn"}] #button example
  )
  
rpc()

