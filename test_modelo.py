import joblib

def test_model_prediction_range():
    model = joblib.load('../backend/modelo_review.pkl')
    sample = [4, 4, 4, 4, 4]
    pred = model.predict([sample])
    assert int(pred[0]) in range(1, 6)
