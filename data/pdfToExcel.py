import pdftables_api

apiKey = 'rgzaxzbg1bcf'
c = pdftables_api.Client(apiKey, timeout=(60, 3600))
c.csv('NICS_Firearm_Checks_-_Month_Year_by_State_Type.pdf',
      'fireArmsSales')  # replace c.xlsx with c.csv to convert to CSV
