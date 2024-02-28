import os 
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    
    '''
    This class puts the data in the artifacts folder i.e train,test and raw data 
    When you are defining the variables then only use the dataclass instead use init only
    '''
    train_data_path : str = os.path.join('artifacts',"train.csv")
    test_data_path : str = os.path.join('artifacts',"test.csv")
    raw_data_path : str = os.path.join('artifacts',"data.csv")


class DataIngestion:

    ''' 
    It takes the three data from the above code and save it in a ingestion_config
    '''
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or conmponent")
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the Dataset as dataframe')
        
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True) # we are taking os.path.dirname so that if the folder is present it will not take it again .
            
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
        
