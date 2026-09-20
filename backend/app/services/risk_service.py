# backend/app/services/risk_service.py


from app.config import settings


def normalize(value, minimum, maximum):
    """
    Переводит число в диапазон 0-1

    Например:
    Kp от 0 до 9

    Kp=0  -> 0
    Kp=9  -> 1
    """

    if value <= minimum:
        return 0

    if value >= maximum:
        return 1

    return (value - minimum) / (maximum - minimum)



def calculate_weather_risk(
        kp_index: float,
        proton_flux: float | None = None,
        xray_flux: float | None = None
):
    """
    Расчёт риска от космической погоды
    """

    risks = []


    # Геомагнитная активность
    if kp_index is not None:
        kp_risk = normalize(
            kp_index,
            0,
            9
        )

        risks.append(kp_risk)



    # Радиационные частицы
    if proton_flux is not None:

        proton_risk = normalize(
            proton_flux,
            0,
            100
        )

        risks.append(proton_risk)



    # Рентгеновское излучение
    if xray_flux is not None:

        xray_risk = normalize(
            xray_flux,
            0,
            10
        )

        risks.append(xray_risk)



    # Если данных нет
    if len(risks) == 0:
        return {
            "risk": None,
            "status": "no_data"
        }



    average = sum(risks) / len(risks)


    return {
        "risk": round(average, 3),
        "status": "ok"
    }




def calculate_debris_risk(
        miss_distance_km: float | None
):
    """
    Расчёт риска от сближения
    """

    if miss_distance_km is None:
        return {
            "risk": 0,
            "status": "no_conjunction"
        }



    SAFE_DISTANCE = 100


    risk = 1 - (
        miss_distance_km /
        SAFE_DISTANCE
    )


    if risk < 0:
        risk = 0


    if risk > 1:
        risk = 1


    return {
        "risk": round(risk,3),
        "status": "conjunction"
    }





def calculate_total_risk(
        weather_risk: float,
        debris_risk: float
):
    """
    Итоговый индекс риска
    """


    total = (
        weather_risk *
        settings.weather_weight
        +
        debris_risk *
        settings.debris_weight
    )


    return round(total,3)