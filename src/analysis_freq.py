import warnings
import pandas as pd 
from tabulate import tabulate
import re
    # df = pd.read_csv("data/137-174.xlsx")
    # df_drop = df.drop_duplicates()
    # df_drop = df_drop.drop(columns=['ภาค'])
# tabulate.PRESERVE_WHITESPACE = True

class Analysis_frequency:
    def __init__(self,df):
        self.df =  pd.read_excel(df)
        self.df = self.df.groupby("ความถี่").first().reset_index()
        self.df = self.df.drop_duplicates(subset=["ความถี่"]) 
        self.df = self.df.drop(columns=['ภาค','ผู้ใช้งานในพื้นที่','เขต','อุปกรณ์'])
        self.df["วันที่ตรวจสอบ"] = self.df["วันที่ตรวจสอบ"].str.replace(' 00:00:00','')
        
    
    #check_length data  return
    @staticmethod
    def check_length(value):
        try:
            value = value.replace(r'จัดสรรทดแทนกรมการทหารสื่อสาร', ' ')
           
        except:
            print("dont Have")
          
        else:
            split_value = value.split(',')
            
            if len(split_value) >= 3:
                return split_value[0]
            else:
                return value
            
        
    #have a chance to have users
    def freq_usage(self):
     
        usage = self.df[(self.df['% Occupancy']>5) & (pd.notna(self.df['หน่วยงานผู้ใช้คลื่น']))].copy()
        usage['หน่วยงานผู้ใช้คลื่น'] = usage['หน่วยงานผู้ใช้คลื่น'].apply(self.check_length)
      #  usage =usage.to_dict(orient="records")

        return  usage

    #maybe illegal
    def ferq_illegal(self):
        illegal = self.df[(self.df['% Occupancy']>5) & (pd.isna(self.df['หน่วยงานผู้ใช้คลื่น']))].copy()
        illegal['หน่วยงานผู้ใช้คลื่น'] = "not in db"
       # result_illegal = illegal.to_dict(orient="records")
        return illegal

    #should delete
    def should_delete(self):
        delete = self.df[(self.df['% Occupancy'] < 5 )].copy()   
        delete = delete.fillna("no database")
        delete['หน่วยงานผู้ใช้คลื่น'] = delete['หน่วยงานผู้ใช้คลื่น'].apply(self.check_length)
        #result_delete = delete.to_dict(orient='records')
        return delete

    
filter_freq = Analysis_frequency



# with warnings.catch_warnings():
#     warnings.simplefilter('ignore')
#     amateur_freq = Analysis_frequency('data/137-174.xlsx')
#     usage = amateur_freq.should_delete()
#     print(usage)    

       
    
       











