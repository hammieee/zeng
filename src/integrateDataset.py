import pandas as pd

'''
1. integrateDataset() integrates datasets from:
- Group 5
- Group 8
- Groop 29
2. replaces empty fields with NaN
3. Returns integrated dataset as csv file
'''

def integrateDataset():
    url = [
        'https://raw.githubusercontent.com/hammieee/zeng/main/Ransomware%20Logs/24016-48619%20-%20MUHAMMAD%20FA-AIZ%20BIN%20MOHAMMAD%20FAMMI%20.%20-%20Oct%2026%2C%202022%20438%20AM/Gp29_Coursework%201%20dataset/Gp29_Coursework%201%20dataset/T1537_kibana_clean_Gp29_MohamadLutfee.csv',
        'https://raw.githubusercontent.com/hammieee/zeng/main/Ransomware%20Logs/24016-48619%20-%20MUHAMMAD%20FA-AIZ%20BIN%20MOHAMMAD%20FAMMI%20.%20-%20Oct%2026%2C%202022%20438%20AM/Gp29_Coursework%201%20dataset/Gp29_Coursework%201%20dataset/T1589_kibana_clean_Gp29_NicholasLum.csv',
        'https://raw.githubusercontent.com/hammieee/zeng/main/Ransomware%20Logs/24016-48619%20-%20MUHAMMAD%20FA-AIZ%20BIN%20MOHAMMAD%20FAMMI%20.%20-%20Oct%2026%2C%202022%20438%20AM/Gp29_Coursework%201%20dataset/Gp29_Coursework%201%20dataset/T1003.001_kibana_clean_Gp29_MuhammadFa-aiz.csv',
        'https://raw.githubusercontent.com/hammieee/zeng/main/Ransomware%20Logs/24016-48619%20-%20MUHAMMAD%20FA-AIZ%20BIN%20MOHAMMAD%20FAMMI%20.%20-%20Oct%2026%2C%202022%20438%20AM/Gp29_Coursework%201%20dataset/Gp29_Coursework%201%20dataset/T1486_kibana_clean_Gp29_TohXianYong.csv',
        'https://raw.githubusercontent.com/hammieee/zeng/main/Ransomware%20Logs/24016-48619%20-%20MUHAMMAD%20FA-AIZ%20BIN%20MOHAMMAD%20FAMMI%20.%20-%20Oct%2026%2C%202022%20438%20AM/Gp29_Coursework%201%20dataset/Gp29_Coursework%201%20dataset/T1563_kibana_clean_Gp29_VannessaHo.csv',
        'https://raw.githubusercontent.com/hammieee/zeng/main/Ransomware%20Logs/24016-48619%20-%20MUHAMMAD%20FA-AIZ%20BIN%20MOHAMMAD%20FAMMI%20.%20-%20Oct%2026%2C%202022%20438%20AM/Gp29_Coursework%201%20dataset/Gp29_Coursework%201%20dataset/T1566.002_kibana_clean_Gp29_LeeYenNing.csv',
        "https://raw.githubusercontent.com/hammieee/zeng/main/Ransomware%20Logs/23992-48619%20-%20KEVIN%20POOK%20YUAN%20KAI%20.%20-%20Oct%2026%2C%202022%20507%20AM/Gp08_dataset/T1053_auditbeat_clean_Gp08_IanPehShunWei.csv",
        "https://raw.githubusercontent.com/hammieee/zeng/main/Ransomware%20Logs/23992-48619%20-%20KEVIN%20POOK%20YUAN%20KAI%20.%20-%20Oct%2026%2C%202022%20507%20AM/Gp08_dataset/T1068_auditbeat_clean_Gp08_JeremyJevonChowZiYou.csv",
        "https://raw.githubusercontent.com/hammieee/zeng/main/Ransomware%20Logs/23992-48619%20-%20KEVIN%20POOK%20YUAN%20KAI%20.%20-%20Oct%2026%2C%202022%20507%20AM/Gp08_dataset/T1486_auditbeat_clean_Gp08_ChamZhengHanDonovan.csv",
        "https://raw.githubusercontent.com/hammieee/zeng/main/Ransomware%20Logs/23992-48619%20-%20KEVIN%20POOK%20YUAN%20KAI%20.%20-%20Oct%2026%2C%202022%20507%20AM/Gp08_dataset/T1548_auditbeat_clean_Gp08_JeremyJevonChowZiYou.csv",
        "https://raw.githubusercontent.com/hammieee/zeng/main/Ransomware%20Logs/23992-48619%20-%20KEVIN%20POOK%20YUAN%20KAI%20.%20-%20Oct%2026%2C%202022%20507%20AM/Gp08_dataset/T1552_auditbeat_clean_Gp08_LimJinTaoBenjamin.csv",
        "https://raw.githubusercontent.com/hammieee/zeng/main/Ransomware%20Logs/23992-48619%20-%20KEVIN%20POOK%20YUAN%20KAI%20.%20-%20Oct%2026%2C%202022%20507%20AM/Gp08_dataset/T1554_auditbeat_clean_Gp08_IanPehShunWei.csv",
        "https://raw.githubusercontent.com/hammieee/zeng/main/Ransomware%20Logs/Anne/MITRE%20Attack%20Clean%20Logs/T1053_auditbeat_clean_Gp5_YeoZiWei.csv",
        "https://raw.githubusercontent.com/hammieee/zeng/main/Ransomware%20Logs/Anne/MITRE%20Attack%20Clean%20Logs/T1068_auditbeat_clean_Gp5_YeoZiWei_sudoExploit.csv",
        "https://raw.githubusercontent.com/hammieee/zeng/main/Ransomware%20Logs/Anne/MITRE%20Attack%20Clean%20Logs/T1486_auditbeat_clean_Gp5_NurShahidahBinteImran.csv",
        "https://raw.githubusercontent.com/hammieee/zeng/main/Ransomware%20Logs/Anne/MITRE%20Attack%20Clean%20Logs/T1560.001_auditbeat_clean_Gp5_SuEnSiobhan.csv",
        "https://raw.githubusercontent.com/hammieee/zeng/main/Ransomware%20Logs/Anne/MITRE%20Attack%20Clean%20Logs/T1083_clean_Gp5_AnneTanCiEn.csv",
        "https://raw.githubusercontent.com/hammieee/zeng/main/Ransomware%20Logs/Anne/MITRE%20Attack%20Clean%20Logs/T1083_clean_Gp5_AnneTanCiEn_fileCreation.csv",
        "https://raw.githubusercontent.com/hammieee/zeng/main/Ransomware%20Logs/Anne/MITRE%20Attack%20Clean%20Logs/T1053.003_T1543.002_auditbeat_clean_Gp5_NgYongQuanAlfred.csv"]

    result = []
    key = ["host.name", "process.args", "file.path", "event.action", "user.name.text"]
    dataframe = ""

    for i in range(len(url)):
        keyA = key.copy()
        df = pd.read_csv(url[i])
        df = df.replace('-$', 'NaN', regex=True)
        df = df.replace('^\s$', 'NaN', regex=True)
        df.replace('^\d\d\d\d\d\d\d\d\d$', '', regex=True)

        for j in key:
            if j not in list(df):
                keyA.remove(j)
        result.append(df.loc[:, keyA])

    showcase = pd.concat(result)
    showcase.replace('^\d\d\d\d\d\d\d\d\d$', '', regex=True)
    showcase.fillna('NaN', inplace=True)

    showcase.to_excel('out.xlsx', index=False)
    showcase.to_csv('out.csv', index=False)

    return ('out.csv')