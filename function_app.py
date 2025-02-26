import azure.functions as func
import logging
from sum_model import summarize_text
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="summarize")
def summarize(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    text = req.params.get('text')
    if not text:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            text = req_body.get('text')

    if text:
        summary = summarize_text(text)
        return func.HttpResponse(
            json.dumps({'summary': summary}),
            mimetype="application/json",      
            status_code=200
        )
    
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a text in the query string or in the request body for a summary.",
             status_code=200
        )