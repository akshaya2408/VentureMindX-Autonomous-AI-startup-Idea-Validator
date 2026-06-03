from database.mongodb import report_collection

def save_report(report):

    result = report_collection.insert_one(report)

    return str(result.inserted_id)