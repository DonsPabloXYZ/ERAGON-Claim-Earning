import requests
from datetime import datetime
import time
import pytz,json,threading
from colorama import Fore, Style, init
init(autoreset=True)
red = Fore.LIGHTRED_EX
blue = Fore.LIGHTBLUE_EX
green = Fore.LIGHTGREEN_EX
yellow = Fore.LIGHTYELLOW_EX
black = Fore.LIGHTBLACK_EX
white = Fore.LIGHTWHITE_EX
reset = Style.RESET_ALL
magenta = Fore.LIGHTMAGENTA_EX


url = 'https://api-mainnet.eragon.gg'

def ll(x):
    print(json.dumps(x, indent=4))
    
def afterClaim(token):
    api_url = f"{url}/users/claimEra3MineSession"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": f"Bearer {token}",
        "if-none-match": "W/\"2bf-FeeYcHBnwqm634PX5ZWvvlvcoIY\"",
        "priority": "u=1, i",
        "sec-ch-ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "Referer": "https://eragon.gg/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }

    response = requests.delete(api_url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Gagal, status kode: {response.status_code}")
        return None

from colorama import Fore, Style

def claim_era3_mine_session(token, index):
    api_url = f"{url}/users/claimEra3MineSession"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": f"Bearer {token}",
        "priority": "u=1, i",
        "sec-ch-ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "Referer": "https://eragon.gg/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    data = {"claimImmediate": True}  
    response = requests.post(api_url, headers=headers, json=data)

    if response.status_code == 201:
        response_data = response.json()
        era3 = response_data['data']['era3']

        session_rate = response_data['data']['sessionEra3Rate']  # Pastikan ini adalah float
        
        if isinstance(session_rate, str):
            session_rate = float(session_rate.replace(',', '.'))  # Ganti koma dengan titik jika perlu
        elif isinstance(session_rate, float):
            session_rate = session_rate  # Sudah dalam bentuk float
        
        session_rate = f"{session_rate:.10f}"

        # Mengambil waktu saat ini (WIB)
        wib_time = datetime.now(pytz.timezone('Asia/Jakarta')).strftime('%H:%M:%S')
        
        # Menampilkan output klaim dalam format yang diinginkan dengan warna
        print(f"{Fore.LIGHTWHITE_EX} [{black}{wib_time}{white}]{red} - {Style.BRIGHT + Fore.LIGHTMAGENTA_EX}Account Info{Style.RESET_ALL}")
        print(f"{Fore.LIGHTWHITE_EX} [{black}{wib_time}{white}]{red} - {yellow}User: {Fore.LIGHTGREEN_EX}{index}{Style.RESET_ALL}")
        print(f"{Fore.LIGHTWHITE_EX} [{black}{wib_time}{white}]{red} - {Fore.LIGHTYELLOW_EX}Total pEGON: {Fore.LIGHTBLUE_EX}{era3}{Style.RESET_ALL}")
        print(f"{Fore.LIGHTWHITE_EX} [{black}{wib_time}{white}]{red} - {Fore.LIGHTGREEN_EX}Success For Claim{Style.RESET_ALL}")
        print(f"{Fore.WHITE}-==========[github.com/DonsPabloXYZ]==========-{Fore.RESET}")
    else:
        print(f"Gagal klaim coin, status kode: {response.status_code}")
        print(response.text)
        return None, 0  # Mengembalikan None dan 0 jika gagal


def countdown_timer(seconds, display=True):
    while seconds:
        mins, secs = divmod(seconds, 60)
        hours, mins = divmod(mins, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)

        # Menghitung sisa waktu
        time_remaining = f"{hours:02d}:{mins:02d}:{secs:02d}"

        # Menentukan ukuran progress bar
        total_length = 30  # Panjang progress bar
        filled_length = int(total_length * (1 - seconds / (120 * 5)))  # Menyesuaikan dengan waktu total
        
        # Membuat progress bar dengan gradasi warna
        progress_bar = ''
        for i in range(filled_length):
            # Menghitung gradasi warna
            if i < filled_length / 2:
                # Warna hijau
                progress_bar += f"{Fore.LIGHTBLUE_EX}█"  # Karakter penuh dengan warna hijau
            else:
                # Warna kuning
                progress_bar += f"{Fore.LIGHTMAGENTA_EX}█"  # Karakter penuh dengan warna kuning

        # Menambahkan karakter kosong
        progress_bar += '-' * (total_length - filled_length)  # Progress bar
        if display:
            # Cetak bar dengan "\r" di akhir untuk memperbarui baris yang sama
            print(f" [{Fore.MAGENTA}{Fore.YELLOW}NEXT CLAIM:{magenta} {time_remaining}{Fore.RESET}] - [{progress_bar}{Fore.RESET}]", end='\r', flush=True)
        
        time.sleep(1)
        seconds -= 1

    if display:
        # Bersihkan karakter sisa setelah countdown selesai
        print(" " * (len(f" [{Fore.MAGENTA}{Fore.YELLOW}NEXT CLAIM:{magenta} {time_remaining}{Fore.RESET}] - [{progress_bar}{Fore.RESET}]") + 2), end='\r')  # Membersihkan baris



def getme(token):
    api_url = f"{url}/users/me"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": f"Bearer {token}",
        "if-none-match": "W/\"2bf-FeeYcHBnwqm634PX5ZWvvlvcoIY\"",
        "priority": "u=1, i",
        "sec-ch-ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "Referer": "https://eragon.gg/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Gagal, status kode: {response.status_code}")
        return None

def checkinmodul():
  
    url = "https://api.mainnet.aptoslabs.com/v1/accounts/0x6d138096fb880d1c16b48f10686b98a96000c0ac18501425378f784c6b81c34d/module/eragon_checkin"

    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9,id;q=0.8",
        "priority": "u=1, i",
        "sec-ch-ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "x-aptos-client": "aptos-typescript-sdk/1.28.0",
        "x-aptos-typescript-sdk-origin-method": "getModule",
        "Referer": "https://eragon.gg/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }

    response = requests.get(url, headers=headers)
    return response.json()

def exe_checkin(token,sender,id):
    url = f"https://api-mainnet.eragon.gg/aggregate-event-records/6699da80291a748b95739ee1/daily-check-in?userId={id}"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9,id;q=0.8",
        "authorization": f'Bearer {token}',  # Gunakan variabel token
        "content-type": "application/json",
        "priority": "u=1, i",
        "sec-ch-ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "Referer": "https://eragon.gg/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }

    # Data body permintaan
    data = {
        "senderAuthHex": "0x02031b68747470733a2f2f6163636f756e74732e676f6f676c652e636f6d20b524b671675ed37245d907a6e220a369a0134db68880b44b75385e92d695e62303000091bdaef2fa57b4754c45f97a9e19b38e5b0032be23f0d8c65f74846c37d94a2ca5ccd2de7a940f88be06ce02eb3cb8c9e1af0f95c6798eaf6259b2b86c40ef086f909200168f92e62d29defac9c0891e05c06f65b2663d606ae70adaa932571a1816bd679ea7885336d4f257f8c6dc7f278f24d70422f0fa6eba34111d8534298096980000000000000001004028926e1180a6ce03351b9db8c0f3721128f6511bb6ecbe05f92a4b27d1d89eff42b14d5818323cee944a501dc782afeab331f661086c1b2a101ec63f010bcb044c7b22616c67223a225253323536222c226b6964223a2235616166663437633231643036653236366363653339356232313435633763366434373330656135222c22747970223a224a5754227d00400d67000000000020097598291aeaee4ddd0e5f26338c6f4cd80fb6e093c16dba0c59e98e2d22b6a400405b5aafcb56eab736e6cd30531b9cf0921878401605622e6bf2fa9866cca61db3a8816e89daf54da39df9ce24c3ac3c0593c1af11efd27c32fc95ad64615c7705",
        "transactionHex": f"{sender}0000000000000000026d138096fb880d1c16b48f10686b98a96000c0ac18501425378f784c6b81c34d0e657261676f6e5f636865636b696e08636865636b5f696e00001027000000000000640000000000000073cffa660000000001010000000000000000000000000000000000000000000000000000000000000000",
        "sender": sender
    }

    # Kirim permintaan POST
    response = requests.post(url, headers=headers, json=data)   
    return response.json()

def checkin(token, index, total_tokens):
    checkinmodul()
    me = getme(token)
    id = me['data']['_id']
    aptos_address = me['data']['aptosAddress']

    # Mendapatkan waktu saat ini di zona waktu Asia/Jakarta
    wib_time = datetime.now(pytz.timezone('Asia/Jakarta')).strftime('%H:%M:%S')

    # Bersihkan output sebelum cetak log baru
    print(f"{' ' * 80}", end='\r', flush=True)  # Membersihkan jejak waktu sebelumnya
    
    # Menampilkan token yang sedang diproses
    print(f"{Fore.LIGHTWHITE_EX} [{black}{wib_time}{white}]{red} - {white}Login As: {Fore.LIGHTYELLOW_EX}Acc {index}{Style.RESET_ALL}")
    print(f"{Fore.LIGHTWHITE_EX} [{black}{wib_time}{white}]{red} - {Fore.LIGHTWHITE_EX}Login{green} Success{Style.RESET_ALL}")
    
    res_checkin = exe_checkin(token=token, sender=aptos_address, id=id)

    # Cek jika respon berhasil atau gagal
    if res_checkin:
        if "description" in res_checkin and "Already checked today" in res_checkin['description']:
            print(f"{Fore.LIGHTWHITE_EX} [{black}{wib_time}{white}]{red} - {yellow}Account {Fore.LIGHTGREEN_EX}{index} {Fore.LIGHTRED_EX} Please Manual Check In{Style.RESET_ALL}")
            print(f"{Fore.WHITE}-==========[github.com/DonsPabloXYZ]==========-{Fore.RESET}")
            print(f"{Fore.LIGHTGREEN_EX} Please Wait..{Fore.RESET}")

            




def main_earning():
    # Membaca token dari file token.txt
    with open("token.txt", "r") as file:
        tokens = [line.strip() for line in file.readlines()]
 
    while True:
        for index, token in enumerate(tokens, start=1):
       
            claim_era3_mine_session(token, index)
        countdown_timer(120 * 5)  # Menghitung mundur selama 10 menit
        
def main_checkin():
    # Membaca token dari file token.txt
    with open("token.txt", "r") as file:
        tokens = [line.strip() for line in file.readlines()]
    
    total_tokens = len(tokens)  # Menghitung total token
    
    for index, token in enumerate(tokens, start=1):
        checkin(token, index, total_tokens)  # Melakukan check-in
        time.sleep(5)  # Delay antara check-in (opsional, bisa dihapus jika tidak diperlukan)

    # Tidak ada countdown, langsung selesai check-in


if __name__ == "__main__":
    # Jalankan checkin terlebih dahulu
    main_checkin()
    
    # Setelah checkin selesai, jalankan earning
    main_earning()
