from monitoring.models import MonitoringData


def get_filtered_occurrences(day=0, month=0, year=0):
    # Montar o filtro dinâmico
    filters = {}
    if year:
        filters["date__year"] = year
    if month:
        filters["date__month"] = month
    if day:
        filters["date__day"] = day

    # Retornar as ocorrências ordenadas por data
    return MonitoringData.objects.filter(**filters).order_by("date")
