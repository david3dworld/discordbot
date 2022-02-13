#from selenium import webdriver
#import pandas as pd
#
#PATH = "C:\Program Files (x86)\chromedriver.exe"
#driver = webdriver.Chrome(PATH)
#
#driver.get("https://playa3ull.games")
#
#node_data = driver.find_elements_by_class_name('wpb_wrapper')
#
#data_list = []
#
#for data in node_data:
#    node_price = data.find_element_by_xpath('//*[@id="pb-node-info-table"]/tbody/tr[6]/td[2]/span[1]').text
#    nodes_sold = data.find_element_by_xpath('//*[@id="pb-node-info-table"]/tbody/tr[3]/td[2]').text
#    token_price = data.find_element_by_xpath('//*[@id="pb-node-info-table"]/tbody/tr[6]/td[2]/span[2]').text
#    data_item = {
#        'Node Price': node_price,
#        'Nodes Sold': nodes_sold,
#        'Token Price': token_price
#    }
#    data_list.append(data_item)
#
##df = pd.DataFrame(data_list)
##print(data_item["Node Price"])