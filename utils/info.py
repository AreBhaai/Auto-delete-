#=========================================================================
# [AutoDelete - Telegram bot to delete messages after specific time]      
# Copyright (C) 2022 Arunkumar Shibu                       
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#=========================================================================

import os

API_ID       = int(os.environ.get("API_ID", "23642215"))
API_HASH     = os.environ.get("API_HASH", "7fbd4d621dc44fda39956268bb78f42f")
BOT_TOKEN    = os.environ.get("BOT_TOKEN", "6728912571:AAFhBuHfBJz7w8nFDPlEPI-t6Sx68Utx2kY")
SESSION      = os.environ.get("SESSION", "AQFowGcAAAOLRVBPL-eSKJsr--ijfyqrr-HR4vqzga7SJWTXMfvTcqXpbNB9UzSuYV-uMSSj8S2syWztjKQz2e_5CFjv96llwYKR8-k4fDr8IxKvOkPNk0OkhvWkMIp0vCjwMxwxUsK_n5XR6o1AyUfGzV9BwQGSsi6zCDUYmd_adWPdCAtqFzSUm3G1y1ATWxR--FM5Pq99USXfsoQNp_fCFM0wfNazMS_sFiZOSTizk9dxaNYNY8PdM9ZtzWl2k8vDcEA2VwKRqVeMeYmpgvv2jo730_8zyHlTcXa3uASsK-dfwkT19fqpa83gv-sIy0wuHk_-wmZK01dZUGJ_mKDz5QrDjAAAAAGlZupAAA")
TIME         = int(os.environ.get("TIME", 1799))
CHATS        = [int(cht) for cht in os.environ.get("CHATS", "-1002130385569 -1001860587879 -1001998223606 -1001731538618 -1002125318782 -1002124016839 -1001829721717 -1002118247955").split()]
WHITE_LIST   = [int(wht) for wht in os.environ.get("WHITE_LIST", "").split()]
BLACK_LIST   = [int(blk) for blk in os.environ.get("BLACK_LIST", "").split()]
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://B:B@cluster0.yyeayop.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
PORT         = os.environ.get("PORT", "8080")
