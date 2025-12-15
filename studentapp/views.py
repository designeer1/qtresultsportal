from django.shortcuts import render, get_object_or_404
from adminapp.models import Result
import pandas as pd

def view_result(request, slug):
    # get active result
    result = get_object_or_404(Result, unique_slug=slug, is_active=True)
 
    # reading file (CSV or Excel)
    file_path = result.file.path

    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    else:
        df = pd.read_excel(file_path)

    search_query = request.GET.get("q")

    matched_record = None

    # search logic
    if search_query:
        search_query = str(search_query).strip().lower()

        for index, row in df.iterrows():
            row_values = row.astype(str).str.lower()
            if search_query in row_values.values:
                matched_record = row.to_dict()
                break

    return render(request, "studentapp/view_result.html", {
        "result": result,
        "matched_record": matched_record,
        "columns": df.columns,
    })
