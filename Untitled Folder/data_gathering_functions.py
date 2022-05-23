def getKills(game):
    kills = []
    for frame in game['info']['frames'][0:16]:
        for event in frame['events']:
            if event['type'] == 'CHAMPION_KILL':
                kills.append(event) 
    kills_df = pd.DataFrame(kills)
    kills_count = kills_df[['killerId', 'victimId']].groupby(by='killerId', axis=0).count().reset_index()    
    blank_df = pd.DataFrame({'player':[1,2,3,4,5,6,7,8,9,10]})
    game1_kills_sb = pd.merge(blank_df, kills_count, how="outer", left_on=blank_df.player, right_on=kills_count.killerId).fillna(0)
    game_kills = game1_kills_sb[['victimId']].rename(columns={'victimId':'Kills'})
    blue_team_kills = game_kills['Kills'][0:5].sum()
    red_team_kills = game_kills['Kills'][5:].sum()
    return [blue_team_kills,red_team_kills]

def getVisionScore(game):
    wardsK = defaultdict(int)
    wardsP = defaultdict(int)
    wardinfo = [wardsP, wardsK]
    
    for frame in game['info']['frames'][0:16]:
        for event in frame['events']:
            if ((event['type'] == 'WARD_KILL') and (event['wardType'] != 'UNDEFINED')) : 
                if event['killerId'] in wardsK: 
                    wardsK[event['killerId']] += 1
                else:
                    wardsK[event['killerId']] =1
            elif ((event['type'] == 'WARD_PLACED') and (event['wardType'] != 'UNDEFINED')) :
                if event['creatorId'] in wardsP: 
                    wardsP[event['creatorId']] += 1
                else:
                    wardsP[event['creatorId']] = 1 
    wardinfo_df = pd.DataFrame(wardinfo).T.sort_index().rename(columns={0:'wards_placed',1:'wards_destroyed'}).fillna(0)
    wardinfo_df['VisionScore'] = wardinfo_df.wards_placed + wardinfo_df.wards_destroyed
    wardinfo_df.reset_index(inplace = True)
    blank_df = pd.DataFrame({'player':[1,2,3,4,5,6,7,8,9,10]}) 
    game_ward_sb = pd.merge(blank_df, wardinfo_df, how="outer", left_on=blank_df.player, right_on=wardinfo_df['index'])
    game_wards = game_ward_sb[['VisionScore']]
    blue_team = game_wards['VisionScore'][0:5].sum()
    red_team = game_wards['VisionScore'][5:].sum()
    return [blue_team,red_team]

def getAssists(game):
    assists = []
    for frame in game['info']['frames'][0:16]:
        for event in frame['events']:
            if event['type'] == 'CHAMPION_KILL':
                assists.append(event) 
    assists_df = pd.DataFrame(assists).dropna()   
    assists_occured = assists_df.assistingParticipantIds
    assists_player_df = defaultdict(int)
    for assist in assists_occured:
        for death in assist:
            if death in assists_player_df:
                assists_player_df[death] += 1
            else:
                assists_player_df[death] = 1    
    assists_player_df = pd.DataFrame([assists_player_df]).T.reset_index()
    blank_df = pd.DataFrame({'player':[1,2,3,4,5,6,7,8,9,10]}) 
    game_assists_sb = pd.merge(blank_df, assists_player_df, how="outer", left_on=blank_df.player, right_on=assists_player_df['index'])
    game_assists = game_assists_sb[[0]]
    blue_team = game_assists[0][0:5].sum()
    red_team = game_assists[0][5:].sum()
    return [blue_team,red_team]

def getcs(game):
    participants_15 = pd.DataFrame.from_dict(pd.DataFrame(pd.DataFrame(game)['info'][4])['participantFrames'][15])
    participants_15_df = participants_15.T[['participantId','jungleMinionsKilled','minionsKilled','level']]
    participants_15_df['cs'] = participants_15_df['jungleMinionsKilled'] + participants_15_df['minionsKilled']
    blank_df = pd.DataFrame({'player':[1,2,3,4,5,6,7,8,9,10]}) 
    game_cs_sb = pd.merge(blank_df, participants_15_df, how="outer", left_on=blank_df.player, right_on=participants_15_df['participantId'])
    game_cs = game_cs_sb[['cs']]
    blue_team = game_cs['cs'][0:5].sum()
    red_team = game_cs['cs'][5:].sum()
    return [blue_team, red_team]


def getlevel(game):
    participants_15 = pd.DataFrame.from_dict(pd.DataFrame(pd.DataFrame(game)['info'][4])['participantFrames'][15])
    participants_15_df = participants_15.T[['participantId','jungleMinionsKilled','minionsKilled','level']]
    blank_df = pd.DataFrame({'player':[1,2,3,4,5,6,7,8,9,10]}) 
    game_levels_sb = pd.merge(blank_df, participants_15_df, how="outer", left_on=blank_df.player, right_on=participants_15_df['participantId'])
    game_levels = game_levels_sb[['level']]
    blue_team = game_levels['level'][0:5].sum()
    red_team = game_levels['level'][5:].sum()
    return [blue_team, red_team]

ELITE_MONSTER_KILL = []
def getELITE_MONSTER_KILL(game):
    ELITE_MONSTER_KILL = []
    for frame in game['info']['frames'][0:16]:
        for event in frame['events']:
            if event['type'] == 'ELITE_MONSTER_KILL':
                ELITE_MONSTER_KILL.append(event) 
    ELITE_MONSTER_KILL = pd.DataFrame(ELITE_MONSTER_KILL)
    if 'monsterSubType' in ELITE_MONSTER_KILL.columns:
        return ELITE_MONSTER_KILL[['killerTeamId','monsterType', 'monsterSubType']]
    else:
        if len(ELITE_MONSTER_KILL.columns) >= 1:
            ELITE_MONSTER_KILL['monsterSubType'] = ELITE_MONSTER_KILL['monsterType'].replace('DRAGON',0)
            return ELITE_MONSTER_KILL[['killerTeamId','monsterType', 'monsterSubType']]
        else:
            return None
        

def getwin(game):
    getoutcome = {}
    for outcome in pd.DataFrame(game)['info'][15]:
        if outcome['win'] == True:
             getoutcome.update({outcome['teamId']:outcome['win']})
    if list(getoutcome.keys())[0] == 100:
        return 'Blue'
    else:
        return 'Red'
    
def getBuildingDestroyed(game):
    building_destroyed = []
    for frame in game['info']['frames'][0:16]:
        for event in frame['events']:
            if event['type'] == 'BUILDING_KILL':
                building_destroyed.append(event)
    building_destroyed_df = pd.DataFrame(building_destroyed)        
    if 'teamId' in building_destroyed_df.columns:
        return building_destroyed_df[['teamId','buildingType','laneType','towerType']]
    else:
        return pd.DataFrame(data = [[0,0,0,0]], columns = ['teamId','buildingType','towerType','laneType'])





























