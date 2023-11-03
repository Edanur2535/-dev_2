import pandas as pd
import xlsxwriter
dataFrame=pd.read_excel('kulucka_ogrenci.xlsx')
workbook=xlsxwriter.Workbook('duzenlenmis_liste.xlsx')
worksheet=workbook.add_worksheet()

worksheet.write("A1","ID")
worksheet.write("B1","İSİM")
worksheet.write("C1","SOY İSİM")
worksheet.write("D1","BÖLÜM")
worksheet.write("E1","SINIF")
sayi=2
for students in dataFrame.columns:
    first=students.split("__")
    second=first[0].split("$")
    bolum=first[1]
    sinif=first[2]
    order=second[0]
    ad=second[1]
    soyad=second[2]
    hucre1 = "A" + str(sayi)
    hucre2 = "B" + str(sayi)
    hucre3 = "C" + str(sayi)
    hucre4 = "D" + str(sayi)
    hucre5 = "E" + str(sayi)

    worksheet.write(hucre1,order)
    worksheet.write(hucre2, ad)
    worksheet.write(hucre3,soyad)
    worksheet.write(hucre4, bolum)
    worksheet.write(hucre5, sinif)
    sayi = sayi + 1

workbook.close()



