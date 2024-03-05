from melting_pot.google import gbq
from projects.laas import StageABC


class Env(StageABC):
    _stage = {
        'nextweek': 'nw',
        'www': 'www',
    }


def asdf():
    return gbq(
        '''
        WITH skill_df AS (
        SELECT
            wd_id,
            jd,
            STRUCT(
            JSON_EXTRACT_STRING_ARRAY(skills_json) AS skills
            ) skill
        FROM `wanted_ml.jd_skills_json`)

        SELECT DISTINCT skill_name_flattened as content FROM skill_df
        CROSS JOIN UNNEST(skill.skills) AS skill_name_flattened
        '''
    , Env.config("_stage"))


if __name__ == '__main__':
    res = asdf()
