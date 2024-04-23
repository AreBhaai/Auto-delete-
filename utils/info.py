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
SESSION      = os.environ.get("SESSION", "AQFowGcAMkv5NEWXmPPp7dQb9qSb-B6ACbQs5khqrAvA5suyl4BWLeL7jT-V5flL4bR2CP0QhI9w83UjZvgi3nl43g59oCFmfFBrNVdAzsDZKXLouU3216tq5pUL-bW5nz29NiOms19CZQwGE9LH0jYn_T_uirSyAdZmeVriUzKinR6Y2zmU5N4-_yBTJZEvb0aWZqXD0n8FUHGwCGCzdXIR0BKFrts-p67COmrubF-GtXcYDC_I1whyrUzrzgoDIlPLJw5iGrQ9Abr2K7-QlanIYzeg1K_I8WYDU6UuuHJ3vw6-MCdnzSeqdYFWUb2-ouILzLyKez6mXRMp0gAOn92OjmlMEgAAAAGlZupAAA")
TIME         = int(os.environ.get("TIME", 1799))
CHATS        = [int(cht) for cht in os.environ.get("CHATS", "-1002130385569 -1001860587879 -1001998223606 -1001731538618 -1002125318782 -1002124016839 -1001829721717 -1002118247955").split()]
WHITE_LIST   = [int(wht) for wht in os.environ.get("WHITE_LIST", "").split()]
BLACK_LIST   = [int(blk) for blk in os.environ.get("BLACK_LIST", "").split()]
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://knight_rider:GODGURU12345@knight.jm59gu9.mongodb.net/?retryWrites=true&w=majority")
PORT         = os.environ.get("PORT", "8080")
