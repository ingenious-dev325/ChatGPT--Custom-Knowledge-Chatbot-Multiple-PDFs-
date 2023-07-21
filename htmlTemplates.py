css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://img.freepik.com/free-vector/robot-android-realistic-3d-composition-with-artificial-support-agent-cybernetic-anthropomorphous-machine-with-feminine-apperance_1284-28638.jpg?size=626&ext=jpg&ga=GA1.1.1314113236.1689581092&semt=ais">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://img.freepik.com/free-psd/3d-illustration-person-with-sunglasses_23-2149436188.jpg?w=740&t=st=1689581156~exp=1689581756~hmac=dd31f64976d22b79e208ad69d2d232a4f38343d2ebf96b7ea2f61c53e9310521">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''