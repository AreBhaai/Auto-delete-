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

API_ID       = int(os.environ.get("API_ID", "20925335"))
API_HASH     = os.environ.get("API_HASH", "bfd4023766d6081305379bdbe124e9c0")
BOT_TOKEN    = os.environ.get("BOT_TOKEN", "6728912571:AAFhBuHfBJz7w8nFDPlEPI-t6Sx68Utx2kY")
SESSION      = os.environ.get("SESSION", "AQE_S5cAf_E9_A1rVIOyPks6728QlQCVguYTCPTdJlfCvR1oX1TX_Dd3_Y6e2aUtopgQcnUKT-gFixeg0UnFs2uUUeVxQJN_DABMBSPTobdgylnsl0xANUP82qwLXG7G9weSJPa2GvaVy-MjdmCwQhYXAaAL4XIusIYAflFsmH6r-xnuWLyg0jLzDkgKdxiRMRjjatzkHGrxfHOexN3H-PRKWYJLnJJ_D73U-HuAK13gP6N_LhaVl3UXcm2HhEFVWqGYt4JBAK-EnDaaf09jGgxSLmiKxnEcODXUCZd8FKS8swgcmo8gH9pxiGEeeDkF8cLEnGrlXMqdIyMtbtOrBDKUDI7OQwAAAAGFPEFwAA")
TIME         = int(os.environ.get("TIME", 10))
CHATS        = [int(cht) for cht in os.environ.get("CHATS", "-1002130385569 -1001998223606 -1002125318782 -1001860587879 -1001731538618 -1002124016839 -1001829721717").split()]
WHITE_LIST   = [int(wht) for wht in os.environ.get("WHITE_LIST", "").split()]
BLACK_LIST   = [int(blk) for blk in os.environ.get("BLACK_LIST", "").split()]
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://knight_rider:GODGURU12345@knight.jm59gu9.mongodb.net/?retryWrites=true&w=majority")
PORT         = os.environ.get("PORT", "8080")
