import pandas as pd
import math

careAreas = pd.read_csv(r"C:\Users\skava\Desktop\github\unhack2024\22PW02\Dataset-0\1st\CareAreas.csv", header=None)
metaData = pd.read_csv(r"C:\Users\skava\Desktop\github\unhack2024\22PW02\Dataset-0\1st\metadata.csv")

careAreas.columns = ['Id', 'Xmin', 'Xmax', 'Ymin', 'Ymax']
metaData.columns = ["main_size", "sub_size"]

main_size = float(metaData['main_size'][0])
sub_size = float(metaData['sub_size'][0])

main_list = []

for i in range(len(careAreas)):
    xmin = round(float(careAreas['Xmin'][i]), 6)
    ymin = round(float(careAreas['Ymin'][i]), 6)
    xmax = xmin + main_size
    ymax = ymin + main_size
    main_list.append([i, xmin, xmax, ymin, ymax])

mainFields = pd.DataFrame(main_list, columns=['ID', 'Xmin', 'Xmax', 'Ymin', 'Ymax'])

print(mainFields)

mainFields.to_csv(r"mainfield.csv", index=False, header=None)

def create_sub_list(care_area_id, xmin, xmax, ymin, ymax, sub_size):
    sub_list = []
    sub_id = 0
    num_sub_list_x = math.ceil((xmax - xmin) / sub_size)
    num_sub_list_y = math.ceil((ymax - ymin) / sub_size)
    
    for i in range(num_sub_list_y):
        for j in range(num_sub_list_x):
            sub_xmin = xmin + j * sub_size
            sub_ymin = ymin + i * sub_size
            sub_xmax = sub_xmin + sub_size
            sub_ymax = sub_ymin + sub_size
            
            if sub_xmin <= xmax and sub_ymin <= ymax:
                sub_list.append([sub_id, sub_xmin, sub_xmax, sub_ymin, sub_ymax, care_area_id])
                sub_id += 1
    
    return sub_list

allsub_list = []

for index, row in careAreas.iterrows():
    sub_list = create_sub_list(row['Id'], row['Xmin'], row['Xmax'], row['Ymin'], row['Ymax'], sub_size)
    allsub_list.extend(sub_list)

sub_list_df = pd.DataFrame(allsub_list, columns=['sub_id', 'Xmin', 'Xmax', 'Ymin', 'Ymax', 'CareAreaID'])

print(sub_list_df)

sub_list_df.to_csv(r"subfield.csv", index=False, header=None)