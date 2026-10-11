# importing library 
import dlib
import numpy as np 
import face_recognition_models
from sklearn.svm import SVC
import streamlit as st 

from src.database.db import get_all_students


@st.cache_resource
def load_dlib_models():
    detector = dlib.get_frontal_face_detector()

    sp = dlib.shape_predictor(
        face_recognition_models.pose_predictor_model_location()
    )
    
    facerec = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )

    return detector, sp , facerec

def get_face_embeddings(image_np):
    detector, sp , facerec = load_dlib_models()
    faces = detector(image_np ,1)

    encodings =[]

    for face in faces:
        shape = sp(image_np,face)
        face_descriptor = facerec.compute_face_descriptor(image_np,shape,1) # 128 Dimentions

        encodings.append(np.array(face_descriptor))
    return encodings
@st.cache_resource
def get_trained_model():
    x = []
    y = []

    student_db = get_all_students()

    if not student_db:
        return None 
    for student in student_db:
        embedding = student.get("face_embedding")
        if embedding:
            x.append(np.array(embedding))
            y.append(student.get("student_id"))

    if len(x) == 0:
        return 0
    clf = SVC(kernel="linear",probability=True,class_weight="balanced")

    try:
        clf.fit(x , y)
    except ValueError:
        pass
    return {'clf': clf , "X":x,"Y":y}


def train_classifier():
    st.cache_resource.clear()
    model_data = get_trained_model()
    return bool(model_data)

def predict_attendance(class_image_np):
    encoding  = get_face_embeddings(class_image_np)

    detected_students = {}

    model_data = get_trained_model()

    if not model_data:
        return detected_students , [],len(encoding)

    clf = model_data["clf"]
    X_train =model_data["X"]
    y_train =model_data["Y"]

    all_students = sorted(list(set(y_train)))

    for encode in encoding:
        # numnber of students are greater than 2 
        if len(all_students)>=2:
            predicted_id = int(clf.predict([encode])[0])
        # in frame only one students in 
        else:
            predicted_id =int(all_students[0])

        # we get exact embedding in store with registration 
        student_embedding =  X_train[y_train.index(predicted_id)]

        #after time of matching  : we are checking that mathematically face can match 
        best_match_score = np.linalg.norm(student_embedding - encode)

        # if set a thershold value if diffrence of both face embedding is very high 
        resemblance_threshold =0.6 

        if best_match_score <= resemblance_threshold:
            detected_students[predicted_id] = True
    return detected_students, all_students, len(encoding)