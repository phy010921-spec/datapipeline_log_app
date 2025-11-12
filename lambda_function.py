import base64
import json
import mysql.connector

def lambda_handler(event, context):
    # DB connect -> event data parsing -> 예약 확정된 사람 -> DB
    db_config = {
        "user":"admin",
        "password":"lgu8mkmk!",
        "host":"lgu8-mk.cp44qmmosojx.ap-northeast-2.rds.amazonaws.com",
        "database":"ye_logdata",
    }

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    for record in event["Records"]:
        record_data = base64.b64decode(record["kinesis"]["data"]).decode("utf-8")
        data = json.loads(record_data)

        if data["reserv"] == "yes":
            # CREATE Query
            strSql = """
                INSERT INTO saas_log (time, user_id, servicemenu, stars, access_type, reserve) 
                VALUES (%s, %s, %s, %s, %s, %s);
            """
            values = (
                data["time"],
                data["user_id"],
                data["state"],
                data["stars"],
                data["accesstype"],
                data["reserv"]
            )

            cursor.execute(strSql, values)
            connection.commit()
    cursor.close()
    connection.close()

    return {
        "return_code" : 200,
    }