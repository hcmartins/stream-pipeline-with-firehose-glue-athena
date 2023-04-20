from generate_click_data import generate_click_data
from kenesis_firehose import KinesisFireHose
 
  
def main():
    for i in range(1, 30):
 
        json_data = generate_click_data()
        print(json_data)
        helper = KinesisFireHose()
        helper.insert_item(json_data=json_data)
 

main()
