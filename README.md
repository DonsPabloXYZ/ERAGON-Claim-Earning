# ERAGON AUTO CLAIM EARNING

![alt text](https://github.com/DonsPabloXYZ/ERAGON-Claim-Earning/blob/main/Screenshot_179.jpg)

ERAGON Auto Claim is a Python script designed for automating token claims and performing daily check-ins on the Eragon.gg platform. This script helps users manage token claims efficiently without the need for manual steps.

## Features

- **Automatic Token Claim**: Automatically claim tokens every 10 minutes.
- **Daily Check-in**: Perform daily check-ins for each registered account.
- **Real-Time Time Display**: Show the claim time in WIB format.
- **Detailed Logging**: Provide information about each claim, whether successful or failed.

## Requirements

- Python 3.x
- Libraries:
- `requests`
- `datetime`
- `pytz`
- `colorama

## Installation

- git clone https://github.com/DonsPabloXYZ/ERAGON-Claim-Earning.git
- cd ERAGON-Claim-Earning
- pip install -r requirements.txt
- python main.py

## How It Works

- The script reads tokens from the token.txt file.
- token.txt format
token1
token2
token3
- First, the script performs check-ins for each registered account.
- After the check-ins are complete, the script starts the token claiming process automatically every 10 minutes.

## Get Token

- Right-click anywhere on the page and select Inspect or use the shortcut Ctrl + Shift + I 
- Go to Network Search "me"
- Select Header > authorization > Bearer
- eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.xxxxxxxxxx
- Copas to token.txt

## Contact

If you have any questions or suggestions, please reach out to me on Telegram: @kelasmalamairdrop.

## License

This project is licensed under the **[MIT License](https://opensource.org/licenses/MIT)** - see the [LICENSE](LICENSE) file for details.
