import datetime
import os
import shutil
import pandas as pd
import win32com.client as win32

today = datetime.datetime.today().strftime('%m%d%Y_%I%p')

jobs = pd.read_excel("../Job Search/Applied Jobs.xlsx")
