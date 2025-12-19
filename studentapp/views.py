from django.shortcuts import render, get_object_or_404
from adminapp.models import Result
import pandas as pd
import os

# =========================
# VIEW RESULT (Public URL)
# =========================
def view_result(request, slug):
    """
    Student-accessible result page.
    - Uses the unique_slug of Result.
    - Handles missing slugs and missing files gracefully.
    """
    # Get Result object by slug
    result = Result.objects.filter(unique_slug=slug).first()
    if not result:
        # Slug not found
        return render(request, "studentapp/result_not_found.html")

    # Check if file exists
    if not result.file or not os.path.exists(result.file.path):
        return render(request, "studentapp/file_missing.html", {
            "result": result,
            "message": "Result file is not available at this time."
        })

    file_path = result.file.path

    # Read CSV or Excel
    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        else:
            df = pd.read_excel(file_path)
    except Exception as e:
        return render(request, "studentapp/file_missing.html", {
            "result": result,
            "message": f"Error reading the file: {str(e)}"
        })

    # Search by query parameter
    search_query = request.GET.get("q")
    matched_record = None
    if search_query:
        search_query = str(search_query).strip().lower()
        for index, row in df.iterrows():
            row_values = row.astype(str).str.lower()
            if search_query in row_values.values:
                matched_record = row.to_dict()
                break

    # Render the result page
    return render(request, "studentapp/view_result.html", {
        "result": result,
        "matched_record": matched_record,
        "columns": df.columns,
    })
