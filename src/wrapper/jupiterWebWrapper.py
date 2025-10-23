from requests import session

JUPITER_WEB_AUTH = 'https://uspdigital.usp.br/jupiterweb/autenticar'
CLASS_DETAILS_URL = 'https://uspdigital.usp.br/jupiterweb/dwr/call/plaincall/DisciplinaControleDWR.obterDisciplinaEvolucaoCurso.dwr'
SCHEDULE_URL = "https://uspdigital.usp.br/jupiterweb/dwr/call/plaincall/GradeHorariaControleDWR.obterGradeHoraria.dwr"
CLASS_TEACHER_DETAILS_URL = 'https://uspdigital.usp.br/jupiterweb/dwr/call/plaincall/DisciplinaControleDWR.obterTurmaEvolucaoCurso.dwr'

async def authenticate_in_jupiter_web(session: session, username, password):
    try:
        session.post(
            JUPITER_WEB_AUTH,
            params = {
                "codpes": username,
                "senusu": password,
                "url": ""
            }
        )
        return session
    except Exception as e:
        print(f"Could not authenticate in jupter web: {e}")

async def get_schedule_from_jupiter_web(session: session, username):
    try:
        return session.post(
            SCHEDULE_URL,
            params = {
                "callCount":1,
                "nextReverseAjaxIndex":0,
                "c0-scriptName":"GradeHorariaControleDWR",
                "c0-methodName":"obterGradeHoraria",
                "c0-id":0,
                "c0-param0":f"string:{username}",
                "c0-param1":"string:1",
                "batchId":0,
                "instanceId":0,
                "page":"%2Fjupiterweb%2FgradeHoraria",
                "scriptSessionId": "epRedes"
            }
        )
    except Exception as e:
        print(f"Could not load schedule in jupiter web: {e}")

async def get_class_details_from_jupiter_web(session: session, class_code):
    try:
        return session.post(
            CLASS_DETAILS_URL,
            params = {
                'callCount':1,
                'nextReverseAjaxIndex':0,
                'c0-scriptName':'DisciplinaControleDWR',
                'c0-methodName':'obterDisciplinaEvolucaoCurso',
                'c0-id':0,
                'c0-param0':f'string:{class_code}',
                'batchId': 0,
                'instanceId':0,
                'page':'%2Fjupiterweb%2FgradeHoraria%3Fcodmnu%3D4759',
                'scriptSessionId':'epRedes',
            }
        )
    except Exception as e:
        print(f"Could not load class details in jupiter web: {e}")

async def get_class_teacher_details_from_jupiter_web(session: session, class_code):
    try:
        return session.post(
            CLASS_TEACHER_DETAILS_URL, 
            params = {
                'callCount':1,
                'nextReverseAjaxIndex':0,
                'c0-scriptName':'DisciplinaControleDWR',
                'c0-methodName':'obterTurmaEvolucaoCurso',
                'c0-id':0,
                'c0-param0':f'string:{class_code}',
                'batchId':0,
                'instanceId':0,
                'page':'%2Fjupiterweb%2FgradeHoraria%3Fcodmnu%3D4759',
                'scriptSessionId':'epRedes',
            }
        )
    except Exception as e:
        print(f"Could not load class teacher details in jupiter web: {e}")