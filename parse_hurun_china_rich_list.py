# parse data from Hurun China Rich List

import json
import pandas as pd


def parsing_rich_list():
    # create a dataframe to store rich people info
    df = pd.DataFrame(columns=['company_cn', 'company_en', 'industry_cn', 'industry_en', 'rank_year',
                               'wealth_rmb', 'wealth_usd', 'company_head_quarters_cn', 'company_head_quarters_en',
                               'name_cn', 'gender', 'age', 'birth_place_cn', 'birth_place_en', 'birthday',
                               'permanent_cn', 'permanent_en', 'university_cn', 'university_en', 'education_cn',
                               'character_index'])

    # Match original names to my dataframe column names
    name_match_dict = {
        "hs_Rank_Rich_ComHeadquarters_Cn": "company_head_quarters_cn",
        "hs_Rank_Rich_ComHeadquarters_En": "company_head_quarters_en",
        "hs_Rank_Rich_ComName_Cn": "company_cn",
        "hs_Rank_Rich_ComName_En": "company_en",
        "hs_Rank_Rich_Industry_Cn": "industry_cn",
        "hs_Rank_Rich_Industry_En": "industry_en",
        "hs_Rank_Rich_Year": "rank_year",
        "hs_Rank_Rich_Wealth": "wealth_rmb",
        "hs_Rank_Rich_Wealth_USD": "wealth_usd",
        "hs_Character_Age": "age",
        "hs_Character_BirthPlace_Cn": "birth_place_cn",
        "hs_Character_BirthPlace_En": "birth_place_en",
        "hs_Character_Birthday": "birthday",
        "hs_Character_Education_Cn": "education_cn",
        "hs_Character_Fullname_Cn": "name_cn",
        "hs_Character_Gender": "gender",
        "hs_Character_Permanent_Cn": "permanent_cn",
        "hs_Character_Permanent_En": "permanent_en",
        "hs_Character_School_Cn": "university_cn",
        "hs_Character_School_En": "university_en"
    }

    with open('Hurun China Rich List.txt', 'r', encoding='utf-8') as f:
        for line in f:
            rank_rows = json.loads(line, encoding='utf-8')['rows']
            for item in rank_rows:
                # company info related fields

                company_fields = [
                    "hs_Rank_Rich_ComHeadquarters_Cn",
                    "hs_Rank_Rich_ComHeadquarters_En",
                    "hs_Rank_Rich_ComName_Cn",
                    "hs_Rank_Rich_ComName_En",
                    "hs_Rank_Rich_Industry_Cn",
                    "hs_Rank_Rich_Industry_En",
                    "hs_Rank_Rich_Year",
                    "hs_Rank_Rich_Wealth",
                    "hs_Rank_Rich_Wealth_USD"
                ]

                # get data from original json
                company_info = {name_match_dict[key]: item.get(key) for key in company_fields}

                # person info related fields
                person_fields = [
                    "hs_Character_Age",
                    "hs_Character_BirthPlace_Cn",
                    "hs_Character_BirthPlace_En",
                    "hs_Character_Birthday",
                    "hs_Character_Education_Cn",
                    "hs_Character_Fullname_Cn",
                    "hs_Character_Gender",
                    "hs_Character_Permanent_Cn",
                    "hs_Character_Permanent_En",
                    "hs_Character_School_Cn",
                    "hs_Character_School_En"
                ]
                # get data from original json
                for ix, Character in enumerate(item["hs_Character"]):
                    person_info = {name_match_dict[key]: Character.get(key) for key in person_fields}
                    person_info['character_index'] = ix     # some companies are owned by couples

                    all_info = {**company_info, **person_info}    # merge two dicts

                    # insert info into df
                    df = df.append(all_info, ignore_index=True)

    # write data to csv
    df.to_csv('HurunChinaRichList.csv', mode='a+', encoding='utf_8_sig')


if __name__ == "__main__":
    parsing_rich_list()
