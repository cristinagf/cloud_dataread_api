from flask import jsonify
from google.cloud import firestore

def get_resume(request):
    """
    Fetches the resume data from Firestore and returns it as a JSON response.
    """
    # Get resume data from Firestore
    resume_data = firestore.Client().collection('resumes').document('1').get().to_dict()
    # Return JSON response
    return jsonify(resume_data), 200
