import pandas as pd
import math
def readinput():
    careareas = pd.read_csv(r"C:\Users\skava\Desktop\github\unhack2024\22PW02\Dataset-0\1st\CareAreas.csv", header=None)
    metadata = pd.read_csv(r"C:\Users\skava\Desktop\github\unhack2024\22PW02\Dataset-0\1st\metadata.csv")

    careareas.columns = ['id', 'x1', 'x2', 'y1', 'y2']

    main_field_size = metadata.iloc[0, 0]
    sub_field_size = metadata.iloc[0, 1]

    print("Subfield size is: ", sub_field_size)

    main_field = []
    sub_field = []
    for index, row in careareas.iterrows():
        x1 = row['x1']
        x2 = row['x2']
        y1 = row['y1']
        y2 = row['y2']
        sub_id=0
        num_sub_field_x = math.ceil((x2 - x1) / sub_field_size)
        num_sub_field_y = math.ceil((y2 - y1) / sub_field_size)
        for i in range(num_sub_field_y):
            for j in range(num_sub_field_x):
                sub_xmin = x1 + j * sub_field_size
                sub_ymin = y1 + i * sub_field_size
                sub_xmax = sub_xmin + sub_field_size
                sub_ymax = sub_ymin + sub_field_size
            
                if sub_xmin <= x2 and sub_ymin <= y2:
                    sub_field.append([ sub_xmin, sub_xmax, sub_ymin, sub_ymax, index])
                    sub_id += 1
    df = pd.DataFrame(main_field, columns=["Xmin", "Xmax", "Ymin", "Ymax"])
    df1= pd.DataFrame(sub_field)
    df.to_csv("mainfield.csv",header=False)
    df1.to_csv("subfield.csv",header=False)
    print("csv file created")
readinput()