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
SESSION      = os.environ.get("SESSION", "AQFowGcApD5BlQuyqE-SarhDRIs2Xlm2xupT4d2r91-X8SlV8ymoz-DDnrwOYs5nyifYZmm6jpICVxARgK4tIvTcTzD1NzgD39lZuBZZjH9cOJGCNT0_HKiCbMT9URotXJiu7KQu3UOyre4jyoQBumK9zYMk-NUgp86gEEcLWry-gyyX_Oli2nWl2KP_OSozicdIKI7I81qUGQcDQf-YRpCCsbiILSYFaSNABRBtUvqX04V5PKvXVO8qGt9N3-l7MTlAI0ucWm_gpTKySjqhpW3qqRuxtGilpSIUxtjfqniwCfDW8YozkNtJ_M9fz25ap9Q2U7SGtqe5PAmoQw2QDXtF4V01AwAAAAGlZupAAA")
TIME         = int(os.environ.get("TIME", 1799))
CHATS        = [int(cht) for cht in os.environ.get("CHATS", "-1002165124718 -1002192898527 -1001806393841 -1002028003841 -1002130385569 -1001860587879 -1001998223606 -1001731538618 -1002125318782 -1002124016839 -1001829721717 -1002118247955 -1002226662541 -1002093568632 -1001952162324 -1002225302404").split()]
WHITE_LIST   = [int(wht) for wht in os.environ.get("WHITE_LIST", "").split()]
BLACK_LIST   = [int(blk) for blk in os.environ.get("BLACK_LIST", "").split()]
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://B:B@cluster0.yyeayop.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
PORT         = os.environ.get("PORT", "8080")
