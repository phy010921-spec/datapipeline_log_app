import datetime
from django.shortcuts import render
import random
import requests as req
import json

from log.models import AptCost
from bs4 import BeautifulSoup

import mysql.connector


# Create your views here.
def get_log(key):
    current_time = datetime.datetime.now()
    #현재날짜를 long type으로 표현
    timestamp = int(current_time.timestamp() * 1000)

    time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    events= {
        1: {'event': 'lgu_app_01', 'timestamp': timestamp, 'local_time': time, 'item_id': '01-001',
            'bt_desc': '식품-과일', 'access_type': 'phone', 'amount': random.randint(1, 5)},
        2: {'event': 'lgu_app_01', 'timestamp': timestamp, 'local_time': time, 'item_id': '01-002',
            'bt_desc': '식품-견과/건과', 'access_type': 'web', 'amount': random.randint(1, 5)},
        3: {'event': 'lgu_app_01', 'timestamp': timestamp, 'local_time': time, 'item_id': '01-003',
            'bt_desc': '식품-채소', 'access_type': 'phone', 'amount': random.randint(1, 5)},
        4: {'event': 'lgu_app_01', 'timestamp': timestamp, 'local_time': time, 'item_id': '01-004',
            'bt_desc': '식품-쌀/잡곡', 'access_type': 'web', 'amount': random.randint(1, 5)},
        5: {'event': 'lgu_app_01', 'timestamp': timestamp, 'local_time': time, 'item_id': '01-005',
            'bt_desc': '식품-생수/음료', 'access_type': 'phone', 'amount': random.randint(1, 5)},
        6: {'event': 'lgu_app_01', 'timestamp': timestamp, 'local_time': time, 'item_id': '01-006',
            'bt_desc': '식품-건강식품', 'access_type': 'web', 'amount': random.randint(1, 5)},
        7: {'event': 'lgu_app_01', 'timestamp': timestamp, 'local_time': time, 'item_id': '01-007',
            'bt_desc': '식품-간편요리', 'access_type': 'phone', 'amount': random.randint(1, 5)},
        8: {'event': 'lgu_app_01', 'timestamp': timestamp, 'local_time': time, 'item_id': '01-008',
            'bt_desc': '식품-간편식', 'access_type': 'web', 'amount': random.randint(1, 5)},
        9: {'event': 'lgu_app_01', 'timestamp': timestamp, 'local_time': time, 'item_id': '01-009',
            'bt_desc': '식품-유제품', 'access_type': 'phone', 'amount': random.randint(1, 5)},
        10: {'event': 'lgu_app_02', 'timestamp': timestamp, 'local_time': time, 'item_id': '02-001',
             'bt_desc': '생활용품-헤어', 'access_type': 'web', 'amount': random.randint(1, 5)},
        11: {'event': 'lgu_app_02', 'timestamp': timestamp, 'local_time': time, 'item_id': '02-002',
             'bt_desc': '생활용품-바디/세안', 'access_type': 'phone', 'amount': random.randint(1, 5)},
        12: {'event': 'lgu_app_02', 'timestamp': timestamp, 'local_time': time, 'item_id': '02-003',
             'bt_desc': '생활용품-세탁세제', 'access_type': 'web', 'amount': random.randint(1, 5)},
        13: {'event': 'lgu_app_02', 'timestamp': timestamp, 'local_time': time, 'item_id': '02-004',
             'bt_desc': '생활용품-건강', 'access_type': 'phone', 'amount': random.randint(1, 5)},
        14: {'event': 'lgu_app_02', 'timestamp': timestamp, 'local_time': time, 'item_id': '02-005',
             'bt_desc': '생활용품-수납/정리', 'access_type': 'phone', 'amount': random.randint(1, 5)},
        15: {'event': 'lgu_app_02', 'timestamp': timestamp, 'local_time': time, 'item_id': '02-006',
             'bt_desc': '생활용품-안전', 'access_type': 'web', 'amount': random.randint(1, 5)},
        16: {'event': 'lgu_app_02', 'timestamp': timestamp, 'local_time': time, 'item_id': '02-007',
             'bt_desc': '생활용품-생활잡화', 'access_type': 'web', 'amount': random.randint(1, 5)},
        17: {'event': 'lgu_app_03', 'timestamp': timestamp, 'local_time': time, 'item_id': '03-001',
             'bt_desc': '뷰티-헤어', 'access_type': 'phone', 'amount': random.randint(1, 5)},
        18: {'event': 'lgu_app_03', 'timestamp': timestamp, 'local_time': time, 'item_id': '03-002',
             'bt_desc': '뷰티-향수', 'access_type': 'phone', 'amount': random.randint(1, 5)},
        19: {'event': 'lgu_app_03', 'timestamp': timestamp, 'local_time': time, 'item_id': '03-003',
             'bt_desc': '뷰티-남성화장품', 'access_type': 'phone', 'amount': random.randint(1, 5)},
        20: {'event': 'lgu_app_03', 'timestamp': timestamp, 'local_time': time, 'item_id': '03-004',
             'bt_desc': '뷰티-여성화장품', 'access_type': 'web', 'amount': random.randint(1, 5)},
    }
    return events.get(key,"out of bound")

def log_index(request):
    return render(request, "log_index.html")

def log_gen_i(request):
    return render(request, "log_gen_i.html")

def btn_gen_i_click(request, product_id):
    #1~20번 물품을 구매한 정보를 api gw로 전달
    data =get_log(product_id)
    # endpoint_url="https://qo321l50zb.execute-api.ap-northeast-2.amazonaws.com/dev_stage/version1"

    stream_name = "ye_ver2_ki_product"
    endpoint_url=f"https://8zn3xcbft3.execute-api.ap-northeast-2.amazonaws.com/dev_stage/version2/{stream_name}"

    json_data = json.dumps(data)    #dumps() 안에는 딕셔너리 형태가 들어가야 함
    resp = req.post(endpoint_url, data = json_data, headers={"Content-Type":"application/json"})
    print("ye_ver2_ki_product",resp.text)

    #stream_name = "yj_ver2_ki_app"
    #endpoint_url = f"https://qo321l50zb.execute-api.ap-northeast-2.amazonaws.com/dev_stage/version2/{stream_name}"

    #json_data = json.dumps(data)  # dumps() 안에는 딕셔너리 형태가 들어가야 함
    #resp = req.post(endpoint_url, data=json_data, headers={"Content-Type": "application/json"})
    #print("yj_ver2_ki_app",resp.text)

    return render(request, "log_gen_i.html")

def log_gen_ii(request):
    return render(request,"log_gen_ii.html")

def btn_gen_ii_click(request):
    if request.method == "POST" :

        current_time = datetime.datetime.now()
        time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        user_id = request.POST["userid"]
        servicemenu=request.POST["servicemenu"]
        stars = request.POST["stars"]
        accesstype= request.POST["accesstype"]
        reserv = request.POST["reserv"]

        form_data={
            "time": str(time),
            "user_id": str(user_id),
            "state": str(servicemenu),
            "stars": str(stars),
            "accesstype": str(accesstype),
            "reserv": str(reserv),
        }

        # Send to API GW
        # Form data : content type(application/x-www-form-urlencoded)
        stream_name = "ye_ver2_ki_saas_stream"
        endpoint_url = f"https://8zn3xcbft3.execute-api.ap-northeast-2.amazonaws.com/dev_stage/version2/{stream_name}"

        resp = req.post(
            endpoint_url,
            data = form_data,
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
        )

        print(resp.text)

        return render(request, "log_gen_ii.html")


def btn_gen_iii_click(request):
    # 자동로그 app log 생성하기
    # 호텔 예약을 위한 로그 파일 생성재료
    user_pool = ["ace", "phdmk", "keras", "tensor", "pytorch", "gogo", "alice", "korea"]
    service_pool = ["일정보기", "호텔예약", "둘러보기", "예약문의", "예약해지", "상담연결", "추천하기"]
    stars = [1, 2, 3, 4, 5]
    access_type = ["web", "android", "ios"]

    logs = []
    current_time = datetime.datetime.now()
    time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    if request.method == "POST":
        loop_count = int(request.POST["numlog"])

        for i in range(loop_count):
            log_data = {"time": time,
                        "user_id": user_pool[random.randint(0, len(user_pool) - 1)],
                        "service_menu": service_pool[random.randint(0, len(service_pool) - 1)],
                        "stars": str(stars[random.randint(0, len(stars) - 1)]),
                        "access_type": access_type[random.randint(0, len(access_type) - 1)],
                        "isReservation": str(random.randint(0, 1))}
            logs.append(log_data)

        # dict -> str : json.dumps()
        with open("resv_log.log", "a+", encoding = "utf-8") as fd:
            for log in logs:
                fd.write(json.dumps(log, ensure_ascii=False) + "\n")  # 한 줄씩 JSON 문자열로 저장 (ensure_ascii=False --> 한글안깨짐)

        context = {
            "logs": logs
        }
        return render(request, "log_gen_iii.html", context)
    return render(request, "log_gen_iii.html")


def btn_openapi(request):
    return render(request,"open_api.html")


def btn_openapi_click(request):
    # OPEN API URL
    # resp = Request(URL)
    # parsing resp
    # insert db
    # test_url = """
    # https://apis.data.go.kr/1613000/RTMSDataSvcAptTrade/getRTMSDataSvcAptTrade?
    # serviceKey=서비스키&LAWD_CD=11110&DEAL_YMD=202407&pageNo=1&numOfRows=1
    # """

    db_config = {
        "user": "admin",
        "password": "monicloud!",
        "host": "moni.cvk8m0gqs06n.ap - northeast - 2.rds.amazonaws.com",
        "database": "ye_lg8_master",
    }

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    url = "https://apis.data.go.kr/1613000/RTMSDataSvcAptTrade/getRTMSDataSvcAptTrade?"

    for pageNo in range(1, 5):
        params = {
            "serviceKey": "6c5485e04c32d6317693a0c0d7eabfd5659e7be39702277c7b2b11abb5f92583",
            "LAWD_CD": "11110",
            "DEAL_YMD": "202501",
            "pageNo": str(pageNo),
            "numOfRows": "20",
        }

        resp = req.get(url, params=params)
        decoded_data = resp.content.decode("utf-8")
        # print(decoded_data)

        # decoded_data에 대한 paser만들기

        # 1. Dom tree 구성하기
        soup = BeautifulSoup(decoded_data, "xml")

        # "<item>" 태그들만 모두 찾기
        items = soup.find_all("item")

        for index, item in enumerate(items):
            try:
                apt_name = item.find("aptNm").text
                build_year = item.find("buildYear").text
                deal_amount = item.find("dealAmount").text
                deal_day = item.find("dealDay").text
                deal_month = item.find("dealMonth").text
                deal_year = item.find("dealYear").text
                exclu_usearea = item.find("excluUseAr").text
                floor = item.find("floor").text
                land_leaseholdgbn = item.find("landLeaseholdGbn").text
                sgg_cd = item.find("sggCd").text
                umd_nm = item.find("umdNm").text

                try:
                    # DB입력
                    strSql = """
                       INSERT INTO apt_cost (
                            apt_name, build_year, deal_amount, deal_day, deal_month, deal_year, 
                            exclu_usearea, floor, land_leaseholdgbn, sgg_cd, umd_nm
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
                    """
                    data = (apt_name, build_year, deal_amount, deal_day, deal_month, deal_year,
                            exclu_usearea, floor, land_leaseholdgbn, sgg_cd, umd_nm)

                    cursor.execute(strSql, data)
                    cursor.commit()
                    print("success save!!!")

                except mysql.connector.Error as e:
                    print(e)

            except Exception as err:
                print(err)

    if connection.is_connected():
        cursor.close()
        connection.close()

    return render(request, "open_api.html")