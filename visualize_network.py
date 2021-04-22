# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 03:48:19 2021

@author: Bin Tang
"""

import pandas as pd
import networkx as nx

def main():
    #client needs to change each project file name here:
    file_path = "14312511_interactions.xlsx" 
    #from here, if the file is excel, no need to change
    df = pd.read_excel(file_path, index_col=0)
    
    G_weighted = nx.Graph()
    for index, row in df.iterrows():
        G_weighted.add_edge(row["commentor.name"], \
                            row["mention.name"],\
                            weight = row["count"])
    
    nx.draw_networkx(G_weighted)  
    
main()
