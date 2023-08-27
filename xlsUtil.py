
from openpyxl import Workbook

def createWorkBook(name):
  wb = Workbook()
  return wb

def createWorkSheet(wb,name):
    ws = wb.create_sheet(name)
    ws.title = name
    return ws
    
def  addData( headers, rows,wsName ,xlName):
    wb = createWorkBook(xlName)
    ws = createWorkSheet(wb,wsName)
    ws.append(headers)
    for row in rows:
        ws.append(row)
    wb.save(xlName)
    
      



