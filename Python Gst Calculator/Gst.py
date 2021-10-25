print ('''
MM'"""""`MM            dP   MM'""""'YMM          dP                   dP            dP
M' .mmm. `M            88   M' .mmm. `M          88                   88            88
M  MMMMMMMM .d8888b. d8888P M  MMMMMooM .d8888b. 88 .d8888b. dP    dP 88 .d8888b. d8888P .d8888b. 88d888b.
M  MMM   `M Y8ooooo.   88   M  MMMMMMMM 88'  `88 88 88'  `"" 88    88 88 88'  `88   88   88'  `88 88'  `88
M. `MMM' .M       88   88   M. `MMM' .M 88.  .88 88 88.  ... 88.  .88 88 88.  .88   88   88.  .88 88
MM.     .MM `88888P'   dP   MM.     .dM `88888P8 dP `88888P' `88888P' dP `88888P8   dP   `88888P' dP
MMMMMMMMMMM                 MMMMMMMMMMM

''')
Original_price = input("Original_price>> ")
Net_price = input ("Net_price>> ")
GST_amount = Net_price - Original_price
GST_percent = ((GST_amount * 100) / Original_price)
GST_per = str(GST_percent)
Partl = "GST = "
Part2 = "%"
Final = Partl + GST_per + Part2
print (Final)
