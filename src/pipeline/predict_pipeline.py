import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        Item_Identifier: int,
        Item_Weight: int,
        Item_Fat_Content: int,
        Item_Visibility: int,
        Item_Type: int,
        Item_MRP: int,
        Outlet_Size: int,
        Outlet_Location_Type: int,        
        Outlet_Type: int):

        self.Item_Identifier = Item_Identifier

        self.Item_Weight = Item_Weight

        self.Item_Fat_Content = Item_Fat_Content

        self.Item_Visibility = Item_Visibility

        self.Item_Type = Item_Type

        self.Item_MRP = Item_MRP

        self.Outlet_Size = Outlet_Size

        self.Outlet_Location_Type = Outlet_Location_Type

        self.Outlet_Type = Outlet_Type

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Item_Identifier": [self.Item_Identifier],
                "Item_Weight": [self.Item_Weight],
                "Item_Fat_Content": [self.Item_Fat_Content],
                "Item_Visibility": [self.Item_Visibility],
                "Item_Type": [self.Item_Type],
                "Item_MRP": [self.Item_MRP],
                "Outlet_Size": [self.Outlet_Size],
                "Outlet_Location_Type": [self.Outlet_Location_Type],
                "Outlet_Type": [self.Outlet_Type],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
