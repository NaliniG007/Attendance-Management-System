from numpy import append
from openpyxl import workbook,load_workbook
#import sri


def writting(presentlist):
    wb=load_workbook('C:/Users/SRIKANTH/OneDrive/Attachments/Document/Book1.xlsx')
    ws=wb['Sheet1']
    ws.append(['Name','Time Stamp'])
    names=presentlist
    print(names)
    for i in names:
        ws.append(i)

    #print(names)
    wb.save('C:/Users/SRIKANTH/OneDrive/Attachments/Document/Book1.xlsx')
    print("writtten succes")    

