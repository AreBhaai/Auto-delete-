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
SESSION      = os.environ.get("SESSION", "AQFowGcAKckPor7j0klq8Al4AIC-ZMdCcAYMYqAOJ8Tqbp-2yeVFffkxzHzj7AWAaS0ImGvT8SZwuMrMcNm4wXesFxwm6abFXMA5ooF9CFHpQVuBR7XfYj3825ZZXa7Vn9CYVrQLgTo9vxB2OceJlZM_pBrc-NsnQgPwhv0ujiNWC98kDpf80KEsTOtSooaS13R1Hl969xC4Y7AgrKwH97vgFHImliYBoqZHyUJiu2kvP-BMNFPZQRxF-yQfogwFL_0Rgw09sP_FC5EHpYVhfjEqckfvtvCc6m9DOs3pywjkP3TnEO4B8ESqY4PwYmh-bGMiNwh4f2HUYw4f2xl_74uSkL6U5AAAAAGlZupAAA")
TIME         = int(os.environ.get("TIME", 1799))
CHATS        = [int(cht) for cht in os.environ.get("CHATS", "-1002130385569 -1001860587879 -1001998223606 -1001731538618 -1002125318782 -1002124016839 -1001829721717 -1002118247955").split()]
WHITE_LIST   = [int(wht) for wht in os.environ.get("WHITE_LIST", "").split()]
BLACK_LIST   = [int(blk) for blk in os.environ.get("BLACK_LIST", "").split()]
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://B:B@cluster0.yyeayop.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
PORT         = os.environ.get("PORT", "8080")
