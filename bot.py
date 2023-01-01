import vk_api
import config as c
from vk_api.longpoll import VkLongPoll

# Define a function to send a message to a user
def send_message(user_id, message):
  vk.method("messages.send", {"user_id": user_id, "message": message})

# Enter your VK API access token here
ACCESS_TOKEN = c.my_token

# Initialize the VK API client
vk = vk_api.VkApi(token=ACCESS_TOKEN)

# Initialize the VK Long Poll client
longpoll = VkLongPoll(vk)

# Main loop
for event in longpoll.listen():
  # Check if the event is a new message
  if event.type == vk_api.longpoll.VkEventType.MESSAGE_NEW:
    # Get the ID of the user who sent the message
    user_id = event.user_id
    
    # Get the message text
    message_text = event.text
    
    # Send a reply to the user
    if message_text == 'Hi':
      send_message(user_id, "Hello! I'm a VK user bot, and I'll automatically reply to your messages.")
      
      
#writen with love by Agent-502#
