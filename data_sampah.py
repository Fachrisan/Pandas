import pandas as pd 

dataframe_scv = pd.read_csv('jumlah_produksi_sampah.csv')
print(dataframe_scv)


tahun1 = 2019
produksi_tertentu1 = 0

for i, r in dataframe_scv.iterrows():
    if r["tahun"] == tahun1 and pd.notna(r["jumlah_produksi_sampah"]) :
        produksi_tertentu1 += r['jumlah_produksi_sampah']
print(f"\nTotal produksi pada tahun {tahun1}: {produksi_tertentu1} ton")


produksi_pertahun = {}

for i, r in dataframe_scv.iterrows():
    if pd.notna(r["jumlah_produksi_sampah"]):
        tahun = r["tahun"]
        jumlah_produksi = r["jumlah_produksi_sampah"]
    
        if tahun in produksi_pertahun:
            produksi_pertahun[tahun] += jumlah_produksi 
        else:
            produksi_pertahun[tahun] = jumlah_produksi 
print("\nTotal produksi sampah pertahun:")
print(pd.Series(produksi_pertahun))


produksi_sampah = {}

for i, r in dataframe_scv.iterrows():
    if pd.notna(r["jumlah_produksi_sampah"]):
        kota = r["nama_kabupaten_kota"]
        tahun = r["tahun"]
        jumlah_produksi = r["jumlah_produksi_sampah"]

        if (kota, tahun) in produksi_sampah:
            produksi_sampah[(kota, tahun)] += jumlah_produksi  
        else:
            produksi_sampah[(kota, tahun)] = jumlah_produksi 


print("\nTotal produksi sampah kota/kabupaten pertahun:")
print(pd.Series(produksi_sampah))



df_produksi_pertahun = pd.DataFrame(list(produksi_pertahun.items()), columns=["Tahun", "Total Produksi Sampah (ton)"])
df_produksi_pertahun.to_csv("produksi_sampah_pertahun.csv", index=False)

print("\nBerhasil Menambahkan")