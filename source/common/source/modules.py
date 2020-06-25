import pandas as pd
import numpy as np
import cornac.models.recommender as cmr
import math

import warnings
warnings.filterwarnings("ignore")

def mag(x): return math.sqrt(sum(i**2 for i in x))

def cosine_similarity(p_m, u_m, user_id):
    cos_sim = []
    
    u_vec = u_m.loc[user_id,:]
    u_size = mag(u_vec)

    for i in range(len(p_m)):
        p_vec = p_m.iloc[i,:]
        p_size = mag(p_vec)
        cos_sim.append(np.dot(p_vec, u_vec)/(p_size*u_size))
        
    return cos_sim

#Eat_contents_based
def Eat_recommendation(u_id):
     # 0. preprocess place_matrix
    place_matrix = pd.read_csv('../../Eat/data/normalized_item_matrix.csv')
    cbf = place_matrix[['p_id']]
    place_matrix.set_index('p_id', inplace=True)
    
     # 1. preprocess user_matrix
    user_matrix = pd.read_csv('../../Eat/data/normalized_user_matrix.csv')
    user_id  = 'u1s2&'+u_id
    user_index = user_matrix[user_matrix['u_id']==user_id].index[0]
    del user_matrix['u_id']
    
    # 2. cbf result
    cbf_result = cosine_similarity(place_matrix, user_matrix, user_index)
    cbf['cbf'] = cbf_result
    cbf.set_index('p_id', inplace=True, drop=True)
    print('Complete to get Eat - contents_based result')
    
    # 3. ncf result
    ncf = pd.read_csv('../../Eat/data/predictions/ncf_scores.csv')
    ncf.rename(columns = {'ncf_score':'ncf'}, inplace=True)
    ncf = ncf[ncf['u_id'] == u_id]
    del ncf['u_id']
    ncf['p_id'] = ncf['p_id'].astype(int)
    ncf.set_index('p_id', inplace=True, drop=True)
    print('Complete to get Eat - ncf result')
    
    # 4. make_matrix
    eat_info =  pd.read_csv('../../Eat/data/translated_eat_info.csv')
    eat_info = pd.DataFrame(eat_info, columns=['p_id','name','address'])
    eat_info.set_index('p_id', inplace=True, drop=True)
    eat_info['district'] = 0
    for i in range (0, len(eat_info['address'])):
        eat_info['district'][i] = eat_info['address'][i].split(' ')[1]
    print('Complete to make Eat -Result matrix')
    
    # 5. join more
    result = eat_info.join(cbf, how='left').join(ncf, how='left')
    result['result'] = result['cbf'] * result['ncf']
    result.sort_values(by=['result'], inplace=True, ascending=False)
    
    return result

#Go_contents_based
def Go_recommendation(u_id):
    # 0. preprocess place_matrix
    place_matrix = pd.read_csv('../../Go/data/normalized_item_matrix.csv')
    cbf = place_matrix[['p_id']]
    del place_matrix['total_count']
    place_matrix.set_index('p_id', inplace=True)
    
    # 1. preprocess user_matrix
    user_matrix = pd.read_csv('../../Go/data/normalized_user_matrix.csv')
    user_id  = 'u1s2&'+u_id
    user_index = user_matrix[user_matrix['u_id']==user_id].index[0]
    del user_matrix['u_id']
    del user_matrix['total_count']
    
    # 2. cbf result
    cbf_result = cosine_similarity(place_matrix, user_matrix, user_index)
    cbf['cbf'] = cbf_result
    cbf.set_index('p_id', inplace=True, drop=True)
    print('Complete to get Go - contents_based result')
    
    # 3. ncf result
    ncf = pd.read_csv('../../Go/data/ncf_scores2.csv')
    ncf.rename(columns = {'ncf_score':'ncf'}, inplace=True)
    ncf = ncf[ncf['u_id'] == u_id]
    del ncf['u_id']
    ncf.set_index('p_id', inplace=True, drop=True)
    print('Complete to get Go - ncf result')
    
    # 4. make_matrix
    go_info =  pd.read_csv('../../Go/data/item_info.csv')
    go_info = pd.DataFrame(go_info, columns=['p_id','p_name','address'])
    go_info['district'] = 0
    for i in range (0, len(go_info['address'])):
        try:
            if ' ' in go_info['address'][i]:
                go_info['district'][i] = go_info['address'][i].split(' ')[1]
            else:
                go_info['district'][i] = go_info['address'][i]
        except:
            pass
    go_info.set_index('p_id', inplace=True, drop=True)
    print('Complete to make Go - Result matrix')
    
    # 5. join more
    result = go_info.join(cbf, how='left').join(ncf, how='left')
    result['result'] = result['cbf'] * result['ncf']
    result.dropna(inplace=True)
    result.sort_values(by=['result'], inplace=True, ascending=False)
    
    return result

#Watch_contents_based
def Watch_recommendation(u_id):
    # 0. preprocess place_matrix
    place_matrix = pd.read_csv('../../Watch/data/normalized_item_matrix.csv')
    cbf = place_matrix[['p_id']]
    place_matrix.set_index('p_id', inplace=True)
    
     # 1. preprocess user_matrix
    user_matrix = pd.read_csv('../../Watch/data/normalized_user_matrix.csv')
    user_id  = 'u1s2&'+u_id
    user_index = user_matrix[user_matrix['u_id']==user_id].index[0]
    del user_matrix['u_id']
    
    # 2. cbf result
    cbf_result = cosine_similarity(place_matrix, user_matrix, user_index)
    cbf['cbf'] = cbf_result
    cbf.set_index('p_id', inplace=True, drop=True)
    print('Complete to get Watch - contents_based result')
    
    # 3. ncf result
    ncf = pd.read_csv('../../Watch/data/predictions/ncf_scores.csv')
    ncf.rename(columns = {'ncf_score':'ncf'}, inplace=True)
    ncf = ncf[ncf['u_id'] == u_id]
    del ncf['u_id']
    ncf['p_id'] = ncf['p_id'].astype(int)
    ncf.set_index('p_id', inplace=True, drop=True)
    print('Complete to get Watch - ncf result')
    
    # 4. make_matrix
    watch_info =  pd.read_csv('../../Watch/data/current_movie.csv')
    watch_info = pd.DataFrame(watch_info, columns=['id','name'])
    watch_info.set_index('id', inplace=True, drop=True)
    print('Complete to make Watch Result matrix')
    
    # 5. join cbf,ncf
    result = watch_info.join(cbf, how='left').join(ncf, how='left')
    result['result'] = result['cbf'] * result['ncf']
    
    # 6.get movie_name
    result.sort_values(by=['result'], ascending=False, inplace=True)
    reco_movie_name = result.iloc[0]['name']
    
    return reco_movie_name

def get_preferred_district(u_id):
    user_survey_df = pd.read_csv('../data/survey_result.csv')
    district = user_survey_df[user_survey_df['u_id'] == u_id]['District'].values[0]
    return district.split(', ')

def Search_Recommendable_Places(eat_matrix, go_matrix, u_id):
    dist_ls = get_preferred_district(u_id)
    eat_matrix = eat_matrix[eat_matrix['district'].isin(dist_ls)]
    go_matrix = go_matrix[go_matrix['district'].isin(dist_ls)]
    
    eat_matrix.reset_index(inplace=True, drop=True)
    go_matrix.reset_index(inplace=True, drop=True)
    
    trial=0
    e_i=0
    g_i=0
    
    if len(dist_ls) > 1 :
        if (eat_matrix['district'][0] == go_matrix['district'][0]):
            print('베스트 행정구 일치!')
            eat_res =  eat_matrix.iloc[0]
            go_res = go_matrix.iloc[0]
            return (eat_res, go_res)
        
        else:
            while (eat_matrix['district'][0] != go_matrix['district'][g_i]):
                g_i = g_i + 1
            eat_res1 =  eat_matrix.iloc[0]
            go_res1 = go_matrix.iloc[g_i]
            
            while (eat_matrix['district'][e_i] != go_matrix['district'][0]):
                e_i = e_i + 1
            eat_res2 =  eat_matrix.iloc[e_i]
            go_res2 = go_matrix.iloc[0]
            
            return(eat_res1, go_res1, eat_res2, go_res2)
        
#         while (e_i< len(eat_matrix) and g_i<len(go_matrix)):
#             if (eat_matrix['district'][e_i] == go_matrix['district'][g_i]):
#                 eat_res =  eat_matrix.iloc[e_i]
#                 go_res = go_matrix.iloc[g_i]
#                 return (eat_res, go_res)
                
#             if (trial%2 == 0):
#                 e_i = e_i+1
#             else:
#                 g_i = g_i+1
#             trial = trial + 1
    else:
        eat_res = eat_matrix[eat_matrix['district']==dist_ls[0]].iloc[0]
        go_res = go_matrix[go_matrix['district']==dist_ls[0]].iloc[0]
        return (eat_res, go_res)

def save_each_user_reco_item(user_id, eat, go, watch):
    pd.to_csv(f'../data/')

