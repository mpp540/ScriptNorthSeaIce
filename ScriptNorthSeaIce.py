import pandas as pd
import matplotlib.pyplot as plt

url_csv = 'https://sandbox.zenodo.org/record/26045/files/N_seaice_extent_daily_v3.0.csv'

df = pd.read_csv(url_csv)

columna_extension = 'Extent'
median_by_year = df.groupby('Year')[columna_extension].median().reset_index()

# Graficar los datos
plt.figure(figsize=(10, 6))
plt.plot(median_by_year['Year'], median_by_year[columna_extension], marker='o', linestyle='-', color='blue')
plt.title('Median Sea Ice Extent Over Years (Hemisferio Norte)')
plt.xlabel('Year')
plt.ylabel('Median Extent')
plt.grid(True)
plt.show()
