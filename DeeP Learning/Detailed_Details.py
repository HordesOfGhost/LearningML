
import pandas as pd
import numpy as np
#if you have dropped rows you have to reindex to use this function.
def Detailed_Details(df,feature,outcome,max_unique_value_count):
    from IPython.display import HTML, display
    html=f"<h3><center>Comparing {feature} With {outcome}</center></h3>"
    
    
    #for checking type
    type={'int','int16','int32','int64','float','float16','float32','float64'}
    
    uniq_cases=max_unique_value_count
    total_data=len(df)
    
    #defining feature
    df_feature=df[feature]
    check_type=df_feature.dtypes
    
    
    #defining outcome
    df_outcome=df[outcome]
    check_type_outcome=df_outcome.dtypes
    check_type_feature=df_feature.dtypes
    #designing vars
    design=0
    design_feature=0
    if(str(check_type_outcome) in type or str(check_type_feature) in type):   # Checks if feature is of int or float data type
        
        if(df_feature.nunique()<=uniq_cases): #Checks if feature has less unique values
            
            uniq_sorted_ft=sorted(df_feature.unique()) #Sorts features unique values
            
            #Unique occurence of features
            feature_count=np.array(list(df[feature].value_counts().sort_index()))
            
            #Percentage of each occurence of Feature
            feature_percent=[]
            for i in range(0,len(feature_count)):
                feature_percent.append(round(((feature_count[i]/total_data)*100),2))
            feature_percent=np.array(feature_percent)
            
            #UNIQUE NUMERICAL FEATURES AND UNIQUE NUMERICAL OUTCOMES
            if(df_outcome.nunique()<=uniq_cases):
                
                uniq_sorted_ot=sorted(df_outcome.unique()) #list to put unique values for outcome
                
                #Each Unique Occurence of features and outcomes simultanously
                outcome_count = np.array(list(df.groupby([outcome,feature]).size().unstack(fill_value=0).stack()))
                
                #Percentage of Occurence of features with outcome
                
                #partioning feature with respect to outcome
                partition=int(((len(outcome_count)/len(feature_count))or(len(feature_count)/len(outcome_count))))
                #so that percent will be float
                outcome_count_float=[]
                for i in range(0,len(outcome_count)):
                    outcome_count_float.append(float(outcome_count[i]))
                #Calculating outcome percentage
                outcome_percent=[]
                for i in range(0, len(outcome_count_float), len(feature_count)):
                    outcome_percent.append(outcome_count_float[i:i+len(feature_count)])
                
                for i in range(0,len(feature_count)):
                    for j in range(0,partition):
                        outcome_percent[j][i]=((outcome_percent[j][i]/feature_count[i])*100)
                        outcome_percent[j][i]=round(outcome_percent[j][i],2)
                outcome_percent=np.array(outcome_percent)
                
                #indexes of outcome data
                indexes=[]
                for uniq in uniq_sorted_ot:
                    indexes.append(uniq_sorted_ot.index(uniq))
                
                #Display
                html+=f"Total Features {len(df)}  <br>"
                html+="<center><table cellpadding=15>"
                    
                if design==0:
                    html+="<tr>"
                    html+=f"<td>{feature}</td> <td>Total No. ({feature})</td> <td> Percentage ({feature}) </td>"
                    for i in indexes:
                        html+=f"<td>Total {outcome}<br>({uniq_sorted_ot[i]})</td> <td>Percentage {outcome}<br>({uniq_sorted_ot[i]})</td> "
                    html+="</tr>"
                    design=1
                for i in range (0,len(feature_count)):
                    html+="<tr>"
                    for j in range(0,partition):
                        if design_feature==0:
                            html+=f"<td></center>{uniq_sorted_ft[i]}</center></td><td>{feature_count[i]}</td><td>{feature_percent[i]}%</td>"
                        if design_feature==0:
                            html+=f"<td>{outcome_count[i]}</td><td>{outcome_percent[j][i]}%</td>"
                        else:
                            html+=f"<td>{outcome_count[i+len(feature_count)*j]}</td><td>{outcome_percent[j][i]}%</td>"
                        design_feature=1
                    html+=f"</tr>"
                    design_feature=0
                html+="<table></center>"
                display(HTML(html))
                #UNIQUE NUMERICAL FEATURES AND MULTIPLE NUMERICAL OUTCOME
            elif(df_outcome.nunique()>uniq_cases and str(check_type_outcome) in type):
                mean_value=round(df_outcome.mean(),2)
                
                #Dict for Total and percent
                total={}
                percent={}
                #Dict for total above and below mean and thier percentage
                total_outcome_abm={}
                total_outcome_blm={}
                percent_outcome_abm={}
                percent_outcome_blm={}
                #initializing dictionaries with 0
                for i in uniq_sorted_ft:
                    total_outcome_abm[i]=0
                    total_outcome_blm[i]=0
                    total[i]=0
                    percent[i]=0
                    percent_outcome_abm[i]=0
                    percent_outcome_blm[i]=0
                #Count for total above and below mean
                for uniq in uniq_sorted_ft:
                    for i in range(0,len(df)):
                        if(df_outcome[i]>=mean_value):
                            if(df[feature][i]==uniq):
                                total_outcome_abm[uniq]+=1
                        else:
                            if(df[feature][i]==uniq):
                                total_outcome_blm[uniq]+=1
                #Count total in each category
                for uniq in uniq_sorted_ft:
                    total[uniq]=total_outcome_abm[uniq]+total_outcome_blm[uniq]
                #Count percent in each category
                for uniq in uniq_sorted_ft:
                    percent[uniq]=round(total[uniq]/total_data*100,2)
                    percent_outcome_abm[uniq]=round(total_outcome_abm[uniq]/total[uniq]*100,2)
                    percent_outcome_blm[uniq]=round(total_outcome_blm[uniq]/total[uniq]*100,2)
                                             
                #Display
                if design==0:
                    html+=f"Total Features {len(df)}<br>"
                    html+=f"Mean of {outcome} = {mean_value}<br>"
                    html+="<center><table cellpadding=15>"
                    html+="<tr>"
                    html+=f"<td><center>{feature}</center> </td> <td>Total No. <br>({feature})</td> <td> Percentage <br>({feature}) </td>"
                    html+=f"<td>Total No.<br>(Greater Than Mean)</td> <td>Percentage<br>(Greater Than Mean)</td><td>Total No.<br>(Less Than Mean)</td> <td>Percentage <br>(Less Than Mean)</td> "
                    html+="</tr>"
                    design=1
                
                design_feature=0
                for uniq in uniq_sorted_ft:
                    
                    html+="<tr>"    
                    html+=f"<td>{uniq}</td> <td>{total[uniq]}</td><td>{percent[uniq]} %</td><td>{total_outcome_abm[uniq]}</td><td>{percent_outcome_abm[uniq]} %</td><td>{total_outcome_blm[uniq]}</td><td>{percent_outcome_blm[uniq]} %</td>"           
                    html+=f"</tr>"
                html+="</table></center>"
                
                display(HTML(html))
        elif(df_feature.nunique()>uniq_cases and str(check_type_feature)  in type):
                
                mean_value=round(df_feature.mean(),2)
                #Dict for Total and percent
                total={}
                percent={}
                total_abm=0
                total_blm=0
                #Dict for total above and below mean and thier percentage
                total_feature_abm={}
                total_feature_blm={}
                percent_feature_abm={}
                percent_feature_blm={}
                #initializing dictionaries with 0
                uniq_sorted_ot=sorted(df_outcome.unique())
                for i in uniq_sorted_ot:
                    total_feature_abm[i]=0
                    total_feature_blm[i]=0
                    total[i]=0
                    percent[i]=0
                    percent_feature_abm[i]=0
                    percent_feature_blm[i]=0
                #Count below mean and above mean
                for i in range(0,len(df)):
                    if(df_feature[i]>=mean_value):
                        total_abm+=1
                    else:
                        total_blm+=1
                #Count for total above and below mean
                for uniq in uniq_sorted_ot:
                    for i in range(0,len(df)):
                        if(df_feature[i]>=mean_value):
                            if(df[outcome][i]==uniq):
                                total_feature_abm[uniq]+=1
                        else:
                            if(df[outcome][i]==uniq):
                                total_feature_blm[uniq]+=1
                #Count total in each category
                for uniq in uniq_sorted_ot:
                    total[uniq]=total_feature_abm[uniq]+total_feature_blm[uniq]
                #Count percent in each category
                for uniq in uniq_sorted_ot:
                    percent[uniq]=round(total[uniq]/total_data*100,2)
                    percent_feature_abm[uniq]=round(total_feature_abm[uniq]/total[uniq]*100,2)
                    percent_feature_blm[uniq]=round(total_feature_blm[uniq]/total[uniq]*100,2)
                
                #MULTIPLE NUMERICAL FEATURES AND UNIQUE NUMERICAL OUTCOMES 
                if(df_outcome.nunique()<=uniq_cases):
                    uniq_sorted_ot=sorted(df_outcome.unique()) #Sorts features unique values
                   
                    #Unique occurence of features
                    outcome_count=np.array(list(df[outcome].value_counts().sort_index()))
            
                    #Percentage of each occurence of Feature
                    outcome_percent=[]
                    for i in range(0,len(outcome_count)):
                        outcome_percent.append(round(((outcome_count[i]/total_data)*100),2))
                    outcome_percent=np.array(outcome_percent)
            
                    #Checks if outcome has less unique values
                                             
                    #Display
                    if design==0:
                        html+=f"Total Features {len(df)}<br>"
                        html+=f"Mean of {feature} = {mean_value}<br>"
                        html+="<center><table cellpadding=15>"
                        html+="<tr>"
                        html+=f"<td><center>{feature}</center> </td> <td>Total No. <br>({feature})</td> <td> Percentage <br>({feature}) </td>"
                        for uniq in uniq_sorted_ot:
                            html+=f"<td>Total Outcome<br>({uniq})</td><td>Percentage Outcome<br>({uniq})"
                        html+="</td>"
                        html+="</tr>"
                        design=1
                
                    design_feature=0
                    html+=f"<tr><td>Greater Than Mean</td><td>{total_abm}</td><td>{round((total_abm/total_data)*100,2)}</td>"
                    for uniq in uniq_sorted_ot:
                        html+=f"<td>{total_feature_abm[uniq]}</td><td>{percent_feature_abm[uniq]} %</td>"
                    html+=f"<tr><td>Less Than Mean</td><td>{total_blm}</td><td>{round((total_blm/total_data)*100,2)}</td>"
                    for uniq in uniq_sorted_ot:
                        html+=f"<td>{total_feature_blm[uniq]}</td><td>{percent_feature_blm[uniq]} %</td>"  
                    html+="</table></center>"
                
                    display(HTML(html))
                #MULTIPLE NUMERICAL FEATURES AND MULTIPLE NUMERICAL OUTCOMES
                elif(df_outcome.nunique()>uniq_cases and str(check_type_outcome)  in type):
                    mean_value_outcome=round(df_outcome.mean(),2)
                    
                    total_out_abm_fet_abm=0
                    total_out_abm_fet_blm=0
                    total_out_blm_fet_abm=0
                    total_out_blm_fet_blm=0
                        
                    #Count for total above and below mean
                    for i in range(0,len(df)):
                        if(df_outcome[i]>=mean_value_outcome):
                            if(df[feature][i]>=mean_value):
                                total_out_abm_fet_abm+=1
                            else:
                                total_out_abm_fet_blm+=1
                        else:
                            if(df[feature][i]>=mean_value):
                                total_out_blm_fet_abm+=1
                            else:
                                total_out_blm_fet_blm+=1
                    per_out_abm_fet_abm=round((total_out_abm_fet_abm/total_abm*100),2)
                    per_out_abm_fet_blm=round((total_out_abm_fet_blm/total_blm*100),2)
                    per_out_blm_fet_abm=round((100-per_out_abm_fet_abm),2)
                    per_out_blm_fet_blm=round((100-per_out_abm_fet_blm),2)      
                    
                    
                    #Display
                    if design==0:
                        html+=f"Total Features {len(df)}<br>"
                        html+=f"Mean of {feature} = {mean_value}<br>"
                        html+=f"Mean of {outcome} ={mean_value_outcome}<br>"
                        html+="<center><table cellpadding=15>"
                        html+="<tr>"
                        html+=f"<td>{feature} </td> <td>Total No. <br>({feature})</td> <td> Percentage <br>({feature}) </td>"
                        html+=f"<td> Total Outcome <br>Greater Than Mean<br>({mean_value_outcome})</td><td> Percentage Outcome <br>Greater Than Mean<br>({mean_value_outcome})</td>"
                        html+=f"<td> Total Outcome <br>Less Than Mean<br>({mean_value_outcome})</td><td> Percentage Outcome <br>Less Than Mean<br>({mean_value_outcome})</td>"
                        html+="</td>"
                        html+="</tr>"
                        design=1
                
                    design_feature=0
                    html+=f"<tr><td>Greater Than Mean<br>({mean_value})</td><td>{total_abm}</td><td>{round((total_abm/total_data)*100,2)} %</td><td>{total_out_abm_fet_abm}</td><td>{per_out_abm_fet_abm} %</td><td>{total_out_blm_fet_abm}</td><td>{per_out_blm_fet_abm} %</td>"
                    
                    html+=f"<tr><td>Less Than Mean<br>({mean_value})</td><td>{total_blm}</td><td>{round((total_blm/total_data)*100,2)} %</td><td>{total_out_abm_fet_blm}</td><td>{per_out_abm_fet_blm} %</td><td>{total_out_blm_fet_blm}</td><td>{per_out_blm_fet_blm} %</td>"
                      
                    html+="</table></center>"
                    
                    display(HTML(html))
                          
    elif((str(check_type_feature) not in type and df_feature.nunique()<=uniq_cases) and (str(check_type_outcome) not in type) and df_outcome.nunique()<=uniq_cases):
        #UNIQUE STRING FEATURE VS UNIQUE STRING OUTCOME
        if(df_feature.nunique()<=uniq_cases and df_outcome.nunique()<=uniq_cases ): #Checks if feature has less unique values
            
            uniq_sorted_ft=sorted(df_feature.unique()) #Sorts features unique values
            
            #Checks if outcome has less unique values
            uniq_sorted_ot=sorted(df_outcome.unique()) #list to put unique values for outcome
                
            #Unique occurence of features
            feature_count=np.array(list(df[feature].value_counts().sort_index()))
                
                
            #Each Unique Occurence of features and outcomes simultanously
            outcome_count = np.array(list(df.groupby([outcome,feature]).size().unstack(fill_value=0).stack()))
                
            #Percentage of each occurence of Feature
            feature_percent=[]
            for i in range(0,len(feature_count)):
                feature_percent.append(round(((feature_count[i]/total_data)*100),2))
            feature_percent=np.array(feature_percent)    
                
                
            #Percentage of Occurence of features with outcome
                
            #partioning feature with respect to outcome
            partition=int(((len(outcome_count)/len(feature_count))or(len(feature_count)/len(outcome_count))))
            #so that percent will be float
            outcome_count_float=[]
            for i in range(0,len(outcome_count)):
                outcome_count_float.append(float(outcome_count[i]))
            #Calculating outcome percentage
            outcome_percent=[]
            for i in range(0, len(outcome_count_float), len(feature_count)):
                outcome_percent.append(outcome_count_float[i:i+len(feature_count)])
                
            for i in range(0,len(feature_count)):
                for j in range(0,partition):
                    outcome_percent[j][i]=((outcome_percent[j][i]/feature_count[i])*100)
                    outcome_percent[j][i]=round(outcome_percent[j][i],2)
            outcome_percent=np.array(outcome_percent)
                
            #indexes of outcome data
            indexes=[]
            for uniq in uniq_sorted_ot:
                indexes.append(uniq_sorted_ot.index(uniq))
                
            #Display
            html+=f"Total Features {len(df)}<br>"
            html+="<center><table cellpadding=15>"
            if design==0:
                html+="<tr>"
                html+=f"<td><center>{feature}</center> </td> <td>Total No. <br>({feature})</td> <td> Percentage <br>({feature}) </td>"
                for i in indexes:
                    html+=f"<td>Total No.<br>({uniq_sorted_ot[i]})</td> <td>Percentage <br>({uniq_sorted_ot[i]})</td> "
                html+="</tr>"
                design=1
            for i in range (0,len(feature_count)):
                html+="<tr>"
                for j in range(0,partition):
                    if design_feature==0:
                        html+=f"<td></center>{uniq_sorted_ft[i]}</center></td><td>{feature_count[i]}</td><td>{feature_percent[i]}%</td>"
                    if design_feature==0:
                        html+=f"<td>{outcome_count[i]}</td><td>{outcome_percent[j][i]}%</td>"
                    else:
                        html+=f"<td>{outcome_count[i+len(feature_count)*j]}</td><td>{outcome_percent[j][i]}%</td>"
                    design_feature=1
                html+=f"</tr>"
                
                design_feature=0
            html+=f"</table></center>"
            display(HTML(html))
        #MULTIPLE NUMERICAL FEATURES VS UNIQUE STRING OUTCOME
        if (df_feature.nunique()>uniq_cases and str(check_type_feature)  in type and df_outcome.nunique()<=uniq_cases):
            mean_value=round(df_feature.mean(),2)
            uniq_sorted_ot=sorted(df_outcome.unique()) #Sorts features unique values
            #Dict for Total and percent
            total={}
            
            percent={}
            total_abm=0
            total_blm=0
            #Dict for total above and below mean and thier percentage
            total_feature_abm={}
            total_feature_blm={}
            percent_feature_abm={}
            percent_feature_blm={}
            #initializing dictionaries with 0
            uniq_sorted_ot=sorted(df_outcome.unique())
            for i in uniq_sorted_ot:
                total_feature_abm[i]=0
                total_feature_blm[i]=0
                total[i]=0
                percent[i]=0
                percent_feature_abm[i]=0
                percent_feature_blm[i]=0
            #Count below mean and above mean
            for i in range(0,len(df)):
                if(df_feature[i]>=mean_value):
                    total_abm+=1
                else:
                    total_blm+=1
            #Count for total above and below mean
            for uniq in uniq_sorted_ot:
                for i in range(0,len(df)):
                    if(df_feature[i]>=mean_value):
                        if(df[outcome][i]==uniq):
                            total_feature_abm[uniq]+=1
                    else:
                        if(df[outcome][i]==uniq):
                            total_feature_blm[uniq]+=1
            #Count total in each category
            for uniq in uniq_sorted_ot:
                total[uniq]=total_feature_abm[uniq]+total_feature_blm[uniq]
            #Count percent in each category
            for uniq in uniq_sorted_ot:
                percent[uniq]=round(total[uniq]/total_data*100,2)
                percent_feature_abm[uniq]=round(total_feature_abm[uniq]/total[uniq]*100,2)
                percent_feature_blm[uniq]=round(total_feature_blm[uniq]/total[uniq]*100,2)
                        
            #Unique occurence of features
            outcome_count=np.array(list(df[outcome].value_counts().sort_index()))
            
            #Percentage of each occurence of Feature
            outcome_percent=[]
            for i in range(0,len(outcome_count)):
                outcome_percent.append(round(((outcome_count[i]/total_data)*100),2))
            outcome_percent=np.array(outcome_percent)
            
            #Checks if outcome has less unique values
                                             
            #Display
            if design==0:
                html+=f"Total Features {len(df)}<br>"
                html+=f"Mean of {feature} = {mean_value}<br>"
                html+="<center><table cellpadding=15>"
                html+="<tr>"
                html+=f"<td><center>{feature}</center> </td> <td>Total No. <br>({feature})</td> <td> Percentage <br>({feature}) </td>"
                for uniq in uniq_sorted_ot:
                    html+=f"<td>Total Outcome<br>({uniq})</td><td>Percentage Outcome<br>({uniq})"
                html+="</td>"
                html+="</tr>"
                design=1
                
                design_feature=0
                html+=f"<tr><td>Greater Than Mean</td><td>{total_abm}</td><td>{round((total_abm/total_data)*100,2)}</td>"
                for uniq in uniq_sorted_ot:
                    html+=f"<td>{total_feature_abm[uniq]}</td><td>{percent_feature_abm[uniq]} %</td>"
                html+=f"<tr><td>Less Than Mean</td><td>{total_blm}</td><td>{round((total_blm/total_data)*100,2)}</td>"
                for uniq in uniq_sorted_ot:
                    html+=f"<td>{total_feature_blm[uniq]}</td><td>{percent_feature_blm[uniq]} %</td>"  
                html+="</table></center>"
                
                display(HTML(html))
        #UNIQUE STRING FEATURES AND MULTIPLE NUMERICAL OUTCOMES
        if(df_feature.nunique()<=uniq_cases and df_outcome.nunique()>uniq_cases and str(check_type_outcome)  in type):
            mean_value=round(df_outcome.mean(),2)
            
            #Dict for Total and percent
            total={}
            percent={}
            #Dict for total above and below mean and thier percentage
            total_outcome_abm={}
            total_outcome_blm={}
            percent_outcome_abm={}
            percent_outcome_blm={}
            #initializing dictionaries with 0
            for i in uniq_sorted_ft:
                total_outcome_abm[i]=0
                total_outcome_blm[i]=0
                total[i]=0
                percent[i]=0
                percent_outcome_abm[i]=0
                percent_outcome_blm[i]=0
            #Count for total above and below mean
            for uniq in uniq_sorted_ft:
                for i in range(0,len(df)):
                    if(df_outcome[i]>=mean_value):
                        if(df[feature][i]==uniq):
                            total_outcome_abm[uniq]+=1
                    else:
                        if(df[feature][i]==uniq):
                            total_outcome_blm[uniq]+=1
            #Count total in each category
            for uniq in uniq_sorted_ft:
                total[uniq]=total_outcome_abm[uniq]+total_outcome_blm[uniq]
            #Count percent in each category
            for uniq in uniq_sorted_ft:
                percent[uniq]=round(total[uniq]/total_data*100,2)
                percent_outcome_abm[uniq]=round(total_outcome_abm[uniq]/total[uniq]*100,2)
                percent_outcome_blm[uniq]=round(total_outcome_blm[uniq]/total[uniq]*100,2)
                                             
            #Display
            if design==0:
                html+=f"Total Features {len(df)}<br>"
                html+=f"Mean of {outcome} = {mean_value}<br>"
                html+="<center><table cellpadding=15>"
                html+="<tr>"
                html+=f"<td><center>{feature}</center> </td> <td>Total No. <br>({feature})</td> <td> Percentage <br>({feature}) </td>"
                html+=f"<td>Total No.<br>(Greater Than Mean)</td> <td>Percentage<br>(Greater Than Mean)</td><td>Total No.<br>(Less Than Mean)</td> <td>Percentage <br>(Less Than Mean)</td> "
                html+="</tr>"
                design=1
                
            design_feature=0
            for uniq in uniq_sorted_ft:
                html+="<tr>"    
                html+=f"<td>{uniq}</td> <td>{total[uniq]}</td><td>{percent[uniq]} %</td><td>{total_outcome_abm[uniq]}</td><td>{percent_outcome_abm[uniq]} %</td><td>{total_outcome_blm[uniq]}</td><td>{percent_outcome_blm[uniq]} %</td>"           
                html+=f"</tr>"
            html+="</table></center>"
            display(HTML(html))
        
    if(df_feature.nunique()>len(df)/1.5 and str(check_type_feature not in type)):
        html_alert=f"<h2><center>CAN'T_EVALUATE_ERROR:<font color='red'> {feature}</font> as <font color='red'> Feature </font> is of type <font color='red'>{check_type_feature}</font> having a large number of unique values.</center></h2>"
        display(HTML(html_alert))          
    if(df_outcome.nunique()>len(df)/1.5 and str(check_type_outcome not in type)):
        html_alert=f"<h2><center>CAN'T_EVALUATE_ERROR:<font color='red'> {outcome}</font> as <font color ='red'>Outcome </font> is of type <font color='red'>{check_type_outcome}</font> having a large number of unique values.</center></h2>"
        display(HTML(html_alert))  