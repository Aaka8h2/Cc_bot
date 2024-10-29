import telebot, json, requests, re, random, faker
from faker import Faker
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

fake = Faker()

admin_id = '5983253591'  # اي دي بتاعك هنا
bot = telebot.TeleBot("7699407451:AAHhp54nzRj0j8ZJBDIvUMnldskQpOtPdAI")# توكن بتاعك هنا
#AddUser
def load_users():
    try:
        with open('users.json', 'r') as f:
            users = json.load(f)
    except FileNotFoundError:
        users = {}
        with open('users.json', 'w') as f:
            json.dump(users, f)
    return users
users = load_users()
def add_user(user_id):
    users[user_id] = True
    with open('users.json', 'w') as f:
        json.dump(users, f)
def remove_user(user_id):
    if user_id in users:
        del users[user_id]
        with open('users.json', 'w') as f:
            json.dump(users, f)
@bot.message_handler(commands=["adduser"])
@bot.message_handler(func=lambda m: m.text.startswith('.adduser'))
def adduser(message):
    if str(message.chat.id) == admin_id:
        command_parts = message.text.split()
        if len(command_parts) < 2:
            bot.reply_to(message, "Sorry, this command requires a user_id.")
        else:
            user_id = command_parts[1]
            add_user(user_id)
            bot.reply_to(message, f"User {user_id} added")
    else:
        bot.reply_to(message, "Sorry, you do not have permission to use this command.")
@bot.message_handler(commands=["removeuser"])
@bot.message_handler(func=lambda m: m.text.startswith('.removeuser'))
def removeuser(message):
    if str(message.chat.id) == admin_id:
        command_parts = message.text.split()
        if len(command_parts) < 2:
            bot.reply_to(message, "Sorry, this command requires a user_id.")
        else:
            user_id = command_parts[1]
            remove_user(user_id)
            bot.reply_to(message, f"User {user_id} removed")
    else:
        bot.reply_to(message, "Sorry, you do not have permission to use this command.")
#Applicable Restriction Here
""" if str(message.chat.id) not in users.keys():
    bot.reply_to(message, "You Cannot Use this Bot Please Contact Owner To Gain Access")
    return """
#
#AddUser Ends
#BotFace
button_pages_lite = {
    '𝔸𝕌𝕋ℍ 𝔾𝔸𝕋𝔼𝕊': [
        """
------------------------
𝐁𝐑𝐀𝐈𝐍𝐓𝐑𝐄𝐄 𝐀𝐔𝐓𝐇 /bauth CC|MM|YY|CVC
𝐒𝐓𝐀𝐓𝐔𝐒 𝐎𝐅𝐅 ❌
------------------------
𝐒𝐓𝐑𝐈𝐏𝐄 𝐀𝐔𝐓𝐇 /sauth CC|MM|YY|CVC
𝐒𝐓𝐀𝐓𝐔𝐒 𝐎𝐅𝐅 ❌
------------------------
𝐒𝐇𝐎𝐏𝐈𝐅𝐘 𝐀𝐔𝐓𝐇 /shpauth CC|MM|YY|CVC
𝐒𝐓𝐀𝐓𝐔𝐒 𝐎𝐅𝐅 ❌
------------------------
"""
    ],
    'ℂℍ𝔸ℝ𝔾𝔼 𝔾𝔸𝕋𝔼𝕊': [
        """
------------------------
𝐁𝐑𝐀𝐈𝐍𝐓𝐑𝐄𝐄 𝐂𝐇𝐀𝐑𝐆𝐄 /bchk CC|MM|YY|CVC
𝐒𝐓𝐀𝐓𝐔𝐒 𝐎𝐅𝐅 ❌
------------------------
𝐒𝐓𝐑𝐈𝐏𝐄 𝐂𝐇𝐀𝐑𝐆𝐄 /schk CC|MM|YY|CVC
𝐒𝐓𝐀𝐓𝐔𝐒 𝐎𝐅𝐅 ❌
------------------------
𝐒𝐇𝐎𝐏𝐈𝐅𝐘 𝐂𝐇𝐀𝐑𝐆𝐄 /shp CC|MM|YY|CVC
𝐒𝐓𝐀𝐓𝐔𝐒 𝐎𝐅𝐅 ❌
------------------------
"""
    ],
    '𝕋𝕆𝕆𝕃𝕊': [
        """
------------------------
𝐂𝐂 𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐄 /gen CC|MM|YY|CVC
𝐒𝐓𝐀𝐓𝐔𝐒 𝐎𝐍 ✅
------------------------
𝐁𝐈𝐍 𝐈𝐍𝐅𝐎 /bin 4xxxxx
𝐒𝐓𝐀𝐓𝐔𝐒 𝐎𝐍 ✅
------------------------
𝐕𝐁𝐕 𝐈𝐍𝐅𝐎 /vbv CC|MM|YY|CVC
𝐒𝐓𝐀𝐓𝐔𝐒 𝐎𝐅𝐅 ❌
------------------------
𝐏𝐑𝐎𝐗𝐘 𝐒𝐂𝐑𝐀𝐏 /px
𝐒𝐓𝐀𝐓𝐔𝐒 𝐎𝐍 ✅
------------------------
𝐒𝐓𝐑𝐈𝐏𝐄 𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐎𝐑 /skgen (Max 20)
𝐒𝐓𝐀𝐓𝐔𝐒 𝐎𝐍 ✅
------------------------
"""
    ]
}
user_page = {}
user_message_content = {}
main_message_id = None
@bot.message_handler(commands=['start'])
@bot.message_handler(func=lambda m: m.text.startswith('.start'))
def send_video_with_buttons(message):
    global main_message_id
    try:
        bot.send_message(message.chat.id, """
bot by @aaka8h""")
        keyboard = generate_keyboard(message.chat.id)
        sent_message = bot.send_photo(message.chat.id, 'https://t.me/hzisnkkx/29', reply_markup=keyboard)
        user_id = message.chat.id
        user_message_content[user_id] = sent_message.caption
        main_message_id = sent_message.message_id
        user_page[user_id] = {}
        for button_id in button_pages_lite:
            user_page[user_id][button_id] = 1
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {str(e)}")
def generate_keyboard(user_id, hide_buttons=False):
    keyboard = InlineKeyboardMarkup(row_width=2)
    current_button = None
    if hide_buttons:
        current_button = user_page.get(user_id, {}).get('current_button')
        if current_button:
            page_content = button_pages_lite.get(current_button, [])[0]
            keyboard.row()
            keyboard.add(InlineKeyboardButton("ℍ𝕆𝕄𝔼", callback_data='home'))
    else:
        button_ids = list(button_pages_lite.keys())
        for i in range(0, len(button_ids), 2):
            button1_id = button_ids[i]
            button1_text = button1_id
            callback_data1 = f'{button1_id}_1'
            button1 = InlineKeyboardButton(button1_text, callback_data=callback_data1)
            if i + 1 < len(button_ids):
                button2_id = button_ids[i + 1]
                button2_text = button2_id
                callback_data2 = f'{button2_id}_1'
                button2 = InlineKeyboardButton(button2_text, callback_data=callback_data2)
                keyboard.row(button1, button2)
            else:
                keyboard.add(button1)
        
        url_button = InlineKeyboardButton("ℙ𝕌ℝℂℍ𝔸𝕊𝔼 𝔸ℂℂ𝔼𝕊𝕊", url="https://t.me/aaka8h")
        keyboard.add(url_button)
    return keyboard
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    try:
        user_id = call.message.chat.id
        callback_data = call.data.split('_')
        button_id = callback_data[0]
        if button_id in button_pages_lite:
            user_page[user_id]['current_button'] = button_id
            if len(callback_data) > 1:
                page_number = int(callback_data[1])
                total_pages = len(button_pages_lite.get(button_id, []))
                if 1 <= page_number <= total_pages:
                    page_content = button_pages_lite[button_id][page_number - 1]
                    bot.edit_message_caption(chat_id=user_id, message_id=call.message.message_id, caption=page_content, reply_markup=generate_keyboard(user_id, hide_buttons=True))
                    user_page[user_id][button_id] = page_number
            else:
                bot.edit_message_caption(chat_id=user_id, message_id=call.message.message_id, caption=user_message_content[user_id], reply_markup=generate_keyboard(user_id))
        elif callback_data[0] == 'home':
            bot.edit_message_caption(chat_id=user_id, message_id=call.message.message_id, caption=user_message_content[user_id], reply_markup=generate_keyboard(user_id))
            user_page[user_id] = {}
        else:
            pass
    except Exception as e:
        print(e)
#BotFace Ends
#ProxyScrap
@bot.message_handler(commands=['px'])
@bot.message_handler(func=lambda m: m.text.startswith('.px'))
def send_proxy_list(message):
    proxies = fetch_proxies()
    if proxies:
        bot.reply_to(message, "𝐏𝐑𝐎𝐗𝐈𝐄𝐒 𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐄𝐃 ✅\n\n" + "\n".join(proxies))
    else:
        bot.reply_to(message, "𝐅𝐀𝐈𝑳𝐄𝐃 𝐓𝐎 𝐅𝐄𝐓𝐂𝐇 𝐏𝐑𝐎𝐗𝐈𝐄𝐒. 𝐏𝑳𝐄𝐀𝐒𝐄 𝐓𝐑𝐘 𝐀𝐆𝐀𝐈𝐍 𝑳𝐀𝐓𝐄𝐑.")

def fetch_proxies():
    try:
        api_url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
        response = requests.get(api_url)
        if response.status_code == 200:
            proxies = response.text.split("\r\n")[:40]
            return proxies
        else:
            return None
    except Exception as e:
        print("Error fetching proxies:", e)
        return None
#Proxy Ends
#Gen
def generate_credit_card_info(cc, expiry_month, expiry_year, cvv):
    try:
        generated_num = str(cc)
        while len(generated_num) < 15:
            generated_num += str(random.randint(0, 9))
        check_digit = generate_check_digit(generated_num)
        credit_card_number = generated_num + str(check_digit)
        return f"{credit_card_number}|{str(expiry_month).zfill(2)}|{str(expiry_year)[-2:]}|{cvv}"
    except Exception as e:
        print(e)
def generate_check_digit(num):
    try:
        num_list = [int(x) for x in num]
        for i in range(len(num_list) - 1, -1, -2):
            num_list[i] *= 2
            if num_list[i] > 9:
                num_list[i] -= 9
        return (10 - sum(num_list) % 10) % 10
    except Exception as e:
        print(e)
@bot.message_handler(commands=['gen'])
@bot.message_handler(func=lambda m: m.text.startswith('.gen'))
def generate_credit_card(message):
    try:
        match = re.search(r'(\d{1,16})\D*(\d{1,2}|xx)?\D*(\d{2,4}|xx)?\D*(\d{3,4}|xxx)?', message.text)
        if match:
            card_number = match.group(1)
            cc = card_number
            response_message = ""
            for _ in range(10):
                month = int(match.group(2)) if match.group(2) and match.group(2) != 'xx' else random.randint(1, 12)
                year = int(match.group(3)) if match.group(3) and match.group(3) != 'xx' else random.randint(2025, 2029)
                cvv = int(match.group(4)) if match.group(4) and match.group(4) != 'xxx' else random.randint(100, 999)
                credit_card_info = generate_credit_card_info(cc, month, year, cvv)
                response_message += f"<code>{credit_card_info}</code>\n"
            bot.reply_to(message,  f"𝐂𝐀𝐑𝐃𝐒 𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐄𝐃 ✅\n\n{response_message}", parse_mode="HTML")
        else:
            bot.reply_to(message, '', parse_mode="HTML")
    except IndexError:
        bot.reply_to(message, '', parse_mode="HTML")
#Gen Ends
#BinInfo
@bot.message_handler(commands=['bin'])
@bot.message_handler(func=lambda m: m.text.startswith('.bin'))
def search_bin_info(message):
    bin_number = message.text.split()[-1]
    response = requests.get(f'https://binlist.io/lookup/{bin_number}/')
    if response.status_code == 200:
        bin_info = response.json()
        brand = bin_info.get('scheme', 'Unknown')
        level = bin_info.get('category', 'Unknown')
        type = bin_info.get('type', 'Unknown')
        bank_name = bin_info.get('bank', {}).get('name', 'Unknown')
        bank_phone = bin_info.get('bank', {}).get('phone', 'Unknown')
        bank_url = bin_info.get('bank', {}).get('url', 'Unknown')
        country = bin_info.get('country', {}).get('name', 'Unknown')
        emoji = bin_info.get('country', {}).get('emoji', '')
        response_message = f"𝐁𝐈𝐍 𝐈𝐍𝐅𝐎𝐑𝐌𝐀𝐓𝐈𝐎𝐍: ✅\n\n" \
                           f"𝐁𝐑𝐀𝐍𝐃 : {brand}\n" \
                           f"𝐓𝐘𝐏𝐄 : {type}\n" \
                           f"𝐋𝐄𝐕𝐄𝐋 : {level}\n" \
                           f"𝐁𝐀𝐍𝐊 : {bank_name}\n" \
                           f"𝐏𝐇𝐎𝐍𝐄 : {bank_phone}\n" \
                           f"𝐔𝐑𝐋 : {bank_url}\n" \
                           f"𝐂𝐎𝐔𝐍𝐓𝐑𝐘 : {country} {emoji}"
        bot.reply_to(message, response_message)
    else:
        bot.reply_to(message, "𝐅𝐀𝐈𝐋𝐄𝐃 𝐓𝐎 𝐅𝐄𝐓𝐂𝐇 𝐁𝐈𝐍 𝐈𝐍𝐅𝐎𝐑𝐌𝐀𝐓𝐈𝐎𝐍. 𝐏𝐋𝐄𝐀𝐒𝐄 𝐓𝐑𝐘 𝐀𝐆𝐀𝐈𝐍 𝐋𝐀𝐓𝐄𝐑.")
#Bin Ends
#Fake
first_names = ['John', 'Emma', 'Michael', 'Sophia', 'William', 'Olivia', 'James', 'Ava', 'Alexander', 'Isabella',
               'Daniel', 'Emily', 'Benjamin', 'Charlotte', 'Jacob', 'Mia', 'Ethan', 'Abigail', 'David', 'Ella']
last_names = ['Smith', 'Johnson', 'Brown', 'Williams', 'Jones', 'Miller', 'Davis', 'Garcia', 'Rodriguez', 'Wilson',
              'Martinez', 'Anderson', 'Taylor', 'Thomas', 'Hernandez', 'Moore', 'Martin', 'Jackson', 'Thompson', 'White']
@bot.message_handler(commands=['fake'])
@bot.message_handler(func=lambda m: m.text.startswith('.fake'))
def send_fake_info(message):
    full_name = fake.name()
    street_address = fake.street_address()
    state = fake.state()
    zipcode = fake.zipcode()

    def generate_fake_us_phone_number():
        area_code = random.randint(200, 999)
        first_three_digits = random.randint(200, 999)
        last_four_digits = random.randint(1000, 9999)
        phone_number = f"+1 {area_code}-{first_three_digits}-{last_four_digits}"
        return phone_number
    def generate_fake_email():
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        random_number = random.randint(1000, 9999)
        email = f"{first_name.lower()}.{last_name.lower()}{random_number}@gmail.com"
        return email
    fake_phone_number = generate_fake_us_phone_number()
    fake_email = generate_fake_email()
    response_message = f"𝐈𝐍𝐅𝐎 𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐄𝐃 ✅\n\n" \
                       f"𝐅𝐔𝑳𝑳 𝐍𝐀𝐌𝐄 : <code>{full_name}</code>\n" \
                       f"𝐒𝐓𝐑𝐄𝐄𝐓 𝐀𝐃𝐃𝐑𝐄𝐒𝐒 : <code>{street_address}</code>\n" \
                       f"𝐒𝐓𝐀𝐓𝐄 : <code>{state}</code>\n" \
                       f"𝐙𝐈𝐏𝐂𝐎𝐃𝐄 : <code>{zipcode}</code>\n" \
                       f"𝐏𝐇𝐎𝐍𝐄 𝐍𝐔𝐌𝐁𝐄𝐑 : <code>{fake_phone_number}</code>\n" \
                       f"𝐄𝐌𝐀𝐈𝑳 : <code>{fake_email}</code>"
    bot.reply_to(message, response_message, parse_mode='HTML')
#Fake Ends
#SKGEN
def generate_stripe_keys(num_keys):
    max_keys = min(num_keys, 20)
    sklist = []
    ln = "51HjhvpHJcZaFiVNWse203Mf3aOwYakUdm1VwJpCdSQcJHwXfazxZ5yySPumygYaMfxiRTCGRph4yjamXXb8RfdNE00to0noaTY"
    n = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm12345678912345678901234567890'
    for _ in range(max_keys):
        sk = 'sk_live_' + ''.join(random.choice(n) for i in range(len(ln)))
        sklist.append(sk)
    return sklist

@bot.message_handler(commands=['skgen'])
@bot.message_handler(func=lambda m: m.text.startswith('.skgen'))
def generate_and_send_keys(message):
    command_parts = message.text.split(' ')
    num_keys = 1
    if len(command_parts) > 1:
        try:
            num_keys = int(command_parts[1])
        except ValueError:
            pass
    sklist = generate_stripe_keys(num_keys)
    sk_message = '𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐄𝐃 𝐒𝐓𝐑𝐈𝐏𝐄 𝐀𝐏𝐈 𝐊𝐄𝐘𝐒 ✅:\n'
    for sk in sklist:
        sk_message += f'<code>{sk}</code>\n'
    bot.reply_to(message, sk_message, parse_mode='HTML')
#SKGEN ENDS
#GateLogic Here
card_pattern = re.compile(r'(?<!/ba\s)\b(\d{16})\|(\d{2})\|(\d{2}(?:\d{2})?)\|(\d{3})\b')
#Auth
#@bot.message_handler(commands=['auth'])
def handle_ba_command(message):
    try:
        try:
            cc_info = message.text.split()[1]
            match = card_pattern.match(cc_info)
            if not match:
                bot.reply_to(message, "Invalid format. Please provide CC in the format: cc|mm|yy|cvc")
                return
            n, mm, yy, cvc = match.groups()
            if len(yy) == 2:
                yy = '20' + yy
        except IndexError:
            bot.reply_to(message, "Invalid format. Please provide CC in the format: cc|mm|yy|cvc")
            return


        #تحط بواباتك هنا بالشكل ده
    except Exception as e:
        print(e)#Or send it to your telegram channel to see the error Bro
#GateLogic Ends
bot.infinity_polling()
