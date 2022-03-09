import pandas as pd

path = r"C:\Users\gauta\Desktop\epam_training\Movie+Assignment+Data.csv"

data = pd.read_csv( path )

print( data.head() )
